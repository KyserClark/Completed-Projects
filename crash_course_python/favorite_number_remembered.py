import json

try:
    with open('favorite_number.json') as file:
        favorite_number = json.load(file)

except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as file:
        json.dump(favorite_number, file)

else:
    print(f"Your favorite number is {favorite_number}")