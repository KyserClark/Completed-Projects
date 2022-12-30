current_users = ['admin', 'kung_lao', 'scorpion', 'sub-zero', 'kitana']

new_users = ['Sonya', 'Jade', 'Sub-Zero', 'Raiden', 'Kitana']

for user in new_users:
    
    if user.lower() in current_users:
        print((f'Sorry, "{user.lower()}" is taken ') + 
              ('please choose a different username.'))

    if user.lower() not in current_users:
        print(f'"{user.lower()}" is an available username.')