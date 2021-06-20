import random
import time

crit_dmg = random.randint(1, 6)


class Boss:
    def __init__(self, h, d):
        self.health = h
        self.damage = d

    def hit(self, c_dmg):
        dmg = self.damage
        if c_dmg >= 3:
            dmg = self.damage + 4
        else:
            dmg = dmg

        player.health -= dmg

    def defend(self):


player = Boss(100, 10)
milgurd = Boss(500, 5)
print("Welcome to JakeJack pet simulator! Press O to continue!")
time.sleep(1)



# this is super far from done, I still need to add defend and heal stages + a bunch of other stuff, this is def a project i want to continue 
