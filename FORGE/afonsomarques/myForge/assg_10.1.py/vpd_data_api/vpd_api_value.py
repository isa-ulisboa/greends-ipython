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
parser.add_argument('--day', type = int, required = True)
parser.add_argument('--month', type = int, required = True)
parser.add_argument('--year', type = int, required = True)
parser.add_argument('--file', type = str, required = True)

args = parser.parse_args()

#wrk_data = [args.year, args.month, args.day]


try:
    vpd_file = pd.read_csv(args.file, skiprows=1)
    if vpd_file in csv_files:
        #data = pd.read_csv(args.file, skiprows=1)
        #data_obj = datetime.date(args.data)
        my_date = datetime.date(args.year, args.month, args.day)
        vpd_value = aux_func.validate(args.file, my_date)
        print(vpd_value)

except FileNotFoundError:
    print('')
    print("--- CAN YOU PLEASE INSERT AN EXISTING DATASET? ---")
    print('')
    print ('--> currently existing dataset(s):', csv_files)
    print('')
