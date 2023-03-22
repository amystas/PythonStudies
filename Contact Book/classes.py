import re
from tabulate import tabulate


def checkEmailRegEx(text):
    emailRegex = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    return re.fullmatch(emailRegex, text)


class Contact:
    def __init__(self, name='', surname='', company='', phone='', email=''):
        if name.isalpha() and surname.isalpha():
            self.__name = name
            self.__surname = surname
            self.__company = company
        if phone.isdigit() or phone == '':
            self.__phone = phone
        else:
            print('Invalid phone number')
            self.__phone = ''
        if checkEmailRegEx(email) or email=='':
            self.__email = email
        else:
            print('Invalid email')
            self.__email = ''
        self.isFavorite = False

    def __str__(self):
        personalData = {
            "Name": self.__name,
            "Surname": self.__surname,
            "Company": self.__company,
            "Phone number": self.__phone,
            "Email address": self.__email
        }
        return tabulate(personalData.items(), tablefmt="simple_grid")

    def __repr__(self):
        return self.__surname
    
    def setFromList(self, givenList):
        if len(givenList) > 5:
            print('Invalid list')
        elif len(givenList) < 5:
            blankFields = 5 - len(givenList)
            fillingList = ['' for i in range(blankFields)]
            givenList.extend(fillingList)

        self.__name = givenList[0]
        self.__surname = givenList[1]
        self.__company = givenList[2]
        self.__phone = givenList[3]
        self.__email = givenList[4]

    def getAsList(self):
        return [self.__name, self.__surname, self.__company, self.__phone, self.__email]

    def get(self, attribute):
        match attribute:
            case 'name':
                return self.__name
            case 'surname':
                return self.__surname
            case 'company':
                return self.__company
            case 'phone':
                return self.__phone
            case 'email':
                return self.__email
            case other:
                print('There is no such attribute')
    
    def set(self, attribute, value):
        match attribute:
            case 'name':
                self.__name = value
            case 'surname':
                self.__surname = value
            case 'company':
                self.__company = value
            case 'phone':
                if value.isdigit():
                    self.__phone = value
                else: 
                    return False
            case 'email':
                if checkEmailRegEx(value):
                    self.__email = value
                else:
                    return False
            case other:
                print('There is no such attribute')
                return False
        return True


class Contacts:

    def __init__(self, givenList=None):
        if givenList is None:
            self.__listOfContacts = []
        else:
            self.__listOfContacts = givenList.copy()

    def __str__(self):
        if self.__listOfContacts:
            theHeader = ['NAME', 'SURNAME', 'COMPANY', 'PHONE NUMBER', 'EMAIL ADDRESS']
            
            listOfFavorites = [prs for prs in self.__listOfContacts if prs.isFavorite]
            if listOfFavorites: 
                listOfFavorites = sorted(listOfFavorites, key=lambda x: x.get('surname'))
                listOfFavorites = [prs.getAsList() for prs in listOfFavorites]
            
            listOfItems = [prs for prs in self.__listOfContacts if prs.isFavorite == False]
            listOfItems = sorted(listOfItems, key=lambda x: x.get('surname'))
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
        if self.i >= len(self.__listOfContacts):
            raise StopIteration
        value = self.__listOfContacts[self.i]
        self.i += 1
        return value

    def search(self, givenContact):
        try:
            position = self.__listOfContacts.index(givenContact)
            #print('Found at position: ' + str(position+1) + ' out of ' + str(len(self.__listOfContacts)))
            return position
        except ValueError:
            return None
            
    def searchFor(self, searchingBy, searchedValue):
        found = []
        for contact in self.__listOfContacts:
            if contact.get(searchingBy) == searchedValue:
                found.append(contact)
        if found:
            print('Contact found')
            return found
        print('Contact not found')

    def add(self, givenContact):
        if isinstance(givenContact, Contact):
            self.__listOfContacts.append(givenContact)
            return True
        else:
            return False

    def pop(self, index = -1):
        self.__listOfContacts.pop(index)

    def addAtPosition(self, givenContact, givenIndex):
        self.__listOfContacts.insert(givenIndex, givenContact)
