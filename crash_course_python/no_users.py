#usernames = ['admin', 'kyser', 'hanzo', 'bill', 'frank']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print((f'Welcome {username}, ') + 
                 ('would you like to see website statistics?'))
        else:
            print(f'Welcome {username}, thank you for logging in.')
else:
    print('No one is logged in at this time.')