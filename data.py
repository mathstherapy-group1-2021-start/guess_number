class Answer:
    def __init__(self, text, id):
        self.id = id
        self.text = text


class Question:
    def __init__(self, text, answers, correct_id):
        self.text = text
        self.answers = answers
        self.correct_id = correct_id


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions


quiz = Quiz(
    name="Самая первая викторина!",
    questions=[
        Question(
            text="question 1",
            correct_id=1,
            answers=[
                Answer(text="answer 1.1", id=1),
                Answer(text="answer 1.2", id=2),
                Answer(text="answer 1.3", id=3),
                Answer(text="answer 1.4", id=4),
            ],
        ),
        Question(
            text="question 2",
            correct_id=2,
            answers=[
                Answer(text="answer 2.1", id=1),
                Answer(text="answer 2.2", id=2),
                Answer(text="answer 2.3", id=3),
                Answer(text="answer 2.4", id=4),
            ],
        ),
        Question(
            text="question 3",
            correct_id=3,
            answers=[
                Answer(text="answer 3.1", id=1),
                Answer(text="answer 3.2", id=2),
                Answer(text="answer 3.3", id=3),
                Answer(text="answer 3.4", id=4),
            ],
        ),
    ],
)
