# Create an API that receives Tmin, Tmax, RHmean and returns VPD
import myfunctions as f
import argparse
import sys
# code to process the arguments passed from outside the script 
# args= sys.argv
# Definition of the arguments of the script 
parser = argparse.ArgumentParser(exit_on_error=False)
# parser.add_argument('Filename:calculate_vpd') 
parser.add_argument('--Tmax', type = float, required = True)
parser.add_argument('--Tmin', type = float, required = True)
parser.add_argument('--RHmean', type = float, required = True)
try:
   args = parser.parse_args()
except argparse.ArgumentError:
    print('Catching an argument_Error')
#calculation of vpd
vpd = f.calculate_vpd(args.Tmax, args.Tmin, args.RHmean)
print("vpd =",vpd)

