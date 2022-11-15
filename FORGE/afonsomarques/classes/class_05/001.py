

import os


#creating a range(n) number of lists 
lstdirs=[]
for i in range(10):
    lstdirs.append('GDS_sample_folder_00'+ str(i+1))



#creating 10 directories in (path)
path = 'FORGE/afonsomarques'
for item in lstdirs:
    path2create = os.path.join(path, item)
    os.mkdir(path2create)


#creatinb 10 csv files inside each previous created folder with 1000's each
for item in lstdirs:
    outfolder = os.path.join(path, item)
    for f in range(10):
        fout = open (outfolder+'/file'+str(f+1)+'.csv', 'w')
        for n in range(1000):
            fout.write(str(n)+'\n')
        fout.close()
