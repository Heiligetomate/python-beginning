def chiffre(text, key, finish, number):
    for i in range(len(text)):
        value = ord(key[i])
        value = value + number
        element = ord(text[i])
        result = element + value
        if result > 122:
            result = result - 26
        result = chr(result)
        finish.append(result)

    finish = "".join(finish)
    print(f"Die Übersetzung lautet: {finish}.")

def loop():
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
    return key, text

finish = []
key, text = loop()
chiffre(text, key, finish, 123)