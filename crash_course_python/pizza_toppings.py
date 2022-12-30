ask_for_toppings = "What would you like on your pizza? : "
ask_for_toppings += "\n\tType 'quit' to stop adding toppings."
while True:
    topping_choice = input(ask_for_toppings)
    if topping_choice != 'quit':
        print(f"\nAdding {topping_choice} to your pizza...\n")
    elif topping_choice == 'quit':
        print("\nThank you for your order. Please wait while we get that "
              "pizza ready for you.")
        break
