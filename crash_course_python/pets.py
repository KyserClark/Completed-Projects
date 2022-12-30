fluffy = {
    'owner': 'Bill',
    'type': 'cat',
    'gender': 'female',
    'color': 'white',
    }

tank = {
    'owner': 'Sally',
    'type': 'dog',
    'gender': 'male',
    'color': 'brown',
    }

spark = {
    'owner': 'Jacob',
    'type': 'bird',
    'gender': 'male',
    'color': 'blue',
    }

pets = [fluffy, tank, spark, ]

for pet in pets:
    print(f"{pet['owner'].title()}'s {pet['type']} is a {pet['color']} "
          f"{pet['gender']}.")
