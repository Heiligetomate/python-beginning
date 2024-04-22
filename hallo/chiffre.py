import sys


def chiffre(a):
    text = "EIN TEXT MIT WOERTERN IST EINE SCHRIFTLICHE KOMPOSITION DIE GENAU AUS WOERTERN BESTEHT DIESE ART VON TEXT KANN ZU VERSCHIEDENEN THEMEN VERFASST WERDEN UND DIENT OFT DAZU EINE PRAEZISE UND KOMPAKTE DARSTELLUNG EINES SACHVERHALTS EINER MEINUNG EINER GESCHICHTE ODER EINER ERKLAERUNG ZU LIEFERN DIE HERAUSFORDERUNG BEI DER ERSTELLUNG EINES SOLCHEN TEXTES LIEGT IN DER STRINGENTEN BEGRENZUNG DER WORTANZAHL WAS BEDEUTET DASS JEDER SATZ SORGFÄLTIG KONSTRUIERT SEIN MUSS UM DIE NOTWENDIGEN INFORMATIONEN ZU VERMITTELN OHNE DABEI WICHTIGE DETAILS AUSZULASSEN EIN -WOERTER-TEXT KANN FUER VERSCHIEDENE ZWECKE GENUTZT WERDEN WIE ZUM BEISPIEL FUER KURZE BLOGARTIKEL ZUSAMMENFASSUNGEN VON ARTIKELN PRODUKTBESCHREIBUNGEN WERBETEXTE SOZIALE MEDIENBEITRAEGE ODER ALS UEBUNG IN SCHREIBKURSEN UM KONZISION UND PRAEGNANZ ZU UEBEN TROTZ SEINER KUERZE KANN EIN SOLCHER TEXT EINE KLARE BOTSCHAFT VERMITTELN UND MUSS DABEI DEN GRUNDLEGENDEN ANFORDERUNGEN AN STRUKTUR GRAMMATIK UND STILISTIK GENUEGEN"
    text = text.lower()
    text = text.replace(" ", "")

    text = list(text)
    key_word = input("Welches Key Wort? ")
    key_word = key_word.lower()
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


