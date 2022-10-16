# Open the file
a=open("GreenDSfile1.csv")
a.close()

# Count the number of lines + print the number of lines
b = open("GreenDSfile1.csv", 'r')
x = len(b.readlines())
print('Total lines:', x) 
b.close()

#Create a new file named GreenDSfile1_sample500k.csv to store the first 500 000 lines
a = open("GreenDSfile1.csv")
lst = a.readlines()
a.close()
c = open("GreenDSfile1_sample500k.csv", "w")
for i in range(500000):
    c.writelines(lst[i])
c.close()

#Create a new file named GreenDSfile1_samplelast100.csv to store the last 100 lines
a = open("GreenDSfile1.csv")
lst = a.readlines()
a.close()
d = open("GreenDSfile1_samplelast100.csv", "w")
for i in range(100):
    d.writelines(lst[-i-1])
d.close()

