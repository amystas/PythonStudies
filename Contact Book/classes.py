import re
from tabulate import tabulate


def changeEmailRegEx(text):
    emailRegex = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    return re.fullmatch(emailRegex, text)


class Contact:
    def __init__(self, name='', surname='', company='', phone='', email=''):
        if name.isalpha() and surname.isalpha():
            self.name = name
            self.surname = surname
            self.company = company
        if phone.isdigit() or phone == '':
            self.phone = phone
        if changeEmailRegEx(email):
            self.email = email

    def __str__(self):
        personalData = {
            "Name": self.name,
            "Surname": self.surname,
            "Company": self.company,
            "Phone number": self.phone,
            "Email address": self.email
        }
        return tabulate(personalData.items(), tablefmt="simple_grid")

    def setFromList(self, givenList):
        if len(givenList) > 5:
            print('Invalid list')
        elif len(givenList) < 5:
            blankFields = 5 - len(givenList)
            fillingList = ['' for i in range(blankFields)]
            givenList.extend(fillingList)

        self.name = givenList[0]
        self.surname = givenList[1]
        self.company = givenList[2]
        self.phone = givenList[3]
        self.email = givenList[4]

    def getAsList(self):
        return [self.name, self.surname, self.company, self.phone, self.email]


class Contacts:

    def __init__(self, givenList=None):
        if givenList is None:
            self.listOfContacts = []
        else:
            self.listOfContacts = givenList.copy()

    def __str__(self):
        if self.listOfContacts:
            theHeader = ['NAME', 'SURNAME', 'COMPANY', 'PHONE NUMBER', 'EMAIL ADDRESS']
            listOfItems = [prs.getAsList() for prs in self.listOfContacts]
            return tabulate(listOfItems, headers=theHeader, showindex=True)
        else:
            return "You don't have any contacts yet."

    def searchFor(self, givenContact):
        try:
            position = self.listOfContacts.index(givenContact) + 1
            print('Found at position: ' + str(position) + ' out of ' + str(len(self.listOfContacts)))
            print(givenContact)
        except ValueError:
            print('Contact not found')

    def add(self, givenContact):
        if isinstance(givenContact, Contact):
            self.listOfContacts.append(givenContact)

    def pop(self):
        self.listOfContacts.pop()

    def addAtPosition(self, givenContact, givenIndex):
        self.listOfContacts.insert(givenIndex, givenContact)
