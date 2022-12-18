from csv import DictReader, DictWriter
import sys
import argparse
import glob
import pandas as pd
import aux_func
import datetime

    #list all files with the corresponding file type 
csv_files = glob.glob('*vpd.csv')
#print(csv_files)

    #define the  arguments
parser = argparse.ArgumentParser()
#parser.add_argument('--day', type = int, required = True)
#parser.add_argument('--month', type = int, required = True)
#parser.add_argument('--year', type = int, required = True)
parser.add_argument('--data', type=lambda s: datetime.date.strptime(s, '%Y-%m-%d'))
parser.add_argument('--file', type = str, required = True)

args = parser.parse_args()

#wrk_data = [args.year, args.month, args.day]


try:
    if args.file in csv_files:
        data= args.file
        #print (data)
        if data in aux_func.date:
            print ('carlos')
        else:
            print ('miguel')

    
        
    
    

except FileNotFoundError:
    print('')
    print("--- CAN YOU PLEASE INSERT AN EXISTING DATASET? ---")
    print('')
    print ('--> currently existing dataset(s):', csv_files)
    print('')
