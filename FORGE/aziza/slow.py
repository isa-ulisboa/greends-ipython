import multiprocessing
import time
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