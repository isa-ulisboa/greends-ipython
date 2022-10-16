a=open("GreenDSfile1.csv")
a.close()

b = open("GreenDSfile1.csv", 'r')
x = len(b.readlines())
print('Total lines:', x) 
b.close()

a = open("GreenDSfile1.csv")
lst = a.readlines()
a.close()
c = open("GreenDSfile1_sample500k.csv", "w")
for i in range(500000):
    c.writelines(lst[i])
c.close()

a = open("GreenDSfile1.csv")
lst = a.readlines()
last_lines=lst[-100:]
a.close()
d = open("GreenDSfile1_samplelast100.csv", "w")
for i in range(100):
    d.writelines(last_lines[i])
d.close()

