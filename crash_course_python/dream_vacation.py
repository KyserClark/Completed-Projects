responses = {}

polling_active = True

while polling_active:

    name = input("What is your name? \n")
    response = input("What is your dream vacation location?\n")
    responses[name] = response
    repeat = input("Is there another person who wants to respond "
                   "y/n\n").lower()

    if repeat == 'n' or repeat == 'no':
        polling_active = False

print("Poll Results: ")
for name, response in responses.items():
    print(f"\t{name.title()} would like to visit {response.title()}.")

