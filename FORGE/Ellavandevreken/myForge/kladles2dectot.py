import multiprocessing
print("number of cpu: " , multiprocessing.cpu_count()) #eigenschap van mijn pc (number of cores)

#tekst hieronder in cmd prompt uitvoeren door daar te typen python en naam deze file zie worddoc!
import time

#1
def print_func(nr):

    print("I'm processing nr : ", nr)


if __name__ == "__main__":
    start = time.time()
    lst100 = list(range(1,101)) #a list from 1 to 100
    for nr in lst100:  
        print_func(nr)
    
    print("exec time: ", round(time.time()-start,3))

def print_func(nr): 
    lst=[]
    for i in range(5000000): 
        #do something that takes times
        lst.append(i)
    print("I'm processing something slow under item : ", nr)

if __name__ == "__main__":
    start = time.time()
    lst100 = list(range(1,101)) 
    for nr in lst100:  
       print_func(nr)
    
    print("exec time: ", round(time.time()-start,3))

if __name__ == "__main__":
    start = time.time()
    lst100 = list(range(1,101)) 
    #for nr in lst100:  
    #  print_func(nr)
    #create a list of processes
    procs = [] 
    for nr in lst100: 
        proc = multiprocessing.Process(target=print_func, args=(nr,)) #vaanaf nu multiprocess
        procs.append(proc)
        proc.start()
        #we are throwing 100 items, processes to all cpu's 
    for proc in procs:
        proc.join()
    print("exec time: ", round(time.time()-start,3))