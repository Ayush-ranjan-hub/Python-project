class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer.lower():
            score += 1
    print("You got", score, "out of", len(questions), "correct!")


# Create a list of questions
question_list = [
    Question("What is the capital of France? ", "Paris"),
    Question("Who painted the Mona Lisa? ", "Leonardo da Vinci"),
    Question("What is the largest planet in our solar system? ", "Jupiter"),
    Question("What year was Python first released? ", "1991")
]

# Run the quiz
run_quiz(question_list)
