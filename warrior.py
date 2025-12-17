from random import choice
class Warrior:    
    def __init__(self):
        self.damage = choice([3, 4, 5])
        self.luck = 5
        self.escape = 3
        self.price = 10
        self.unit_type = "warrior"
