mortal_kombat_ninjas = ['Scorpion', 'Sub-Zero', 'Reptile', 'Noob-Saibot', 'Smoke', 'Ermac', 'Rain', 'Chameleon', 'Tremor']
print(mortal_kombat_ninjas)
print(mortal_kombat_ninjas[0])
print(mortal_kombat_ninjas[1].title())
print(mortal_kombat_ninjas[-1])
print(f"My favorite Mortal Kombat Character is {mortal_kombat_ninjas[0]}")
mortal_kombat_ninjas[1] = 'Cyber Sub-Zero'
print(mortal_kombat_ninjas)
mortal_kombat_ninjas.append('Kitana')
print(mortal_kombat_ninjas)
mortal_kombat_ninjas.insert(-1, 'Mileena')
print(mortal_kombat_ninjas)
del mortal_kombat_ninjas[-1]
print(mortal_kombat_ninjas)
removed_character = 'Mileena'
mortal_kombat_ninjas.remove(removed_character)
print(f'the removed character was {removed_character}')
print(mortal_kombat_ninjas)
popped_character = mortal_kombat_ninjas.pop()
print(f'{popped_character} has been removed from the list')
print(mortal_kombat_ninjas)
mortal_kombat_ninjas.sort()
print(mortal_kombat_ninjas)
mortal_kombat_ninjas.sort(reverse=True)
print(mortal_kombat_ninjas)
mortal_kombat_ninjas.reverse()
print(mortal_kombat_ninjas)
print(len(mortal_kombat_ninjas))



