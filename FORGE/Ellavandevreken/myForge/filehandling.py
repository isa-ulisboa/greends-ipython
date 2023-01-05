#voor eerder assignments zie file ellavandevreken.py
#assignment 5
f = open("GreenDSfile1.csv") 
lines = f.readlines()
x = len(lines)
print('total lines is',x)
f.close()

fout = open("GreenDSfile1_sample500k.csv", "w")
for i in range(500000): #van 0 tot 499999
    fout.writelines(lines[i])
fout.close()

fout2 = open("GreenDSfile1_samplelast100.csv", "w")
for i in range(100): #van 0 tot 99
    fout2.writelines(lines[x-100+i])
fout2.close()

