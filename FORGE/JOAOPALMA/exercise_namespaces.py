# Exercise for practicing namespaces
# To run this script, it is assumed you have two files:
# - One named myfunctions.py in the same directory as this script
# - Another file named myOtherFunctions.py in the directory myForge

import myfunctions
import myForge.myOtherFunctions

# Accessing a predefined function called "MyFirstGreenDSFunction" in the file myfunctions.py
res = myfunctions.MyFirstGreenDSFunction()
print(res, "---MyFirstGreenDSFunction accessed via myfunctions.MyFirstGreenDSFunction")

# Accessing a predefined function called MySecondGreenDSFunction in the file myfunctions.py
res = myfunctions.MySecondGreenDSFunction()
print (res, "---MySecondGreenDSFunction accessed via myfunctions.MySecondGreenDSFunction")

# Accessing a predefined variable called val1, val2, val3 in the file myOtherFunctions.py (stored in the folder myForge)
print (myForge.myOtherFunctions.val1, "---val1 accessed via from myForge.myOtherFunctions.val1")
print (myForge.myOtherFunctions.val2, "---val2 accessed via from myForge.myOtherFunctions.val2")
print (myForge.myOtherFunctions.val3, "---val3 accessed via from myForge.myOtherFunctions.val3")

# using an alias (to simplify usage)
# Note: As a good coding practice, imports should be done at the start of the code
import myForge.myOtherFunctions as mof
res = mof.mySpecialFunction1() 
print(res,"---mySpecialFunction1 accessed via mof.mySpecialFunction1")
print (mof.val1, "---val1 accessed via mof.val1")
print (mof.val2, "---val2 accessed via mof.val3")
print (mof.val3, "---val3 accessed via mof.val3")

# not need for alias if imports all of it 
from myForge.myOtherFunctions import *
res = mySpecialFunction1()
res2 = val2
print(res, "---mySpecialFunction1 accessed via 'from myForge.myOtherFunctions import *'")
print(res2, "---val2 accessed via from myForge.myOtherFunctions import *")

from myForge import myOtherFunctions
res = myOtherFunctions.mySpecialFunction1()
print (res, "---mySpecialFunction1 accessed via 'from myForge import myOtherFunctions'")
