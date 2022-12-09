import myFunctions as f
import argparse

# Definição dos argumentos

parser = argparse.ArgumentParser()

parser.add_argument('--tmax', type = float, required = True)
parser.add_argument('--tmin', type = float, required = True)
parser.add_argument('--rhmean', type = float, required = True)

args = parser.parse_args()

#Calcular VPD

vpd = f.calculate_vpd_7(args.tmax, args.tmin, args.rhmean)

print("vpd =", vpd, "kPa")

#Exemplo para o terminal
#python Assignment10.1.py --tmax 20 --tmin 30 --rhmean 60
