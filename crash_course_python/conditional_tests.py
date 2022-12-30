kyser = 'cool'
print("Is kyser == 'cool'? Of course I am!")
print(kyser == 'cool')

print("\nIs kyser == 'not_cool'? Nah!")
print(kyser == 'not_cool')
print('\n')
male_mk_ninjas = [
    'Scorpion', 'Sub-Zero', 'Reptile', 'Noob-Saibot', 'Smoke', 'Ermac', 'Rain',
    'Chameleon', 'Tremor',
    ]

female_mk_ninjas = [
    'Kitana', 'Mileena', 'Jade', 'Khameleon', 'Tanya', 'Frost', 'Skarlet' 
    ]

shokan = ['Goro', 'Kintaro', 'Sheeva']

print('These should be true\n')
print('Goro' in shokan)
print('Reptile' in male_mk_ninjas)
print('Jade' in female_mk_ninjas)
print('Sub-Zero' in male_mk_ninjas)
print('Smoke' not in female_mk_ninjas)

print('\nThese should be false\n')
print('Scorpion' in shokan)
print('Jade' in male_mk_ninjas)
print('Sheeva' in female_mk_ninjas)
print('Kintaro' in male_mk_ninjas)
print('Skarlet' not in female_mk_ninjas)