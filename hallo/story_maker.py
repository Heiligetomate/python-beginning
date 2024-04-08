from sound import *

while True:
    user_input = input("Do you want to create a Mad Lib? ")
    if user_input.lower() == "yes":
        sound('audio_files', 'zisch')
        noun_plural = input("Enter a noun in plurial: ")
        sound('audio_files', 'zisch')
        color = input("Enter a colour: ")
        sound('audio_files', 'zisch')
        color2 = input("Enter a colour: ")
        sound('audio_files', 'zisch')
        flower_plural = input("Enter a flower in plurial: ")
        sound('audio_files', 'zisch')
        noun = input("Enter a noun: ")
        sound('audio_files', 'zisch')
        verb = input("Enter a verb: ")
        sound('audio_files', 'zisch')

        print(f'{noun_plural} are {color}')
        print(f'{flower_plural} are {color2}')
        print(f'I {verb} {noun}')
        sound('audio_files', 'belohnung')

    elif user_input.lower() == "no":
        print("bye bye Kartoffelbrei!")
        break

    else:
        print("I didn't understand. Please try again.") 