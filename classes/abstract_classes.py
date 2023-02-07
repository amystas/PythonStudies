from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print('You drive the car')


class Motorcycle(Vehicle):
    def go(self):
        print('You ride the motorcycle')


