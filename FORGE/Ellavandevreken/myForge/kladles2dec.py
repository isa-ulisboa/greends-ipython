import multiprocessing
#tekst hieronder in cmd prompt uitvoeren door daar te typen python3 naam deze file 
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
#tijd was: 0.031