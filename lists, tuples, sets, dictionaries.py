# list
def lists():
    food = ['pizza', 'hot dog', 'pasta', 'pudding']

    food[0] = 'sushi'

    food.pop()
    food.append('ice cream')
    food.remove('hot dog')
    food.insert(2, 'cake')
    food.sort()

    for x in food:
        print(x, end='\t')
    print()
    food.clear()

    # 2d lists = multidimensional list
    drinks = ['coffee', 'soda', 'tea']
    dessert = ['cake', 'cookies']
    dinner = ['pizza', 'pasta', 'steak']
    meal = [drinks, dinner, dessert]
    print(meal)
    print(meal[0][2])


# tuple = collection which is ordered and unchangeable, allows duplicates, used to group together related data
def tuples():
    student = ('Rob', 20, 'male')
    print(student.count('Rob'))
    print(student.index('male'))

    for x in student:
        print(x, end='\t')
    print()

    if 'Rob' in student:
        print('Rob is here')


# set = unordered, unindexed collection, no duplicate values
def sets():
    utensils = {'fork', 'knife', 'spoon'}
    utensils.add('napkin')
    # utensils.remove('knife')

    dishes = {'bowl', 'plate', 'cup', 'knife'}
    # utensils.update(dishes)  # adds elements from dishes to utensils

    print(utensils.difference(dishes))
    print(utensils.intersection(dishes))

    dinner_table = utensils.union(dishes)
    for x in dinner_table:
        print(x)


# dictionary = changeable, unordered collection of unique key:value pairs
def dictionaries():
    capitals = {'USA': 'Washington DC',
                'India': 'New Delhi',
                'Russia': 'Moscow'}
    capitals.update({'Germany': 'Berlin'})
    capitals.update({'Russia': 'St Petersburg'})
    capitals.pop('India')

    print(capitals['USA'])
    print(capitals.get('Germany'))
    print(capitals.keys())
    print(capitals.values())
    print(capitals.items())
    print(capitals)

    for key, value in capitals.items():
        print(key, value)

    capitals.clear()


def indexing():
    name = 'amy Stas'
    if name[0].islower():
        name = name.title()
        # name = name[0].upper() + name[1:]
    print(name)

    firstname = name[:3].upper()
    lastname = name[4:].lower()
    print(firstname, lastname)

    last_character = name[-1]
    print(last_character)


# lists()
# tuples()
# sets()
# dictionaries()
indexing()
