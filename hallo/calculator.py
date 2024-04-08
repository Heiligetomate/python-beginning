def calculator():
    print("Welcome to the calculator")
    while True:
        input_str = input("What would you like to? 1 for division, 2 for multiplication, 3 for addition, 4 for subtraction, and 5 for end this programm. ")
        if input_str == "1":
            a = input("Which dividend?: ")
            b = input("Which divisor? : ")
            print(float(a) / int(b))
        elif input_str == "2":
            a = input("Which faktor 1?: ")
            b = input("Which faktor 2?: ")
            result = float(a) / float(b)
            print(f'The result is {result}')
        elif input_str == "3":
            a = input("Which summand 1?: ")
            b = input("Which summand 2?: ")
            result = float(a) + float(b)
            print(f'The result is {result}')
        elif input_str == "4":
            a = input("Which minuend?   : ")
            b = input("Which subtrahend?: ")
            result = float(a) - float(b)
            print(f'The result is {result}')
        elif input_str == "5":
            break
        else:
            print("Invalid! You have to write a number")




