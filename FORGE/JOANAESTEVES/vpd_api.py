import myFunctions as mf
import argparse

# Arguments

parser = argparse.ArgumentParser() 
parser.add_argument('--tmax', type = float, required=True)
parser.add_argument('--tmin', type = float, required=True, help = "this is min temp in celsius")
parser.add_argument('--rhmean', type = float, required=True)
args = parser.parse_args()

# Calculate VPD

vpd = mf.calculate_vpd(args.tmax, args.tmin, args.rhmean)
vpd = round(vpd, 2)

print(vpd)