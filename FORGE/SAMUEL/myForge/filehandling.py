#ASSIGNMENT 5 - HANDLING AN ASCII FILE

import csv

i=0

with open ("GreenDSfile1.csv", 'r') as file:  #"r" de reading
    csvreader = csv.reader(file)
    for row in csvreader:
        i=i+1

print(i)  #dá o número de linhas do ficheiro: 2.000.000

#para eliminar a 1.ª linha (quando há título, p.ex.): header = next(csvreader)


#para armazenar as primeiras 500000 linhas:
lst = []  #criar uma lista vazia
i=0       

with open ("GreenDSfile1.csv", 'r') as file:  
    csvreader = csv.reader(file)
    for row in list(csvreader)[0:500000]:
        #while i < 500000:  #para considerar as primeiras 500.000 linhas do ficheiro, mas dá zeros e não pode
            #i=i+1
            lst.append(row)  #para adicionar essas linhas à lista criada acima
            print(row)

with open ("GreenDSfile1_sample500k.csv", 'w') as file:  #"w" de writing
    for row in lst:
        file.write(str(row)+ ', ')  #armazena a lista no ficheiro criado


#para armazenar as últimas 100 linhas:
lst = []
i=0

with open ("GreenDSfile1.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in list(csvreader)[1999900:2000000]:
        lst.append(row)
        print(row)

with open ("GreenDSfile1_sample100.csv", 'w') as file:
    for row in lst:
        file.write(str(row)+ ', ')

