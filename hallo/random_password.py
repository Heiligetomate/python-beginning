
import random as r

characters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
characters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
password = []

print("Hello! Welcome to the password generator!")
while True:
    capital = input("How many capital letters would you like to have in your password? ")
    lower = input("How many Lower case letters letters would you like to have in your password? ")
    special = input("How many special characters would you like to have in your password? ")
    try:
        capital = int(capital)
        lower = int(lower)
        special = int(special)
        break
    except:
        print("Invalid input. Please enter an integer")



for i in range(capital):
    character3 = r.choice(characters_upper)
    password.append(character3)
for i in range(lower):
    character1 = r.choice(characters_lower)
    password.append(character1)
for i in range(special):
    character2 = r.choice(special_characters)
    password.append(character2)
r.shuffle(password)
print(f"Your new password is: {''.join(password)}")