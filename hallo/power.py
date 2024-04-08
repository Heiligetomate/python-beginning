def power():
    while True:
        base = input("Enter the base ")
        exponent = input("Enter the exponent ")
        try:
            base = float(base)
            exponent = float(exponent)
        except ValueError:
            print("Invalid input")
            continue
        result = base ** exponent
        print(result)
power()