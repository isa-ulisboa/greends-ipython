import myFunctions

import myForge.myOtherFunctions

res = myFunctions.myFunction()
print(res)
res_01 = myFunctions.myFunction1()
print(res_01)

print(myForge.myOtherFunctions.val1)
print(myForge.myOtherFunctions.val2)
print(myForge.myOtherFunctions.val3)

import myForge.myOtherFunctions as mof 

print(mof.val1)
print(mof.val2)
print(mof.val3)

from myForge.myOtherFunctions import *
from myForge import myOtherFunctions

print(val1)
print(val2)
print(val3)