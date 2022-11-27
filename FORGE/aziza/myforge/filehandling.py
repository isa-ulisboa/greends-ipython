import csv    
#Open the file
f=open("GreenDSfile1.csv")
lst= f.readline()
f.close()
 
#Count the number of lines and Print the number of files
fp = open("GreenDSfile1.csv", 'r')
x = len(fp.readlines())
print("total lines:", x)
fp.close()
#Create a new file named GreenDSfile1_sample500k.csv to store the first 500 000
fp2= open("GreenDSfile1sample500k.csv", "w")
for i in range(500000):
    fp2.writelines(lst[i])
fp2.close()
#Create a new file named GreenDSfile1_samplelast100.csv to store the last 100 lines
fp3 = open("GreenDSfile1.csv")
lst = fp3.readlines()[-100:]
fp3.close()
fp4 = open("GreenDSfile1_sample.csv", "w")
for i in range(100):
    fp4.writelines(lst[i])
fp4.close()
# Delete a file you should import os - operating system
import os
os.remove("GreenDSfile1_sample.csv")
