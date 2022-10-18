import myfunctions
import myforge.myotherfunction
res = myfunctions
print (res)
res= myfunctions
print (res)
print (myforge.myotherfunction.val1)
print(myforge.myotherfunction.val2)
print (myforge.myotherfunction.val3)
import myforge.myotherfunction as mof
from myforge.myotherfunction import * 
res=myforge.myotherfunction.funct1
res=mof. funct1()
res=funct1

f=open("GreenDSfile1.csv")
lst= f.readline ()
f.close