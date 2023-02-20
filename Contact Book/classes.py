import re
from tabulate import tabulate


def checkEmailRegEx(text):
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
        else:
            print('Invalid phone number')
            self.phone = ''
        if checkEmailRegEx(email) or email=='':
            self.email = email
        else:
            print('Invalid email')
            self.email = ''
        self.isFavorite = False

    def __str__(self):
        personalData = {
            "Name": self.name,
            "Surname": self.surname,
            "Company": self.company,
            "Phone number": self.phone,
            "Email address": self.email
        }
        return tabulate(personalData.items(), tablefmt="simple_grid")

    def __repr__(self):
        return self.surname
    
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

    def get(self, attribute):
        match attribute:
            case 'name':
                return self.name
            case 'surname':
                return self.surname
            case 'company':
                return self.company
            case 'phone':
                return self.phone
            case 'email':
                return self.email
            case other:
                print('There is no such attribute')
    
    def set(self, attribute, value):
        match attribute:
            case 'name':
                self.name = value
            case 'surname':
                self.surname = value
            case 'company':
                self.company = value
            case 'phone':
                if value.isdigit():
                    self.phone = value
                else: 
                    return False
            case 'email':
                if checkEmailRegEx(value):
                    self.email = value
                else:
                    return False
            case other:
                print('There is no such attribute')
                return False
        return True


class Contacts:

    def __init__(self, givenList=None):
        if givenList is None:
            self.listOfContacts = []
        else:
            self.listOfContacts = givenList.copy()

    def __str__(self):
        if self.listOfContacts:
            theHeader = ['NAME', 'SURNAME', 'COMPANY', 'PHONE NUMBER', 'EMAIL ADDRESS']
            
            listOfFavorites = [prs for prs in self.listOfContacts if prs.isFavorite]
            if listOfFavorites: 
                listOfFavorites = sorted(listOfFavorites, key=lambda x: x.surname)
                listOfFavorites = [prs.getAsList() for prs in listOfFavorites]
            
            listOfItems = [prs for prs in self.listOfContacts if prs.isFavorite == False]
            listOfItems = sorted(listOfItems, key=lambda x: x.surname)
            listOfItems = [prs.getAsList() for prs in listOfItems]
            
            if listOfFavorites:
                display =  'FAVORITES:\n' + tabulate(listOfFavorites, headers=theHeader, showindex=True) + \
                '\n\nOTHER:\n' + tabulate(listOfItems, headers=theHeader, showindex=True)
            else:
                display = tabulate(listOfItems, headers=theHeader, showindex=True)
            return display   
        else:
            return "You don't have any contacts yet."
        
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i >= len(self.listOfContacts):
            raise StopIteration
        value = self.listOfContacts[self.i]
        self.i += 1
        return value

    def search(self, givenContact):
        try:
            position = self.listOfContacts.index(givenContact)
            #print('Found at position: ' + str(position+1) + ' out of ' + str(len(self.listOfContacts)))
            return position
        except ValueError:
            return None
            
    def searchFor(self, searchingBy, searchedValue):
        for contact in self.listOfContacts:
            if contact.get(searchingBy) == searchedValue:
                print('Contact found')
                print(contact)
                return contact
        print('Contact not found')

    def add(self, givenContact):
        if isinstance(givenContact, Contact):
            self.listOfContacts.append(givenContact)
            return True
        else:
            return False

    def pop(self, index = -1):
        self.listOfContacts.pop(index)

    def addAtPosition(self, givenContact, givenIndex):
        self.listOfContacts.insert(givenIndex, givenContact)
