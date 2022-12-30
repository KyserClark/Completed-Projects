rivers = {
    'Amazon': 'Brazil, Peru, and Columbia',
    'Nile': 'Egypt, and Sudan',
    'Ganges': 'India, and Bangladesh'
    }

for key, value in rivers.items():
    print(f"The {key} river flows through {value}.")

print('\nRIVERS:')
for key in rivers.keys():
    print('\t' + key)

print('\nCOUNTRIES:')
for value in rivers.values():
    countries = (value.split())
    countries.remove('and')
    for country in countries:
        print('\t' + country.strip(','))