
flr = open("GreenDSfile1.csv", "r")

#fl = open("GreenDSfile1.csv", "r")
fllen = len(flr.readlines())
print("Number of lines = ", fllen)
flr.close()


#read the file
fl1 = open("GreenDSfile1.csv", "r")
lst = fl1.readlines()
lst_100 = lst[-100:]
fl1.close()

#create file with the first 500k lines of GreenDSfile1
fl500k_w = open("FORGE/afonsomarques/myForge/assg_5/GreenDSfile1_sample500K.csv", "w")
for i in range(500000):
    fl500k_w.writelines(lst[i])
fl500k_w.close()


#create file with the last 100 lines of GreenDSfile1
fl_last100_w = open("FORGE/afonsomarques/myForge/assg_5/GreenDSfile1_sample-100.csv", "w")
for i in lst_100:
    fl_last100_w.writelines(i)
fl_last100_w.close()

#comando split metodo de uma string









