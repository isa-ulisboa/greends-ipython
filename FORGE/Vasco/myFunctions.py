def myFirstGreenDSFunction(arg1, agr2):
    print(arg1,agr2)
    return 'GREEN DS'

agr1 = "data source 1"
agr2 = "data source 2"

def test():
    return 'something'
a = test()
print (a)

var1=23
var2='ds'
var3=26

list = (var1, var2, var3)

print(var1)
print(var2)
print(var3)

from math import e
import math

def myfunction():
    return "Soils"

def function2():
    return "Field Capacity"

def FieldCapacity(C,D,S,OM,TP):
    val1=0.7919
    val2=0.001691*C
    val3=0.29619*D
    val4=0.000001491*(S**2)
    val5=0.0000821*(OM**2)
    val6=0.02427*(C**-1)
    val7=0.01113*(S**-1)
    val8=0.01472*(math.log(S))
    val9=0.0000733*OM*C
    val10=0.000619*D*C
    val11=0.001183*D*OM
    val12=0.0001664*TP*S
    return val1+val2-val3-val4+val5+val6+val7+val8-val9-val10-val11-val12

print(FieldCapacity(0.2,1.3,0.1,0.05,1))


#sample file first 100

f = open("GreenDSfile1.csv")
lst = f.readlines()
f.close()

fout = open("GreenDSfile1_sample.cvs" , "w")
for i in range(100):
    fout.writelines(lst[i])
fout.close()