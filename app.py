import os
import random
from flask import (
    Flask,
    render_template,
    request,
    session,
    escape,
    redirect,
    url_for,
    abort,
)
from data import quiz

app = Flask(__name__)


def clear_session():
    session.pop("ca", None)
    session.pop("ac", None)


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

    if "current_question" not in session:
        question = quiz.questions[random.randrange(0, len(quiz.questions) - 1)]
        session["current_question"] = question.id
        return render_template(
            "index.html",
            quiz_name=quiz.name,
            question=question,
            correct=False,
        )

    current_question = session["current_question"]

    correct_answers = 0
    if "ca" in session:
        correct_answers = session["ca"]

    answered_questions = []
    if "ac" in session:
        answered_questions = session["ac"]

    correct = False

    question = None
    for q in quiz.questions:
        if q.id == current_question:
            question = q
            break

    if question == None:
        abort(404)

    answer_id = request.args.get("answer_id")
    if answer_id != None:
        correct = question.correct_id == int(answer_id)
        if question.id not in answered_questions:
            answered_questions.append(question.id)
            session["ac"] = answered_questions
            if correct:
                correct_answers += 1
                session["ca"] = correct_answers

    if len(answered_questions) == len(quiz.questions):
        clear_session()

        return render_template(
            "end.html",
            correct_answers=correct_answers,
        )
    else:
        for q in random.sample(quiz.questions, len(quiz.questions)):
            if q.id not in answered_questions:
                session["current_question"] = q.id
                return render_template(
                    "index.html",
                    quiz_name=quiz.name,
                    question=q,
                    correct=correct,
                )


app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
