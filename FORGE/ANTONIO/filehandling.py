import glob
import sys

x=open("GreenDSfile1.csv",'r')
c=len(x.readlines())
print('total lines:',c)

f=len(glob.glob('*'))
print(f)

v=open("GreenDSfile1.csv")
lst1=v.readlines()
v.close()

fout=open("GreenDSfile1_sample500k.csv","w")
for i in range(500000):
    fout.writelines(lst1[i])
fout.close()    

f1=open("GreenDSfile1.csv")
lst2=f1.readlines()[-100:]
f1.close()

fout1=open("GreenDSfile1_sample100.csv","w")
for i in range(100):
    fout1.writelines(lst2[i])
fout1.close()    


