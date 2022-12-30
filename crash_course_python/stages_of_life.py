person_age = 65

if person_age < 2:
    person = 'a Baby'

elif person_age < 4:
    person = 'a Toddler'

elif person_age < 13:
    person = 'a Kid'

elif person_age < 20:
    person = 'a Teenager'

elif person_age < 65:
    person = 'an Adult'

elif person_age >= 65:
    person = 'an Elder'

print(f'This person is {person}.')