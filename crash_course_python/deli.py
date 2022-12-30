sandwich_orders = ['Burger', 'Club', 'Chicken', 'Tuna']
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        order_up = sandwich_orders.pop(0)
        if order_up != 'Burger':
            print(f"Your {order_up} sandwich is finished.")
        elif order_up == 'Burger':
            print(f"Your {order_up} is finished.")

        finished_sandwiches.append(order_up)

if finished_sandwiches:
    print("\nYour order is ready!")
    for sandwich in finished_sandwiches:
        if sandwich != 'Burger':
            print("\t" + sandwich + " sandwich")
        elif sandwich == 'Burger':
            print("\t" + sandwich)
    print("\nPlease pay the cashier :)")

