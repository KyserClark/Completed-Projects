from random import choice

lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

pulls = []

my_ticket = [4, 1, 6, 'A']

tries = 0
while pulls != my_ticket:
    pulls = []
    for i in range(4):
        pull = choice(lotto)
        pulls.append(pull)
    tries += 1
    print(f"Try Number {tries}...")
    print(pulls)
    print('\n')

print("\nThe winning lottery numbers are:")
print("\t" + str(pulls))
print(f"\tIt only took {tries} tries!")


