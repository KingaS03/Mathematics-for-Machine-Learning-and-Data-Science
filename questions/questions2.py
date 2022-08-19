class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     rf"""What is the variance of the following data points X = {-2, 1, 3, 6}?\nProvide the answer with a precision of two decimal places: """,
     rf"""What happens with the variance if we shift the data set by 3 to the right?\n(a) The variance remains the same. \n(b) The variance gets shifted by -3.\n(c) The variance gets shifted by 3.\nType the letter of the correct answer: """,
     rf"""What happens if we scale the data points by a factor 1/2?\n(a) The variance is multiplied by a factor of 1/2.\n(b) The variance is multiplied by a factor of 1/4.\n(c) The variance is multiplied by a factor of 4.\n(d) The variance is multiplied by a factor of 2.\n(e) The variance remains the same.\nType the letter of the correct answer: """
]

questions = [
     Question(question_prompts[0], "8.5"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "b")
]

def run_quiz(questions):
    for question in questions:
        answer = input(question.prompt)
        print()
        if answer == question.answer:
            print('Correct answer. Well done!\n')
        else:
            print(f'Incorrect answer. The correct answer would be: {question.answer}.\n')
            
run_quiz(questions)