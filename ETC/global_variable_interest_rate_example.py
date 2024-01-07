rate=0.035
decrease_rate=0.02

def debt(sum,number_years):
    '''
    Here, it is supposed that interest rates decrease by some proportion every year
    '''
    global rate # if missing, UnboundLocalError: local variable 'rate' referenced before assignment
    for _ in range(number_years):
        rate=(1-decrease_rate)* rate
        sum+=sum*rate
    return sum

# Compute debt on a certain sum after a certain number of years
print(debt(100000,10))


