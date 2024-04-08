import random as r

from class_products import Item

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Glass", 30, 12)

item4 = Item("Wasabinuese", 2, 1000)






while True:
    print("Here are all the products: ")
    print(f'1: {item1.name} \n2: {item2.name} \n3: {item3.name} \n4: {item4.name}')
    user_input = input("If u want to know the price of one of these, tipe in the right number. Press 0 to leave the program. \n")
    if user_input == "1":
        print(f"The price of {item1.name} is {item1.price}.")
    elif user_input == "2":
        print(f"The price of {item2.name} is {item2.price}.")
    elif user_input == "3":
        print(f"The price of {item3.name} is: {item3.price}.")
    elif user_input == "4":
        print(f"The price of {item4.name} is {item4.price}.")
    elif user_input == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid")

#print(item2.calculate_total_price(item1.price, item1.quantity))
