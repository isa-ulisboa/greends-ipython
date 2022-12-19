import myFunctions_10_1 as mf10_1
import argparse


#Giving the arguments
parser = argparse.ArgumentParser()

parser.add_argument('--Tmin', type = float, required = True)
parser.add_argument('--Tmax', type = float, required = True)
parser.add_argument('--RHmean', type = float, required = True)

args = parser.parse_args()

##Possible input Errors##
if float(args.Tmin) < 0:
    raise Exception('Sorry, impossible having nr below zero')
if float(args.Tmax) < 0:
    raise Exception('Sorry, impossible having nr below zero')
if float(args.RHmean) < 0:
    raise Exception('Sorry, impossible having nr below zero')
if float(args.RHmean)>100:
    raise Exception('Sorry, impossible having nr over one hundred ')


#VPD calculation
vpd= mf10_1.calculate_vpd(args.Tmin,args.Tmax,args.RHmean)

print('')
print('Vapour pressure deficit=',round(vpd,3),'\n')