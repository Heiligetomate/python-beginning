
test_file = open("testtext.txt", "r+")
def delete_from_file(compare_to):
    with open("testtext.txt", "r+", encoding="utf-8") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i.strip("\n") != compare_to:
                f.write(i)
        f.truncate()



#Abfrage, was der Benutzer machen möchte
what_does_the_user_want_to_do = input("Hallo was wollen sie mit ihrer Einkaufsliste machen? 1 für Elemente hinzufügen, 2 zum Entfernen von Elementen, 3 um die Liste aufzurufen, 4 um die Liste zu löschen und 5 um das Programm zu verlassen. ")

if what_does_the_user_want_to_do == "1":
    user_input = input("Was wollen sie ihrer Einkaufsliste hinzufügen? ")
    test_file.write(user_input + "\n" )


elif what_does_the_user_want_to_do == "2":
    delete_from_file(input("Was wollen sie löschen? "))


elif what_does_the_user_want_to_do == "3":
    for lines in test_file:
        print(lines)


test_file.close()







#delete_from_file("lalala")
