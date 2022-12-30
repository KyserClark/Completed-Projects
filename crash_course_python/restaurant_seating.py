ask_group_size = "How many people are in your dinner party?: "
group_size = int(input(ask_group_size))
if group_size > 8:
    print("Sorry, but you will have to wait for a table.")
elif group_size <= 8:
    print("We have a table ready for you, right this way.")

