from random import choice

lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

pulls = []

for i in range(4):
    pull = choice(lotto)
    pulls.append(pull)

print("The winning lottery numbers are:")
print("\t" + str(pulls))






