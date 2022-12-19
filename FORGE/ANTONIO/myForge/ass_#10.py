import myFunctions as f
import argparse

# Definição dos argumentos

parser = argparse.ArgumentParser()

parser.add_argument('--tasmax', type = float, required = True)
parser.add_argument('--tasmin', type = float, required = True)
parser.add_argument('--hurs', type = float, required = True)

args = parser.parse_args()

#Calcular VPD

vpd = f.calculate_vpd_7(args.tasmax, args.tasmin, args.hurs)

print("vpd =", vpd, "kPa")

