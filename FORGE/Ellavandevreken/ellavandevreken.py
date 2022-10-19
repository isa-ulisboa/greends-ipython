import net
import myFunctions      #dit is in dezelfde folder als ellavandevreken.py
import myForge.myOtherFunctions    #myOtherFunctions is in another folder nl in myForge dus dot erbij
                                    #bij import zoekt python in de eigen directory

res = myFunctions.firstfun()
print(res)

res = myFunctions.secondfun()
print(res)


val1 = 12
val2 = "hello"
val3 = ["apple", "banana", "cherry"]
print(myForge.myOtherFunctions.val1)
print(myForge.myOtherFunctions.val2)
print(myForge.myOtherFunctions.val3)

#andere opties om te importeren waarbij we telkens hetzelfde bekomen voor res op de lijnen hieronder
import myForge.myOtherFunctions as mof             #mof is an alias for the whole pathname
from myForge.myOtherFunctions import *       # * betekent import everything
from myForge import myOtherFunctions         # same als lijn hierboven 

res = myForge.myOtherFunctions.myspecialfunction()
res = mof.myspecialfunction()      #door lijn 20
res = myspecialfunction()          #door lijn 21 (of 22)


#opdracht tijdens les 14.10
f = open("GreenDSfile1.csv") 
lst = f.readlines()
f.close()

fout = open("GreenDSfile1_sample.csv", "w")
for i in range(100): #van 0 tot 99
    fout.writelines(lst[i])
fout.close()

## nu hebben we een document aangemaakt met de naam GreenDSfile1_sample bestaande uit de eerste 100 lijnen van het document GreenDSfile1 (alle lijnen zitten opgeslagen in de variabele lst) 

#how to delete a file: 
import os
os.remove("GreenDSfile1_sample.csv")

#counting lines (kweenie wat dit hieronder juist is mar check zijn document in de drive: "slingshot2")
for i in range(10):
    fp = open("GreenDSfile1.csv",'r')
    x = len(fp.readlines())
    fp.close()
    print('Total lines:',x)

import netCDF4 as nc
#deze lijn kan je nog niet uitvoeren want ik moest eerst nog pip downloaden eenmaal dat gebeurd is moet je in terminal intypen: 
#pip install netCDF4