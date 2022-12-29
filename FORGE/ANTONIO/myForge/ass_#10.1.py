import myFunctions as func
import argparse

# Definition of the arguments of the script 

parser = argparse.ArgumentParser()

parser.add_argument('--tmax', type = float, required = True)
parser.add_argument('--tmin', type = float, required = True)
parser.add_argument('--rhmean', type = float, required = True)

args = parser.parse_args()

#calculation of vpd

vpd = func.calculate_vpd(args.tmax, args.tmin, args.rhmean)
vpd = round(vpd, 2)

print("vpd =", vpd, "kPa")

print("done")