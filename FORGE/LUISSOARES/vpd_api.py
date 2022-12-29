import numpy as np
import myFunctions as mf
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--tmax', type = float, required = True, help= "Temperatura máxima")
parser.add_argument('--tmin', type = float, required = True, help= "Temperatura mínima")
parser.add_argument('--rhmean', type = float, required = True, help= "Humidade relativa média")

args = parser.parse_args()


vpd = mf.calculate_vpd(args.tmax, args.tmin, args.rhmean)
vpd = round(vpd, 3)

print("Vapor pressure deficit is:", vpd, "kPa.")

