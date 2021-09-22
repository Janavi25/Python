# write a program to roll a dice
import random


class dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice_roll = dice()
print(dice_roll.roll())
