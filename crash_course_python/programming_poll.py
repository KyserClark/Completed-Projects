with open('programming_poll.txt', 'a') as poll:
    response = input("Why do you like programming? ")
    poll.write(response + '\n')