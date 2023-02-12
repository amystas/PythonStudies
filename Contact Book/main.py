import os
from classes import Contact, Contacts

CONTACTS = Contacts()

def loadFromFile():
    path = input('Enter the path: ')
    file = open(path, 'r')
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

def menu():
    print('\nWelcome to Contact Book! Choose an action:')
    print('1) Show contacts')
    print('2) Add contact')
    print('3) Search for a contact')
    print('4) Load contacts from file')
    print('5) Exit')
    choice = int(input())
    return choice

def searchForContact():
    searchingBy = input('What do you want to search by?: ').lower()
    searchedValue = input('Enter value: ')
    CONTACTS.searchFor(searchingBy, searchedValue)
    

action = menu()
while action != 5:
    match action:
        case 1:
            print(CONTACTS)
        case 2:
            enterContactData()
        case 3:
            searchForContact()
        case 4:
            loadFromFile()
    action = menu()