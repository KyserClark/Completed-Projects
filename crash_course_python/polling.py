favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people_to_poll = ['baraka', 'havik', 'jen', 'mavado', 'phil']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll {person.title()}.")
    else:
        print(f"{person.title()} please consider taking our poll.")
