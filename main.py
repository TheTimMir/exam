from exceptions import *


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

    def __str__(self):
        return f"Name:{self.name}\nHealth:{self.health}\nHappiness:{self.happiness}\nCapital:{self.capital}"


class Acton:
    def __init__(self, name: str, health: int, happiness: int, capital: float):
        self.capital = capital
        self.happiness = happiness
        self.health = health
        self.name = name

    def __str__(self):
        return f"Name:{self.name}\nHealth:{self.health}\nHappiness:{self.happiness}\nCapital:{self.capital}"
