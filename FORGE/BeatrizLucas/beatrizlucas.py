import myFunctions
import myForge.myOtherFunctions

res1 = myFunctions.myFunction()
print(res1)

res2 = myFunctions.myFunction2()
print(res2)

print(myForge.myOtherFunctions.val1)
print(myForge.myOtherFunctions.val2)
print(myForge.myOtherFunctions.val3)

import myForge.myOtherFunctions as func

print(func.val1)
print(func.val2)
print(func.val3)

from myForge.myOtherFunctions import *
from myForge import myOtherFunctions

print(val1)
print(val2)
print(val3)









