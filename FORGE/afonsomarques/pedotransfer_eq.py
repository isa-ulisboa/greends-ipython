

import math

def pedotransfer (C, S, D, OM, topsoil):
### C = %  of clay
### S = % of silt
### D = bulk desnity
### OM = % of organic matter
### topsoil = qualitative paramter (0 OR 1)

    l1 = [0.7919, 0.001691*C, -(0.29619*D), -(0.000001491*S**2), 0.0000821*OM**2, 0.02427*C**-1, 0.01113*S**-1, 0.01472*math.log(S), -(0.0000733*OM*C), -(0.000619*D*C), -(0.001183*D*OM), -(0.0001664*topsoil*S) ]
    s = sum(l1)
    return(s)

print (pedotransfer(0.2, 0.1, 1.3, 0.05, 1)) 
