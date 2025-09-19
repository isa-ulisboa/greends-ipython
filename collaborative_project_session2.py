def main():
  # read and sort values
  x=read_values() # x is a list of numbers, either integers or floats
  n=len(x) # integer; number of values
  xmin,xmax=determine_min_max(x) # integers or floats
  # determine number of classes
  m=number_of_classes_sturges(n) # m is a positive integer such that 2**(m-1) <= n <= 2**m
  # determine class amplitude
  delta=amplitude(xmin,xmax,m) # positive float, the range of values divided by the number of classes
  # Compute frequency for each class and plot histogram row by row
  for i in range(m):
    left=xmin+i*delta
    if i < m-1:
      right=left+delta
    else:
      right=left+delta+1 # either 1 or any positive value
    freq=determine_frequency(x,left,right) # integer;  note that each value must belong to one and only one class
    print_frequency(freq) # the output must be '****' where each * represents one observation

def determine_min_max(x):
    xmin = min(x)
    xmax = max(x)
    return xmin, xmax

def number_of_classes_sturges(comprimento_array):
    for m in range(comprimento_array):
        if 2**(m-1) <= comprimento_array <= 2**m:
            return m

def print_frequency(freq):
    print('*' * freq)

def determine_frequency(x,left, right):
    f=0
    for j in range(len(x)):
        if x[j]>=left and x[j]<right:
            f+=1
    return(f)

def read_values():
    # Return a list of numbers
    return [1, 1.2, 3.45, 7.43, 8, 9.7, 13, 22, 31, 15, 2, 3, 4, 5]

def amplitude(xmin,xmax,m):
    return (xmax-xmin)/m

# execute main
main()

