#Open the file
f=open("GreenDSfile1.csv")
lst= f.readline()
f.close()
#Count the number of lines and Print the number of files
fp = open("GreenDSfile1.csv", 'r') 
x = len(fp.readlines())
print('Total lines:', x)
fp.close()
#Create a new file named GreenDSfile1_sample500k.csv to store the first 500 000
f2= open("GreenDSfile1sample500000.csv", "w")
for i in range(500000):
    f2.writelines(lst[i])
f2.close()
#Create a new file named GreenDSfile1_samplelast100.csv to store the last 100 lines 
f3 = open("GreenDSfile1.csv")
lst = f3.readlines()
last_lines=lst[-100:]
f3.close()
fout = open("GreenDSfile1_sample.csv", "w")
fout = f3
fout.close()
#to delete a file you should import os - operating system
import os
os.remove("GreenDSfile1_sample.csv")














