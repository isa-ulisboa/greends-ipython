
import sys
import argparse
import aux_func


    #define the  arguments
parser = argparse.ArgumentParser()
parser.add_argument('--Tmax', type = float, required = True)
parser.add_argument('--Tmin', type = float, required = True)
parser.add_argument('--RHm', type = float, required = True)

args = parser.parse_args()

    #ensure logical values
if float(args.Tmin) > float(args.Tmax):
    print ('--- SERIOUSLY? ---')
    print ('--- Tmax SMALLER THEN Tmin ---')
    sys.exit()

if float(args.RHm) > 100:
    print ('--- RHm IS A PERCENTAGE ---')
    sys.exit()

    #calculate the vpd and print it
wrk_vpd = aux_func.vap_pres_def(args.Tmax, args.Tmin, args.RHm)
print ('')
print ('--> VPD =', round(wrk_vpd, 2))
