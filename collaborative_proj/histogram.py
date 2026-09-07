'''
Builds and prints a text-based histogram for a list of numbers.

The number of classes is determined using Sturges' rule, class amplitude
is computed from the data range, and each class's frequency is printed
as a row of asterisks ('*'), one per observation in that class.
'''

def main():
  # read and values and respective length
  x,n=read_values() # x is a list of numbers, either integers or floats; n is the length of the list
  xmin,xmax=determine_min_max(x) # integers or floats
  # determine number of classes
  m=number_of_classes_sturges(n) # m is a positive integer such that 2**(m-1) <= n <= 2**m
  # determine class amplitude
  delta=amplitude(xmin,xmax,m) # positive float, the range of values divided by the number of classes
  # compute list of (left,right) class boundaries for the histogram, from xmin to xmax
  bins=compute_bins(xmin,xmax,delta)
  # Compute frequency for each class and plot histogram row by row
  for left,right in bins:
    freq=determine_frequency(x,left,right) # integer;  note that each value must belong to one and only one class
    print_frequency(freq) # the output must be '****' where each * represents one observation

def determine_min_max(x):
    '''
    This function returns the minimum and maximum of a list of numbers
    x is  list of integers or floats
    xmin,xmax are the outputs
    '''
    xmin = min(x)
    xmax = max(x)
    return xmin, xmax

def number_of_classes_sturges(comprimento_array):
    '''
    comprimento_array is an integer
    '''
    for m in range(comprimento_array):
        if 2**(m-1) <= comprimento_array <= 2**m:
            return m
def compute_bins(xmin,xmax,delta):
    '''
    xmin, xmax are integers or floats: the minimum and maximum of the data
    delta is a positive number: the width (amplitude) of each class
    returns a list of (left,right) tuples, one per class, starting at xmin
    and spaced by delta, with the last right pushed past xmax so that xmax
    itself (and every value up to it) falls inside the last class
    '''
    bins=[]
    left=xmin
    while left<xmax:
        right=left+delta
        bins.append((left,right))
        left=right
    last_left,last_right=bins[-1]
    bins[-1]=(last_left,last_right+1)
    return bins

def print_frequency(freq):
    print('*' * freq)

def determine_frequency(x,left, right):
    '''
    x is a list of values
    this function computes the number of values larger or equal than left and smaller than right
    '''
    f=0
    for v in x:
      if v>=left and v<right:
            f+=1
    return(f)

def read_values():
    # Return a list of numbers
    values=[1, 1.2, 3.45, 7.43, 8, 9.7, 13, 22, 31, 15, 2, 3, 4, 5]
    return values, len(values)

def amplitude(xmin,xmax,m):
    return (xmax-xmin)/m

# execute main
main()


