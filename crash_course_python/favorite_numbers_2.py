favorite_numbers = {
    'Ron': [3, 69, 0, ],
    'Janet': [58, 17, 32],
    'Kim': [24, 23, 99],
    }

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
    print('\n')
