def myspecialfunction(x=12, y="ella", z=[1,2,3]):   #default values voor als je geen argument meegeeft zijn 12, "ella" en [1,2,3]
#assign to variables (val1, val2, val3) , 3 different datatypes (int, string, list)
  return("the number is "+ str(x)+" the string is "+ y + " te list has " + str(len(z)) + " elements.")
  val1 = x
  val2 = y
  val3 = z
##test
#x = myspecialfunction(12, "hello", ["apple", "banana", "cherry"])
#print(x)