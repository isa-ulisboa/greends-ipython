#ASSIGNMENT #1

print("Seja bem-vindo!")

idade = 20
print(idade)


#ASSIGNMENT #3 (CONT.)

from myForge.myOtherFunctions import myotherfunctions
import myFunctions
import myForge.myOtherFunctions as mof

res_1 = myFunctions.myFirstGreenDSFunction()
print(res_1)

res_2 = myFunctions.mySecondGreenDSFunction()
print(res_2)

res_3 = mof.myotherfunctions()
print(res_3)

print(mof.val1)
print(mof.val2)
print(mof.val3)

'''
from myForge import myOtherFunctions ou import myForge.myOtherFunctions
print(myOtherFunctions.val1)
'''



