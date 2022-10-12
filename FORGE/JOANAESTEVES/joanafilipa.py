print('green data science')
import myFunctions
import myforge.myotherFunctions
res = myFunctions.string()
print(res)
res = myFunctions.myfunction()
print(res)
print(myforge.myotherFunctions.val1)
print(myforge.myotherFunctions.val2)
print(myforge.myotherFunctions.val3)
import myforge.myotherFunctions as mof #dar outro nome a mesma funcao
from myforge.myotherFunctions import *
import myFunctions as mf
res = mf.string()
print(res)
res = mf.myfunction()
print(res)
print(mof.val1)
print(mof.val2)
print(mof.val3)

