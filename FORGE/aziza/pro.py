import multiprocessing
print ("number of cpu:",multiprocessing.cpu_count())
#print ("number of cpu:",multiprocessing.cpu_count())
import time
def print_func(nr):
    print ("i'm processing nr:",nr)
if __name__ == "__main__":
    start= time.time ()  
    lst100=list(range(1,101)) # a list of 1 to 100
    for nr in lst100:
      print_func (nr)
    
    print ("exec time:",round(time.time()-start,3))

def print_func(nl):
    lst=[]
    for i in range(5000000):
      lst.append(i)
    print ("I'm processing something slow under item:",nl)
if __name__ == "__main__":
    start= time.time ()  
    lst100=list(range(1,101)) # a list of 1 to 100
    for nl in lst100:
      print_func (nl)   


def print_func(nl):
    lst=[]
    for i in range(5000000):
      lst.append(i)
    print ("I'm processing something slow under item:",nl)
if __name__ == "__main__":
    start= time.time ()  
    lst100 =list(range(1,101)) # a list of 1 to 100 
    procs = []
    for nr in lst100:
        proc=multiprocessing.Process(target=print_func,args=(nr,))
        procs.append(proc)
        proc.start()
#complete the processes
    for proc in procs: 
     proc.join()
    print ("exec time:",round(time.time()-start,3))
    