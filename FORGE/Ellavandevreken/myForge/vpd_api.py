#assignment 10.1
import myFunctions as mf
import argparse

# define arguments

parser = argparse.ArgumentParser() 

parser.add_argument('--tmax', type = float, required=True, help = "The maximum temperature as a string converted to an argument of type float" )
parser.add_argument('--tmin', type = float, required=True, help = "The minimum temperature as a string converted to an argument of type float")
parser.add_argument('--rhmean', type = float, required=True, help = "The mean relative humidity as a string converted to an argument of type float")

args = parser.parse_args()

if float(args.rhmean) < 0:
    raise Exception('The mean relative humidity can not be negative')
if float(args.rhmean) >100:
    raise Exception('The mean relative humidity can not be higher than 100%')

#VPD calculation

vpdvalue = mf.calculate_vpd(args.tmax, args.tmin, args.rhmean)
vpd = round(vpdvalue, 2)

print("The vpd is", vpd, "kPa.")