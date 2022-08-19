import re

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     rf"""The gradient descent method leads to the phone for the following starting points: """
]

questions = [
     Question(question_prompts[0], "3, 4, 5"),
]

def run_quiz(questions):
    for question in questions:
        answer = input(question.prompt)
        print()
        if set(re.sub(r"[\s+,;.]", "", answer)) == set(re.sub(r"[\s+,;.]", "", question.answer)):
            print('Correct answer. Well done!\n')
        else:
            print(f'Incorrect answer. The correct answer would be: {question.answer}.\n')
            
run_quiz(questions)