from flask import Flask, render_template, request
from data import quiz

app = Flask(__name__)


@app.route("/")
def hello():
    correct_answers = request.args.get("ca")
    if correct_answers == None:
        correct_answers = 0
    correct_answers = int(correct_answers)

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

    if n >= len(quiz.questions):
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
            correct_answers=correct_answers,
        )
