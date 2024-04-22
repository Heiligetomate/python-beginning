import time as t
score = 0

print("Welcome to the math trainer!")


def math_exercise (exercise, time_remaining, result, points, minus_points):
    score = 0
    print(f"Exercise: {exercise}. You have {time_remaining} seconds to solve this.")
    time = t.time()
    user_input = input("What is your answer? ")
    t_now = t.time()

    if t_now - time > time_remaining:
        print('Your time was up!')
        score = score - minus_points * 0.5
    else:
        if int(user_input) == result:
            print('Correct!')
            score = score + points
        else:
            print('Wrong!')
            score = score - minus_points
    print(f"Your score is {score}")
    return score


score1 = math_exercise("What is 1 + 2?", 3, 3, 2, 10)
print(f"Your score is {score1}")
score2 = math_exercise("What is 123 + 5?", 4, 128, 4, 6)
result_score = score1 + score2
print(f"Your total score is {result_score} ")
score1 = math_exercise("What is 12 * 5?", 5, 60, 5, 5)
result_score = result_score + score1
print(f"Your total score is {result_score} ")
score1 = math_exercise("What is 606 / 6?", 5, 101, 4, 4)
result_score = result_score + score1
print(f"Your total score is {result_score} ")
score1 = math_exercise("What is 4 ^ 3?", 6, 64, 5, 5)
result_score = result_score + score1
print(f"Your total score is {result_score} ")
print("Bye! If you want to learn real math DONT PLAY THIS GAME! Watch Youtube orw something like this.")