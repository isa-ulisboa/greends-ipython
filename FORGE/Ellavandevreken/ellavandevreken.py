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