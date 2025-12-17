import random 

class Orc: 
    def __init__ (self): 
        self.damage = random.randint(3, 5) 
        self.loot = round(random.choice(2, 2.5), 1)