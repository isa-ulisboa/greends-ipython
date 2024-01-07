# Compute accumulated interest on a sequence of borrowed amounts
def main(*args, **kwargs):
    '''
    args is a tuple of amounts borrowed
    kwargs is a dictionary with keys num_years and rate
    '''
    print('Positional (*)',args) # args is a tuple
    S=sum(args) 
    print('sum', S)
    print('Named (**)',kwargs) # kwargs is a dictionary
    # Call function debt with **kwargs or kwargs
    D=debt(S,**kwargs) # D expects a number and two named arguments with names num_years and rate
    # same as:
    D=debt(S,kwargs['num_years'],kwargs['rate']) # D expects a number and two named arguments with names num_years and rate
    return D

def sum(values):
    s=0
    for x in values:
        s+=x
    return s

def debt(s,num_years,rate):
    for i in range(num_years):
        s+=s*rate
    return s

if __name__=='__main__':
    D=main(1,2,10,5,num_years=10, rate=0.01)
    print(D)
  

