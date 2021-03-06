import os
from flask import Flask, render_template, request, session, escape
from data import quiz

app = Flask(__name__)


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


@app.route("/")
def hello():
    correct_answers = 0
    if "ca" in session:
        correct_answers = session["ca"]

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
        if correct:
            correct_answers += 1
            session["ca"] = correct_answers

    if n >= len(quiz.questions):
        session.pop("ca", None)

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
