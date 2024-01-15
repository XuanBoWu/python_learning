from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))
    
    def multiple_roll_die(self, count):
        while count > 0:
            self.roll_die()
            count -= 1


die_6 = Die()
print("sides is 6:")
die_6.multiple_roll_die(10)

die_10 = Die(10)
print("sides is 10:")
die_10.multiple_roll_die(10)

die_20 = Die(20)
print("sides is 20:")
die_20.multiple_roll_die(10)


