#Quizzzzz
def quiz_game():
    class quizz:

        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer


    question_register = ["What color are apples? \na : green and red \nb : yellow \nc : blue\n",
                         "What color are orange? \na : green and red \nb : orange \nc : blue\n",
                         "What color are bananas? \na : green and red \nb : yellow \nc : blue\n"]


    questions = [quizz(question_register[0], 'a'),
                 quizz(question_register[1], 'b'),
                 quizz(question_register[2], 'b')]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                print("That's True!")
                score = score + 1
        print(f'Your score is {score}')

    run_test(questions)

