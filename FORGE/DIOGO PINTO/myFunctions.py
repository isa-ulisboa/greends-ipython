'''
#Funções
def teste2():
    return 'myFunc= diogo'


def teste3():
    return 'myFunc= aleleluia'

#########################
def t1():
    return ('ola')

print(t1())

def t2(x,y):
    return (x+y)

print('Soma:', t2(10,20))
'''

import math
def FieldCapacity(C,D,S,OM,TP):
    
    a=0.7919
    b=0.001691*C
    c=0.29619*D
    d=0.000001491*(S**2)
    e=0.0000821*(OM**2)
    f=0.02427*(C**-1)
    g=0.01113*(S**-1)
    h=0.01472*(math.log(S))
    i=0.0000733*OM*C
    j=0.000619*D*C
    k=0.001183*D*OM
    l=0.0001664*TP*S


    return a+b-c-d+e+f+g+h-i-j-k-l

print(FieldCapacity(0.2,1.3,0.1,0.05,1))

#com S= 0.2 não dá