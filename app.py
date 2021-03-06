import os
from flask import Flask, render_template, request, session, escape, redirect, url_for
from data import quiz

app = Flask(__name__)


def clear_session():
    session.pop("ca", None)
    session.pop("ac", None)


@app.route("/session_test")
def session_test():
    if "test_key" in session:
        return "Session test_key: %s" % escape(session["test_key"])

    return "no test_key in session"


@app.route("/session_clean")
def session_clean():
    session.pop("test_key", None)
    return "removed test_key from session"


@app.route("/session_set")
def session_set():
    session["test_key"] = os.urandom(24)
    return "generated test_key into session"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("hello"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    clear_session()
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/restart")
def restart():
    clear_session()
    return redirect(url_for("hello"))


@app.route("/")
def hello():
    if "username" not in session:
        return redirect(url_for("login"))

    correct_answers = 0
    if "ca" in session:
        correct_answers = session["ca"]

    answered_questions = []
    if "ac" in session:
        answered_questions = session["ac"]

    correct = False
    n = request.args.get("n")
    if n == None:
        n = 0
    n = int(n)

    question = quiz.questions[n]

    answer_id = request.args.get("answer_id")
    if answer_id != None:
        n = n + 1
        correct = question.correct_id == int(answer_id)

        if (n - 1) not in answered_questions:
            answered_questions.append(n - 1)
            session["ac"] = answered_questions
            if correct:
                correct_answers += 1
                session["ca"] = correct_answers

    if n >= len(quiz.questions):
        clear_session()

        return render_template(
            "end.html",
            correct_answers=correct_answers,
        )
    else:
        return render_template(
            "index.html",
            quiz=quiz,
            question=quiz.questions[n],
            n=n,
            correct=correct,
        )


app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
