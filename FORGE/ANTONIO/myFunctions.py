def myfunction():
    return "hi"

def function2():
    return "ola"

from cmath import log
import numpy



def FieldCapacity(C,D,S,OM,TP):
    
    val1=0.7919
    val2=0.001691*C
    val3=0.29619*D
    val4=0.000001491*S**2
    val5=0.0000821*OM**2
    val6=0.02427*C**-1
    val7=0.01113*S**-1
    val8=0.01472*numpy*log(S)
    val9=0.0000733*OM*C
    val10=0.000619*D*C
    val11=0.001183*D*OM
    val12=0.0001664*TP*S

    return val1+val2-val3-val4+val5+val6+val7+val8-val9-val10-val11-val12



       #C-percentage clay;D-bulk density;S-percentage silt;OM-percentage organic matter;
       # TP-opsoil andsubsoil are qualitative variables having the value of 1 or 0"""#