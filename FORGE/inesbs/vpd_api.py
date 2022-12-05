import myfunctions as mf
import argparse

# define arguments

parser = argparse.ArgumentParser()

parser.add_argument('--tmax', type = float, required=True)
parser.add_argument('--tmin', type = float, required=True, help = "this is min temp in celsius")
parser.add_argument('--rhmean', type = float, required=True)

args = parser.parse_args()

#calculate VPD

vpd = mf.VPdef(args.tmax, args.tmin, args.rhmean)
vpd = round(vpd, 2)

print(vpd)