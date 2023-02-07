# string methods
def stringMethods():
    name = 'Amy'

    print(len(name))

    print(name.find('A'))

    print(name.capitalize())

    print(name.upper())

    print(name.lower())

    print(name.isdigit())

    print(name.isalpha())

    print(name.count('y'))

    print(name.replace('y', 'i'))

    # prints name three times
    print(name * 3)

    print('  hello  '.strip())  # removes spaces at the beginning and the end
    print('##hello##'.strip('#'))  # removes given character at the beginning and the end
    print('  hello  '.rstrip())  # removes only right whitespaces

    #in Python 3.9
    #s = 'Amy: 10'.removeprefix('Amy: ')
    #print(s)

    text = 'string methods in Python'
    print(text.replace(' ', '-'))

    s = 'Python is awesome!'
    parts = s.partition('is') #return a turple
    print(parts)




# type casting = convert the data type of a value to another data type
def typeCasting():
    x = 1  # int
    y = 2.0  # float
    z = '3'  # str

    x = float(x)
    y = str(y)
    z = int(z)

    print(x, y, z * 3)


# user input
def userInput():
    name = input('What is your name?: ')  # without casting - always str type
    age = int(input('How old are you?: '))
    height = float(input('How tall are you?: '))

    print('Hello ' + name)
    print('You are ' + str(age) + ' years old')
    print('You are ' + str(height) + ' feet tall')


# math functions
def mathFunctions():
    import math
    x, y, z = 1, 2, 3
    pi = -3.14
    print(round(pi))
    print(math.ceil(pi))  # rounding the number up to the nearest whole integer
    print(math.floor(pi))
    print(abs(pi))  # absolute value
    print(pow(pi, 2))
    print(math.sqrt(420))
    print(max(x, y, z))


# slicing = create substring by extracting elements from another string
# indexing[]  slice()    [start:stop:step]
def stringSlicing():
    name = 'AmyStas'
    # start - inclusive, stop - exclusive
    firstName = name[:3]
    lastName = name[3:]

    print(firstName)
    print(lastName)
    # step = how much we're increasing the index, default: 1
    text = name[::2]
    print(text)

    # reversing
    reversedName = name[::-1]
    print(reversedName)

    # slice()
    website1 = 'http://google.com'
    website2 = 'http://wikipedia.com'
    slc = slice(7, -4)
    print(website1[slc])
    print(website2[slc])


# If Statements
def ifStatements():
    age = int(input('How old are you?: '))
    if age == 100:
        print('You are a century old!')
    elif age >= 18:
        print('You are an adult!')
    elif age < 0:
        print("You haven't been born yet!")
    else:
        print('You are a child!')


# logical operators: and, or
def logicalOperators():
    temp = int(input('What is the temperature outside?: '))
    if not (temp >= 0 and temp <= 30):
        print('The temperature is bad today!\nStay inside!')
    elif not (temp < 0 or temp > 30):
        print('The temperature is good today!\nGo outside!')


# while loop
def whileLoop():
    name = None
    while not name:
        name = input('Enter name: ')
    print('Hello ' + name)


# for loop = a statement that will execute it's block of code a limited amount of times
# while loop - unlimited
# for loop - limited
def forLoop():
    for i in range(10):
        print(i + 1)
    for i in range(50, 100 + 1, 5):
        print(i)
    for i in "Amy":
        print(i)

    import time
    for seconds in range(10, 0, -1):
        print(seconds)
        time.sleep(1)
    print('Happy New Year!')


# nested loops
def nestedLoop():
    rows = int(input('How many rows?: '))
    columns = int(input('How many columns?: '))
    symbol = input('Enter a symbol to use: ')
    for i in range(rows):
        for j in range(columns):
            print(symbol, end='')
        print()


# loop control statements = change a loop execution from its normal sequence
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder
def loopControlStatements():
    while True:
        name = input('Enter your name: ')
        if name != '':
            break

    phoneNumber = '123-456-789'
    for i in phoneNumber:
        if i == '-':
            continue
        print(i, end='')
    print()

    for i in range(1, 20 + 1):
        if i == 13:
            pass
        else:
            print(i)


stringMethods()
# typeCasting()
# userInput()
# mathFunctions()
# stringSlicing()
# ifStatements()
# logicalOperators()
# whileLoop()
# forLoop()
# nestedLoop()
#loopControlStatements()
