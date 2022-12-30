ask_for_number = "Input a number to check if it is a multiple of 10: "
user_number = int(input(ask_for_number))
if user_number % 10 > 0:
    print(f"{user_number} is NOT multiple of ten.")
elif user_number % 10 == 0:
        print(f"{user_number} is a multiple of ten!")
