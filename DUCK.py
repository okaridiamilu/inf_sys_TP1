from abc import ABC, abstractmethod

class flyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class canFly():
    def fly(self):
        print("I can fly")

class canNotFly():
    def fly(self):
        print("I can't fly")

class Duck(ABC):
    def __init__(self, fly_behavior: flyBehavior):
        self.__fly_behavior = fly_behavior

    def fly(self):
        self.__fly_behavior.fly()

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck):
    def __init__(self, fly_behavior: flyBehavior):
        self.__fly_behavior = fly_behavior
    
    def quack(self):
            print("Quack")

    def display(self):
        print("I'm a real Mallard duck")

class RedheadDuck(Duck):

    def __init__(self, fly_behavior: flyBehavior):
        self.__fly_behavior = fly_behavior

    def quack(self):
        print("Quack")

    def fly(self):
        self.__fly_behavior.fly()

    def display(self):
        print("I'm a real Redhead duck")

class RubberDuck(Duck):

    def __init__(self, fly_behavior: flyBehavior):
        self.__fly_behavior = fly_behavior

    def quack(self):
        print("Squeak")

    def fly(self):
        print("I can't fly")

    def display(self):
        print("I'm a rubber duck")

