# Schacheroeffnung in besser

colour_options = {
    '1': "Wollen sie wollen eine Eröffnung für Schwarz finden?",
    '2': "Wollen sie wollen eine Eröffnung für Weiß finden?"
}

# 0
bauer_options = {
    "1": "Wollen sie etwas gegen e4 finden?",
    "2": "Wollen sie etwas gegen d4 finden?",
    "3": "Wollen sie etwas gegen etwas Anderes finden?"
}

bauer_options_one = {
    "1": "Sie wollen eine Eröffnung gegen e4 fiden?",
    "2": "Sie wollen eine Eröffnung gegen d4 fiden?",
    "3": "Sie wollen eine Eröffnung gegen den rest fiden?"
}

bekannte_eroeffnung = {
    "1": "Wollen sie eine eher populäre Eröffnung finden?",
    "2": "Wollen sie eine eher unpopuläre Eröffnung finden?",
}

bekannte_eroeffnung_one = {
    "1": "Wollen sie eine eher populäre Eröffnung finden?",
    "2": "Wollen sie eine eher unpopuläre Eröffnung finden?",
}

option_one = [bauer_options_one, bauer_options]
options_in_option_two = [bekannte_eroeffnung, bekannte_eroeffnung]


def choose_number(options):
    print("Bitte auswählen. ")
    while True:
        for k, v in options.items():
            print(f"[{k}] : {v}")
        a = input()
        for i in options.keys():
            if a == i:
                return int(a) - 1
        print("Ungültig! ")


input1 = choose_number(colour_options)
next_options = option_one[input1]

input_option_two = choose_number(next_options)
