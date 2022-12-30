ask_for_age = "Welcome to the movie theater! How old are you? "
prompt = True
loop_count = 0
while prompt and loop_count <= 6:
    loop_count += 1
    try:
        if loop_count >= 6:
            input("\nIf you can't tell us your age, you need to leave."
                  "\n\tPress enter to leave:")
            break

        customer_age = input(ask_for_age)
        if customer_age == 'quit':
            break
        if int(customer_age) < 3:
            print("\n\tYour ticket is free. Thanks for bringing your baby!")
            prompt = False
        elif 3 <= int(customer_age) < 12:
            print("\n\tYour ticket costs $10. Enjoy the movie!")
            prompt = False
        elif int(customer_age) >= 12:
            print("\n\tYour ticket costs $12. Enjoy the movie!")
            prompt = False

    except ValueError:
        if loop_count < 5:
            print("\n\tInput not valid. Please enter an integer.")
            continue


