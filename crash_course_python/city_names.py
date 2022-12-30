def city_country(city_name, country_name):
    return(f'"{city_name.title()}, {country_name.title()}"')

city_1 = city_country('seoul', 'south korea')
city_2 = city_country('new york', 'united states')
city_3 = city_country('tokyo', 'japan')

print(city_1)
print(city_2)
print(city_3)
