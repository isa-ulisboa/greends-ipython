f = open("GreenDSfile1.csv")
f.close()

f1 = open("GreenDSfile1.csv", "r")
x = len(f1.readlines())
print("Total lines:", x)
f1.close()

f2 = open("GreenDSfile1.csv")
lst = f2.readlines()
f2.close()
fout = open("c:/Users/joana/Desktop/GDS/INTPY/greends-ipython-1/FORGE/JOANAESTEVES/GreenDSfile1_sample500k.csv", "w")
for i in range(500000):
    fout.writelines(lst[i])
fout.close()

f3 = open("GreenDSfile1.csv")
lst1 = f3.readlines()[-100:]
f3.close()
fout1 = open("c:/Users/joana/Desktop/GDS/INTPY/greends-ipython-1/FORGE/JOANAESTEVES/GreenDSfile1_samplelast100.csv", "w")
for i in range(100):
    fout1.writelines(lst1[i])
fout1.close()


