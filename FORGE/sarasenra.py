f = open("GreenDSfile1.csv")
lst = f.readlines()
f.close()

fout = open("GreenDSfile1_sample.csv","w")
for i in range(100):
    fout.writelines(lst[1])
fout.close()