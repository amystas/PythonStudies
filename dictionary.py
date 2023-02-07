from tabulate import tabulate 
dictionary = dict()
for i in range(10):
    pol = input('Type a Polish word: ')
    eng = input('Type an English word: ')
    dictionary.update({pol: eng})

print(tabulate(dictionary.items(), headers=["POLSKI", "ANGIELSKI"]))