import os 

lst = []

for i in range (10):
    lst.append("GreenDS_SampleFolder" + str(i+1)) #no primeiro run, i = 0. Por isso é que se coloca i+1

pardir = "FORGE\\BeatrizLucas\\"

for item in lst:
    path2create = os.path.join(pardir, item)
    os.mkdir(path2create)

for item in lst:
    outfolder = os.path.join(pardir,item)
    for f in range (10): #create 10 files
        fout = open(outfolder+"/file_"+str(f)+".csv","w")
        for n in range (1000):
            fout.write(str(n)+"\n")
        fout.close()