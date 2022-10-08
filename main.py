class Person:
    def __init__(self, name: str, health: int, happiness: int, capital: float):
        self.capital = capital
        self.happiness = happiness
        self.health = health
        self.name = name

    def change_status(self, dHealth=0, dHappiness=0, dCapital=0.0):
        self.capital += dCapital
        if self.capital < 0:
            pass
        self.health += dHealth
        if self.health < 0:
            pass
        self.happiness += dHappiness
        if self.happiness < 0:
            pass