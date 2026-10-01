def number_of_classes_sturges(n):    #define the fonction 
    dict={x: 2**x for x in range(1, n + 1)}    #making the dictionnary
    for x, value in dict.items():
        if value >= n:
            return x 
          
