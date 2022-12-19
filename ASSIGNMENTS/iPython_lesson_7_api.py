# GreenDS Master
# João Palma
#################################################################################################
# Creating an API - stand alone program receiving arguments in command line and returning results
# To test this file you need to run this file in terminal, e.g. python3 iPython_lesson_7.api
#################################################################################################


### Code to process the arguments passed from outside the script

# ####### Block 1 - start - to comment/uncomment
# ## Using sys.argv
# import sys
# args = sys.argv
# print (args)
# nameofscript = args[0]
# in1 = args[1] # arguments are loaded as strings. Make sure to cast it to needed datatype
# in2 = args[2] # arguments are loaded as strings. Make sure to cast it to needed datatype
# in3 = args[3] # arguments are loaded as strings. Make sure to cast it to needed datatype
# #then you do whatever with the data received.
# res = in1 * in2 * in3
# print (res) # check why there is an error inthis output and fix it
# ####### Block 1 - end - to comment/uncomment

# ####### Block 2 - start - to comment/uncomment
# ## Adding a block of try, and catch with except
# import sys
# args = sys.argv
# #Handling exceptions
# try:
#     nameofscript = args[0]
#     in1 = args[1] # arguments are loaded as strings. Make sure to cast it to needed datatype
#     in2 = args[2] # arguments are loaded as strings. Make sure to cast it to needed datatype
#     in3 = args[3]
#     #then you do whatever with the data received.
#     res = in1 * in2 * in3 # This script gives an error of TypeError. Add an exception to handle this error to provide a message
#     print (res)
# except IndexError: # see list of exceptions in https://docs.python.org/3/library/exceptions.html#bltin-exceptions
#     print ("You did not specify arguments")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
# ####### Block 2 - end - to comment/uncomment


# ####### Block 3 - start - to comment/uncomment
# ## Using arparse
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--lon', type=float, required=True)
# parser.add_argument('--lat', type=float, required=True)
# args = parser.parse_args()
# dist2equator = int((args.lat * (10000/90)))
# dist2green = int((abs(args.lon) * (10000/90)))
# product = args.lon * args.lat #just a dummy example
# print('Distance to equator:', dist2equator, " km")
# print('Distance to greenwich:', dist2green, " km")
# ####### Block 3 - end - to comment/uncomment

####### Block 4 - start - to comment/uncomment
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--prime', type=int, required=True)
args = parser.parse_args()
# test for prime number
def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
print('Prime number:', is_prime(args.prime))
# # Now you can go to your mersenne quest https://www.mersenne.org 
####### Block 4 - end - to comment/uncomment


# Furhter reading: the ARGPARSE module 
# https://docs.python.org/3/library/argparse.html#module-argparse