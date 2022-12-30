cities = {
    'Seoul': {
        'population': '9.776 million',
        'country': 'South Korea'
    },
    'Tokyo': {
        'population': '13.96 million',
        'country': 'Japan'
    },
    'New York': {
        'population': '8.4 million',
        'country': 'New York USA'
    },
    'Columbus': {
        'population': '878,553',
        'country': 'Ohio USA'
    },
}

for city, city_info in cities.items():
    print(f"{city} is located in {city_info['country']} and has "
          f"a population of {city_info['population']}.")
