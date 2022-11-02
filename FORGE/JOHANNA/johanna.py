# Assignment #2

print("some brilliant small program")

# Assignment 3 - create a project to interact with your namespaces

# import your myfunctions, myOtherFunctions modules
import myFunctions
import myForge.myOtherFunctions 

import myForge.myOtherFunctions as myAlias
from myForge.myOtherFunctions import *
from myForge import myOtherFunctions

# assign to a variable called res the result of the first function of myFunctions module
# print the res variable
res = myFunctions.function_re_str()
print(res)

# assign to a variable called res the result of the second function of myFunctions module
# print the res variable
res  = myFunctions.function_re_str2()
print(res)

# print the variable val1, val2 and val3 from the module myOtherFunctions
print(myForge.myOtherFunctions.val1)
print(myForge.myOtherFunctions.val2)
print(myForge.myOtherFunctions.val3)

# create an alias of the myOtherFunctions module and redo steps 3, 4, 5, 7, using the alias 
print(myAlias.val1)
print(myAlias.val2)
print(myAlias.val3)

# add this line of code: from myForge.myOtherFunctions import * and redo the steps 
print(val1)
print(val2)
print(val3)

# add this line of code: from myForge import myOtherFunctions and redo the steps
print(myOtherFunctions.val1)
print(myOtherFunctions.val2)
print(myOtherFunctions.val3)

