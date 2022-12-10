import multiprocessing
import time
def print_func(nr):
    lst=[]
    for i in range(5000000):
      lst.append(i)
    print ("I'm processing something slow under item:",nr)
if __name__ == "__main__":
    start= time.time ()  
    lst100=list(range(1,101)) # a list of 1 to 100
    for nr in lst100:
      print_func(nr)  
print ("exec time:",round(time.time()-start,3)) 