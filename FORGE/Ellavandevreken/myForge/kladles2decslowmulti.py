import multiprocessing
import time
def print_func(nr): 
    lst=[]
    for i in range(5000000): 
        #do something that takes times
        lst.append(i)
    print("I'm processing something slow under item : ", nr)

if __name__ == "__main__":
    start = time.time()
    lst100 = list(range(1,101)) 
    #for nr in lst100:  
    #  print_func(nr)
    #create a list of processes
    procs = [] 
    for nr in lst100: 
        #print(name)
        #instantiating process with arguments
        proc = multiprocessing.Process(target=print_func, args=(nr,)) #vaanaf nu multiprocess
        procs.append(proc)
        proc.start()
        #we are throwing 100 items, processes to all cpu's 
    for proc in procs:
        proc.join()
    print("exec time: ", round(time.time()-start,3))

#tijd was: 13.275