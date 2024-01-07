pi = 3.1415926535

# converts angle in decimal degrees to radians
def deg2rad(x):
    return pi*x/180
# converts radians to decimal degrees
def rad2deg(x):
    return 180*x/pi

# Square root function using bissection method
# Input: number
def  mysqrt(x):
    tol=10**-5 # error tolerance
    if x<0:
        return 0
    min=0
    max=x+1
    mid=(min+max)/2
    while abs(mid*mid-x)>tol:
        if mid*mid>x:
            max=mid
        else:
            min=mid
        mid=(min+max)/2
    return mid

# input: angle in decimal degrees
# output: approximate value of the sine of that angle
def mysin(x):
    x=x%360
    if 0<=x<=45: return sin45(x)
    if 45<x<=90: return cos45(90-x)
    if 90<x<=180: return mysin(180-x)
    if 180<x<360: return -mysin(x-180)
    
# input: angle in decimal degrees
# output: approximate value of the cosine of that angle
def mycos(x):
    x=x%360
    if 0<=x<=45: return cos45(x)
    if 45<x<=90: return sin45(90-x)
    if 90<x<=180: return -mycos(180-x)
    if 180<x<360: return -mycos(x-180)
    
# McLaurin approximation for cosine
# Input: angle in degrees (supposed to be between 0 and 45)
def cos45(x):
    n=6 # Number of terms in the approximation
    if x<0 or x>45:
        return 'not reliable'
    x=deg2rad(x)
    cos = 1
    fact = 2
    for i in range(1, n + 1):
        cos += ((-1) ** i) * (x**(2*i) / fact)
        fact *= (2*i+1)*(2*i+2)
    return cos

# McLaurin approximation for sine
# Input: angle in degrees (supposed to be between 0 and 45)
def sin45(x):
    n=6 # Number of terms in the approximation
    if x<0 or x>45:
        return 'not reliable'
    x=deg2rad(x)
    sin = x
    fact= 3*2
    for i in range(1, n + 1):
        sin += ((-1) ** i) * (x**(2*i+1) / fact)
        fact *= (2*i+2)*(2*i+3)
    return sin

# Arcsin using bissection method
# input: number
# output: angle in decimal degrees
def myarcsin(x):
    tol=10**-5 # error tolerance
    if x <= -1:
        return -90
    if x >= 1:
        return 90
    min= -90
    max= 90
    mid=(min+max)/2
    while abs(mysin(mid)-x)>tol:
        if mysin(mid)>x:
            max=mid
        else:
            min=mid
        mid=(min+max)/2
    return mid

# input: string (prompt to user), float (minimum value for input), float (maximum value for input)
# output: float (user's provided value between minimum and maximum)
def get_decimal(prompt: str,Min: float, Max: float) -> float:
    while True:
        try:
            x=float(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x
