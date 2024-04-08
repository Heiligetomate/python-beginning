# Schacheröffnungen
print("Guten Tag! Sie Wollen eine Schacheröffnung finden? Dann sind sie hier genau richtig!")
# Abfrage Farbe
farbe = input("Weiß oder Schwarz? 1 für Schwarz und 2 für Weiß. ")
if farbe == "1":
    print("Okay sie wollen eine Eröffnung für Schwarz finden. ")
    # Abfrage Erster Bauer (S)
    Bauer = input(
        "Wollen sie eine Eröffnumg gegen e4 finden, dann drücken sie die 1, wollen sie eine Eröffnung gegen d4 finden, dann drücken sie die 2. Wollen sie eine Eröffnung gegen etwas Anderes finden, dann drücken sie die 3. Wenn sie keine Lust mehr haben, weil sie eine Aufmerksamkeitsspanne einer Fliege haben, dann schreiben sie Fliege.")
    if Bauer == "1":
        print(
            "Okay sie wollen eine Eröffnung gegen e4 finden. Das ist eigentlich der größte Bereich, also werden noch ein paar weitere Fragen kommen.")
        # Abfrage Bekannte Eröffnung?
        Bauer = input(
            "Wollen sie eher eine bekannte Eröffnung spielen (drücken sie die 1), oder eher etwas, was den Gegner verwirren könnte und wenn dein Gegner deine Eröffnung nicht kennt kennt, dann könntest du mit einem großen Vorteil aus der Eröffnung gehen (drücken sie die 2).")

        if Bauer == "1":
            # Abfrage offenes Spiel?
            Spiel = input(
                "Ok jetzt steht noch die Frage offen, ob sie ein offenes Spiel (drücken sie die 1), ein halboffenes Spiel (drücken sie die 2), oder ein geschlossenes Spiel haben wollen (drücken sie die 3).")
            if Spiel == "1":
                print("offene Spiele als Schwarz gegen e4 sind:")
            elif Spiel == "2":
                print("Halboffene Spiele als Schwarz gegen e4 sind:")
            elif Spiel == "3":
                print("Geschlossene Spiele für Schwarz gegen e4 sind:")
            else:
                ("dann halt nicht")
    elif Bauer == "2":
        print("Tja d4 als Schwarz... Da gibts schon ein paar lustige und unlustige Eröffnungen.")
        # Abfrage Bekannt?
        spiel = input(
            "Wollen sie eher eine bekannte Eröffnung spielen (drücken sie die 1), oder eher etwas, was den Gegner verwirren könnte und wenn dein Gegner deine Eröffnung nicht kennt kennt, dann könntest du mit einem großen Vorteil aus der Eröffnung gehen (drücken sie die 2).")
        if spiel == "1":
            print("bekannte Eröffnungen für schwarz gegen d4 sind:")
        elif spiel == "2":
            print("etwas unbekanntere, aber trotzdem gute Eröffnungen als Schwarz gegen d4 sind: ")
    elif Bauer == "3":
        print(
            "Diese Momente, wenn man erwartet, dass Weiß was Normales spielt und dann aufeinmal c4 oder Sf3 kommt... Jaja das ist oll. ")
        # Abfrage gegen welchen Bauern?
        spiel = input(
            "Wenn sie etwas gegen c4 haben wollen, dann drücken sie die 1, wenn sie etwas gegen Sf3 haben wollen, dann drücken sie die 2, wenn sie etwas gegen andere Züge haben wollen, dann drücken sie die 3.")
        if spiel == "1":
            print("Hier sind ein paar Züge gegen c4, die Englische Eröffnung.")
        elif spiel == "2":
            print("Hier sind ein paar Züge gegen den ersten Zug Sf3:")
        else:
            print("So kommen wir hier nicht weiter! Wenn du das Programm nicht nutzen willst, dann lass es doch sein.")
    elif Bauer == "Fliege":
        print("Tja, wusst ichs doch. Vielleich solltest du dir was anderes als Schach suchen.")
    else:
        print("So kommen wir hier nicht weiter! Wenn du das Programm nicht nutzen willst, dann lass es doch sein.")

elif farbe == "2":
    print("Okay sie wollen eine Eröffnumg für Weiß finden.")
    # Welcher Bauer?
    bauer = input("Welcher Zug soll der Erste sein? Drück 1 für e4, 2 für d4, 3 für Sf3 und 4 für andere Eröffnungen.")
    if bauer == "1":
        print(
            "Eine Gute Wahl! Nur leider ist das noch nicht genau genug, da es ganz schön viele Eröffnungen gibt, die mit e4 starten.")
    elif bauer == "2":
        print(
            "d4 ist neben e4 der beliebteste erste Zug als Weiß. Also gibt es auch hier hunderte Variationen, was die Entscheidung nicht leich macht...")
    elif bauer == "3":
        print("Das Sf3 Gebiet ist nicht besonders groß, also wird es nicht besonders kompliziert.")
    elif bauer == "4":
        print(
            "Das Problem bei der ganzen Sache ist, dass jeder Zug den Weiß am anfang machen kann eine Eröffnung ist. Also Wird die Entscheidung auch hier nicht gerade leicht fallen.")
    else:
        print("So kommen wir hier nicht weiter! Wenn du das Programm nicht nutzen willst, dann lass es doch sein.")
else:
    print("So kommen wir hier nicht weiter! Wenn du das Programm nicht nutzen willst, dann lass es doch sein.")