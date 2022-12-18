#ASSIGNMENT 5 - HANDLING AN ASCII FILE

import csv

i=0

with open ("GreenDSfile1.csv", 'r') as file:  #"r" de reading
    csvreader = csv.reader(file)
    for row in csvreader:
        i=i+1

#print(i)  #dá o número de linhas do ficheiro: 2.000.000

#para eliminar a 1.ª linha (quando há título, p.ex.): header = next(csvreader)

lst = []  #criar uma lista vazia
i=0       

with open ("GreenDSfile1.csv", 'r') as file:  
    csvreader = csv.reader(file)
    for row in csvreader:
        while i < 500000:  #para considerar as primeiras 500.000 linhas do ficheiro
            i=i+1
            lst.append(row)  #para adicionar essas linhas à lista criada acima

with open ("GreenDSfile1_sample500k.csv", 'w') as file:  #"w" de writing
    for row in lst:
        file.write(str(row)+ ', ')  #armazena a lista no ficheiro criado


with open ("GreenDSfile1.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if i >= 1999900 and i < 20000000:
            i=i+1
            lst.append(row)
print(lst)

with open ("GreenDSfile1_sample500k.csv", 'w') as file:
    for row in lst:
        file.write(str(row)+ ', ')

