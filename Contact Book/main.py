from classes import Contact, Contacts

CONTACTS = Contacts()

def enterContactData():
    pass

def menu():
    print('\nWelcome to Contact Book! Choose an action:')
    print('1) Show contacts')
    print('2) Add contact')
    print('3) Search for a contact')
    print('4) Exit')
    choice = int(input())
    return choice

action = menu()
while action != 4:
    match action:
        case 1:
            print(CONTACTS)
        case 2:
            enterContactData()
        case 4:
            break
    action = menu()