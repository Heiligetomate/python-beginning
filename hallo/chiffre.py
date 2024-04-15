import sys


def chiffre(a):
    text = input("Welchen Text? ")
    text = text.lower()
    text = text.replace(" ", "")
    text = list(text)
    key_word = input("Welches Key Wort? ")
    key = list(key_word)
    for i in range(int(len(text) / len(key_word))):
        for i in key_word:
            key.append(i)

    finish = []
    for i in range(len(text)):
        element = ord(text[i])
        result = element - ord(key[i]) - a
        if a == 97:
            result = element + ord(key[i]) - a
        if result > 122:
            result = result - 26
        result = chr(result)
        finish.append(result)

    finish = "".join(finish)
    print(f"Die Übersetzung lautet: {finish}.")


while True:

    print("Was wollen sie machen? ")
    user_input = input("[1] : verschlüsseln\n[2] : entschlüsseln\n[3] : leaven\n")
    if user_input == "2":
        chiffre(-123)

    elif user_input == "1":
        chiffre(97)

    elif user_input == "3":
        print("Bye Bye")
        sys.exit()

    else:
        print("Ungültige Eingabe! ")



