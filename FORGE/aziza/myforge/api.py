# create an API 
import sys 
### code to process the arguments passed from outside the script 
args= sys.argv
# print(args)
nameofscript= args[0]
in1= args[1] #arguments are loaded as string.make sure to cast it to needed datatype
in2= args[2]
in3= args[3]
#then you do whatever with the data received
res=in1+in2+in3
print(res)
#clt+z = history
#res=in1*in2*in3 #because can't multiple the string
#handling exceptions 
try:
  nameofscript= args[0]
  in1= args[1]
  in2= args[2]
  in3= args[3]
  #then you do whatever with the data received
  res=in1 * in2 * in3
  print(res)
except Exception as err:
    print (f"unexpected {err=}, {type(err)=}")
#https://www.w3schools.com/bootstrap/bootstrap_grid_basic.asp
