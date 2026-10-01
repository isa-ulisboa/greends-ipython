from read_values import read_values
from determine_min_max import determine_min_max
from number_of_classes_sturges import number_of_classes_sturges
from amplitude import amplitude
from determine_frequency import determine_frequency
from print_frequency import print_frequency

def main():
  # read values
  x=read_values() # x is a list of numbers, either integers or floats
  n=len(x) # integer; number of values
  # determine min value and max value 
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
# execute main
#main()