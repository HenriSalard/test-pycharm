import csv

with open('comptes.csv', 'r') as file:
    obj = csv.reader(file)
    maListe = []

    next(obj) # saute la premiere ligne
    next(obj) # saute la deuxieme ligne
    for line in obj:
        maListe.append(line)


for i in range(len(maListe)):
    print(maListe[i])

