from classes import *
import inheritance
import multilevel_inheritance
import multiple_inheritance
import method_chaining
import super_function
import abstract_classes

car1 = Car('Chevy', 'Corvette', 2021, 'blue')
car2 = Car('Ford', 'Mustang', 2022, 'red')
print(car1.make, car1.model, car1.year, car1.color)

car1.wheels = 2
print(car1.wheels)
print(Car.wheels)

print('\nINHERITANCE')
rabbit = inheritance.Rabbit()
fish = inheritance.Fish()
hawk = inheritance.Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

print('\nMULTILEVEL INHERITANCE')
dog = multilevel_inheritance.Dog()
print(dog.alive)
dog.eat()
dog.bark()

print('\nMULTIPLE INHERITANCE')
rabbit = multiple_inheritance.Rabbit()
hawk = multiple_inheritance.Hawk()
fish = multiple_inheritance.Fish()
rabbit.flee()
fish.hunt()
hawk.hunt()
print('\nMETHOD CHAINING')
car = method_chaining.Car()
car.turn_on().drive().brake().turn_off()

print('\nSUPER FUNCTION')
cube = super_function.Cube(3, 3, 3)
square = super_function.Square(3, 3)
print(cube.volume())
print(square.area())

print('\nABSTRACT CLASSES')
car = abstract_classes.Car()
motorcycle = abstract_classes.Motorcycle()
car.go()
motorcycle.go()
