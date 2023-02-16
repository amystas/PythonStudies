import os
from classes import Contact, Contacts

CONTACTS = Contacts()

def menu():
    print('\nWelcome to Contact Book! Choose an action:')
    print('1) Show contacts')
    print('2) Add contact')
    print('3) Search for a contact')
    print('4) Load contacts from file')
    print('5) Save as file')
    print('6) Exit')
    choice = int(input())
    return choice


def loadFromFile():
    path = input('Enter the path: ')
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        print('File not found')
        return
    addedContacts = 0
    for line in file:
        new = Contact()
        new.setFromList(line.split())
        if CONTACTS.add(new) == False:
            print('File error. Have not added the contact')
        else:
            addedContacts+=1
    print('Added ' + str(addedContacts) + ' contacts!')


def enterContactData():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    company = input('Enter company: ')
    phone = input('Enter phone number: ')
    email = input('Enter email adress: ')
    new = Contact(name, surname, company, phone, email)
    if CONTACTS.add(new):
        print('Contact added!')


def searchForContact():
    searchingBy = input('What do you want to search by?: ').lower()
    searchedValue = input('Enter value: ')
    CONTACTS.searchFor(searchingBy, searchedValue)
  
  
def saveAsFile():
    fileName = input("Type file's name: ") + '.txt'
    try:
        file = open(fileName, 'x')
    except FileExistsError:
        ans = input("File already exists. Do you want to override it? [y/n] ")
        if ans == 'n':
            return
    file = open(fileName, 'w')
    data = ''
    for c in CONTACTS:
        data += ' '.join(c.getAsList()) + '\n'
    file.write(data)
    

action = menu()
while action != 6:
    match action:
        case 1:
            print(CONTACTS)
        case 2:
            enterContactData()
        case 3:
            searchForContact()
        case 4:
            loadFromFile()
        case 5:
            saveAsFile()
    action = menu()