from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self, rolls):
        rolls = [0 for i in range(rolls)]
        for roll in rolls:
            result = str(randint(1, self.sides))
            print('\t' + result)
        print('\n')

six_side = Dice(6)
ten_side = Dice(10)
twenty_side = Dice(20)

print('Roll Six-Sided Die 10 times:')
six_side.roll_dice(10)
print('Roll Ten-Sided Die 10 times:')
ten_side.roll_dice(10)
print('Roll Twenty-Sided Die 10 times:')
twenty_side.roll_dice(10)
