f=open("GreenDSfile1.csv")
lst= f.readline()
f.close

f1 = open("GreenDSfile1.csv", 'r')
x = len(f1.readlines())
print('Total lines:', x) 
f1.close()

f2= open("GreenDSfile1sample500000.csv", "w")
for i in range(500000):
    f2.writelines(lst[i])
f2.close()

f3 = open("GreenDSfile1.csv")
lst = f3.readlines()
last_lines=lst[-100:]
f3.close()

f4 = open("GreenDSfile1samplelast100.csv", "w")
for i in range(100):
    f4.writelines(last_lines[i])
f4.close()

