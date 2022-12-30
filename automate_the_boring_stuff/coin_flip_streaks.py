import random

numberOfStreaks = 0
coin = ['heads', 'tails']
results = []

print('Flipping coin 10,000 times...\n')

for experimentNumber in range(10_000):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    this_flip = (random.choice(coin))
    print(this_flip)
    results.append(this_flip)

    # Code that checks if there is a streak of 6 heads or tails in a row.

    if results[-6:] == ['tails'] * 6 or results[-6:] == ['heads'] * 6:
        numberOfStreaks += 1

percentage = numberOfStreaks / 100
print(f'\nNumber of six in a row streaks that happened: {numberOfStreaks}\n')
print(f'Chance of having six in a row: {percentage}')
