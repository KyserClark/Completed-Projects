favorite_places = {
    'Ron': ['Paris', 'Seoul', 'Tokyo', ],
    'Janet': ['Las Vegas', 'Sydney', 'London', ],
    'Kim': ['New York', 'Moscow', ]
    }

for person, places in favorite_places.items():
    print(f"{person}'s favorite cities are:")
    for place in places:
        print('\t' + (place))
    print('\n')
