import random

class Wizard:
    def __init__(self):
        self.damage = random.choice(range(2, 5))  # 2, 3, or 4
        self.chance = 20
        self.leak = 10
        self.price = 15
        self.unit_type = "wizard"
    

wizard = Wizard()

print(wizard.damage)
print(wizard.unit_type)