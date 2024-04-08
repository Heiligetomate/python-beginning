import sys


while True:
    user_input = input("[1] : verschlüsseln\n[2] : entschlüsseln\n[3] : leaven\n")
    if user_input == "2":
        # ZUM ENTSCHLÜSSELN
        text = input("Welchen Text? ")
        text = text.lower()
        text = text.replace(" ", "")
        text = list(text)
        digit = input("Welches Wort? ")
        key = list(digit)
        len_text = len(text)
        len_digit = len(digit)
        for i in range(int(len_text / len_digit)):
            for i in digit:
                key.append(i)

        finish = []
        for i in range(len_text):
            add = ord(key[i])

            element = ord(text[i])
            result = element - add + 123
            if result > 122:
                result = result - 26
            result = chr(result)
            finish.append(result)
        finish = "".join(finish)
        print(f"Die Übersetzung lautet: {finish}.")

    elif user_input == "1":
        text = input("welchen Text? ")
        text = text.lower()
        text = text.replace(" ", "")
        text = list(text)
        digit = input("Welches Key_word? ")
        key = list(digit)
        len_text = len(text)
        len_digit = len(digit)
        for i in range(int(len_text / len_digit)):
            for i in digit:
                key.append(i)

        finish = []
        for i in range(len_text):
            value = ord(key[i])
            value = value - 97
            element = ord(text[i])
            result = element + value
            if result > 122:
                result = result - 26
            result = chr(result)
            finish.append(result)

        finish = "".join(finish)
        print(f"Die Übersetzung lautet: {finish}.")

    elif user_input == "3":
        print("Bye Bye")
        sys.exit()

    else:
        print("Ungültige Eingabe! ")



