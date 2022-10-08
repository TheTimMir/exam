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


def testing():
    create_video = Action("Create video", -3, 5, 1000)
    lift = Work("Lift boxes", 1, -5, 100)
    workout = Rest("Do a workout", 10, 1, -150)

    rich_man = Person("Travis", 34, 87, 1000000.0)
    reg_man = Person("Igor", 70, 68, 100000.0)
    poor_man = Person("Andrew", 32, 5, 100.0)

    rich_man.do(create_video)  # does smth middle
    print(f"{rich_man}\n")  # returns rich man's status

    reg_man.do(workout)  # rests by doing a workout
    print(f"{reg_man}\n")  # returns regular man's status

    poor_man.do(lift)  # works by lifting boxes
    print(f"{poor_man}\n")  # returns poor man's status

    reg_man.change_status(0, 0, -1000)  # you can manually change stats for, per example, fines
    print(f"{reg_man}\n")

testing()
