while True:
    print("please enter two numbers to add them together:")
    number_1 = input("Enter 1st Number: ")
    number_2 = input("Enter 2nd Number: ")

    try:
        result = int(number_1) + int(number_2)
    except:
        print("You need to enter integers for both numbers")
    else: 
        print(f"The result is {result}.") 
        break
        