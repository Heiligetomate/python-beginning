import random as r

while True:
    user_input = input("Wollen sie würfeln? ")
    if user_input.lower() == "ja":
        test = r.randint(1, 6)
        print("Sie haben eine " + str(test) + " gewürfelt.")
    elif user_input.lower() == "nein":
        print("bye bye Kartoffelbrei!")
        break

    else:
        print("Das War kein Ja! Wenn sie nicht mehr würfeln wollen, dann schreiben sie Nein.")

