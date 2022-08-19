class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     rf"""What is the mean value of the following data points X = {-2, 1, 3, 6}?\nProvide the answer with a precision of two decimal places: """,
     rf"""What happens with the mean if we shift the data set by 3 to the right?\n(a) The mean remains the same. \n(b) The mean gets shifted by -3.\n(c) The mean gets shifted by 3.\nType the letter of the correct answer: """,
     rf"""What happens if we scale the data points by a factor 1/2?\n(a) The mean is multiplied by a factor of 1/2.\n(b) The mean is multiplied by a factor of 2.\n(c) The mean remains the same.\nType the letter of the correct answer: """
]

questions = [
     Question(question_prompts[0], "2"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "a")
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