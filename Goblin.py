from random import choice
class Goblin:    
    def __init__(self):
        self.damage = choice([2, 3])
        self.loot = choice([1, 1.1, 1.2, 1.3, 1.4, 1.5])
