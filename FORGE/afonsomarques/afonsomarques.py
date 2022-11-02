
import myFunctions as mf
#import myForge.my0therfunctions as m0f
###tthe method  (from xxxxx import *) imports everything which is better fo this specific aplicion
from myForge.my0therfunctions import *


res1=mf.my_funnction1()

res2=mf.my_function2()


print(val1,val2,val3)

def res3():
    val2_cap= val2.capitalize()
    val3_length = len(val3)
    for i in val3:
        if i == val3[0]:
            print ("O",val2_cap, "tem", val3_length, "cartões,",val1, "com o numemro", i)
            continue
        print ("outro com o numero", i)

res3()