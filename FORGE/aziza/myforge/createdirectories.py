# impot the os module
from importlib.resources import path
import os
from posixpath import pardir
# create a list with the directories 
os.listdir =[]
for i in range(10):
   os.listdir. append("GreenDS_SampleFolder"+ str(i+1))
# create a folder based on the list we created
# make sure about our parent directory
pardir= "aziza\\myforge\\"
for item in os.listdir: 
   path2create= os.path.join(pardir,item)
   os.mkdir(path2create)
