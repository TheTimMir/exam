from exceptions import *


class Action:
    def __init__(self, name: str, health: int, happiness: int, capital: float):
        self.capital = capital
        self.happiness = happiness
        self.health = health
        self.name = name


class Work(Action):
    def __init__(self, name: str, health: int, happiness: int, capital: float):
        super().__init__(name, health, happiness, capital)


class Rest(Action):
    def __init__(self, name: str, health: int, happiness: int, capital: float):
        super().__init__(name, health, happiness, capital)


class Person:
    def __init__(self, name: str, health: int, happiness: int, capital: float):
        self.capital = capital
        self.happiness = happiness
        self.health = health
        self.name = name

    def change_status(self, dHealth=0, dHappiness=0, dCapital=0.0):
        self.capital += dCapital
        if self.capital < 0:
            raise BankruptException("No money left.")
        self.health += dHealth
        if self.health < 0:
            raise DeathException("No health left.")
        self.happiness += dHappiness
        if self.happiness < 0:
            raise DepressionException("No happiness left.")

    def do(self, action: Action):
        if type(action) == Work:
            if self.happiness > 90:
                self.change_status(0, 0, 0.1 * action.capital)
        elif type(action) == Rest:
            if self.health < 40:
                self.change_status(int(0.2 * action.health), 0, 0)
        self.change_status(action.health, action.happiness, action.capital)

    def __str__(self):
        return f"Name:{self.name}\nHealth:{self.health}\nHappiness:{self.happiness}\nCapital:{self.capital}"


