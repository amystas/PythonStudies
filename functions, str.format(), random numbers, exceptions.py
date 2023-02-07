def hello(first_name, last_name, age):
    print('Hello ' + first_name + ' ' + last_name)
    print('You are ' + str(age) + ' years old')
    print('Have a nice day!')


def multiply(n1, n2):
    return n1 * n2


x = multiply(2, 8)
print(x)


# keyword arguments
def greeting(first, last, age):
    print('Hello ' + first + ' ' + last + ', you are ' + str(age) + ' years old')


greeting(last='Stas', first='Amy', age=17)


# *args = parameter that will pack all arguments into a tuple,
#         useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    args = list(args)
    args[2] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7))


# **kwargs = parameter that will pack all arguments into a dictionary,
#            useful so that a function can accept a varying amount of keyword arguments

def hi(**kwargs):
    # print('Hello ' + kwargs['first'] + ' ' + kwargs['last'])
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')
    print()


hi(title="Ms", first='Amy', last='Stas')

# str.format()
animal = 'cow'
item = 'moon'
# print('The ' + animal + ' jumped over the ' + item)
print('The {} jumped over the {}'.format(animal, item))
print('The {1} jumped over the {0}'.format(item, animal))  # positional argument
print('The {animal} jumped over the {item}'.format(item='moon', animal='cow'))  # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))
# padding
print("Hello my name is {:10}. Nice to meet you".format('Amy'))  # right side
print("Hello my name is {:>10}. Nice to meet you".format('Amy'))  # left side
print("Hello my name is {:^10}. Nice to meet you".format('Amy'))  # centre

print('The number is {:.2f}'.format(3.14159))  # limits to 2 digits after dot (also rounds the number)
print('The number is {:,}'.format(1000))  # adds comma at the thousands place
print('The number is {:b}'.format(1000))  # displays as binary
print('The number is {:o}'.format(1000))  # displays as octal number
print('The number is {:X}'.format(1000))  # displays as hexadecimal
print('The number is {:e}'.format(1000))  # scientific notation

# random numbers
import random

x = random.randint(1, 10)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)
print(x, y, z)

# exception handling
keepTrying = True
while keepTrying:
    try:
        numerator = int(input('Enter a number to divide: '))
        denominator = int(input('Enter a number to divide by: '))
        result = numerator / denominator
    except ZeroDivisionError as e:
        print('cannot divide by zero')
        print('(' + str(e) + ')')
    except ValueError as e:
        print('enter only numbers')
        print('(' + str(e) + ')')
    except Exception as e:
        print('something went wrong')
        print('(' + str(e) + ')')
    else:
        print(result)
        keepTrying = False
    finally:
        print('always executes')
