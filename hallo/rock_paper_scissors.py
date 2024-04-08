import random as r

game = ['rock', 'paper', 'scissors']
score = 0
computer_score = 0
computer_choice = r.choice(game)

print("Rock, Paper, Scissors write one of those")

while True:
    computer_choice = r.choice(game)
    user_choice = input("If you want to end the programm press 0\n")
    if user_choice.lower() == computer_choice:
        print("Draw")
        score = score + 0.5
        computer_score = computer_score + 0.5
        print(f'Your score is: {score}')
        print(f"Computer score is: {computer_score}")
    elif user_choice.lower() == 'rock' and computer_choice == 'scissors' or user_choice.lower() == 'paper' and computer_choice == 'rock' or user_choice.lower() == 'scissors' and computer_choice == 'paper':
        print(f"Computers choice was: {computer_choice}")
        print("You win!")
        score = score + 1
        computer_score = computer_score - 1
        print(f'Your score is: {score}')
        print(f"Computer score is: {computer_score}")
    elif user_choice.lower() == 'rock' and computer_choice == 'paper' or user_choice.lower() == 'paper' and computer_choice == 'scissors' or user_choice.lower() == 'scissors' and computer_choice == 'rock':
        print(f"Computers choice was: {computer_choice}")
        print("You lose!")
        score = score - 1
        computer_score = computer_score + 1
        print(f'Your score is: {score}')
        print(f"Computer score is: {computer_score}")
    elif user_choice == '0':
        print(f"Computers choice was: {computer_choice}")
        print(f'Your score is: {score}')
        print(f"Computer score is: {computer_score}")
        if computer_score > score:
            print("Your score is lower than the computer score. You lost!")
            print("better luck next time!")
        else:
            print("Your score is higher than the computer score. You won!")
            print('You should play more games of chances!')
        break
    elif user_choice.lower() == 'fountain':
        print("Wow you found the easter egg! With the fountain you'll always win.")
        score = score + 100
        computer_score = computer_score - 100
        print(f"Your score is: {score}")
        print(f"Computer score is: {computer_score}")
    else:
        print("Please enter rock, paper, or scissors!!! Now you will get penalty points!")
        score = score -0.5
        print(f"Your score is: {score}")
        print(f"Computer score is: {computer_score}")
    print("New round! The computer never gets tired.")
