name = ''
time = ''
while True:
    with open('guest_book.txt', 'a') as guest_book:
        name = input("What is your name?\n\t q to quit: \n")
        time = input("What time is it?\n\t q to quit: \n")
        if name != 'q' and time != 'q':
            guest_book.write(f"{name} was here at {time}.\n")
            print(f"Thank you {name} have a good time!\n")

    if name == 'q' or time == 'q':
        break
