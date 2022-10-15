
import myFunctions
import myForge.myOtherFunctions

import myForge.myOtherFunctions as Miguel
from myForge.myOtherFunctions import *
from myForge import myOtherFunctions

res=myFunctions.myfirst()
print(res)
res=myFunctions.mysecond()
print(res)

print(myForge.myOtherFunctions.val1)
print(myForge.myOtherFunctions.val2)
print(myForge.myOtherFunctions.val3)
print(Miguel.val1)
print(Miguel.myfunction())
print(myOtherFunctions.myfunction())