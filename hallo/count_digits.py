digits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = ("Weit hinten, hinter den Wortbergen, fern der Laender Vokalien und Konsonantien leben die Blindtexte. "
        "Abgeschieden wohnen sie in Buchstabhausen an der Kueste des Semantik, eines grossen Sprachozeans")

for i in range(len(digits)):
    count = text.count(digits[i])
    print(f"Buchtabe: {digits[i]}, Haefigkeit: {count}")
