import json

favorite_number = input("What is your favorite number? ")

filename = 'favorite_number.json'

with open(filename, 'w') as file:
    json.dump(favorite_number, file)