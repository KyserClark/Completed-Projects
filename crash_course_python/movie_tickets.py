ask_for_age = "Welcome to the movie theater! How old are you? "

while True:
    try:
        customer_age = int(input(ask_for_age))
        if customer_age < 3:
            print("\n\tYour ticket is free. Thanks for bringing your baby!")
            break
        elif 3 <= customer_age < 12:
            print("\n\tYour ticket costs $10. Enjoy the movie!")
            break
        elif customer_age >= 12:
            print("\n\tYour ticket costs $12. Enjoy the movie!")
            break

    except ValueError:
        print("\n\tInput not valid. Please enter an integer.")
        continue
