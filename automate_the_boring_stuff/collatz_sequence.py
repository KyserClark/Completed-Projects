def collatz(number):
    if number % 2 == 0:
        output = (number // 2)

    else:
        output = 3 * number + 1

    print(output)

    if output != 1:
        collatz(output)


while True:
    try:
        user_number = int(input('Enter Number: '))
        break

    except:
        print('Input must be an integer')

collatz(user_number)
