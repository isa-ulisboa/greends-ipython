import material as mtr

def get_pF_forecast(Theta, soilType):
    # import the functions from mterial.py 
    # it is inside de function for it to be independent from externela modules
    import material as mtr
    # create the empty list for the pF's
    soil_pF =[]
    alpha = float(soilType['alpha'])
    Thetar = float(soilType['thetar'])
    Thetas = float(soilType['thetas'])
    nSoil = float(soilType['nsoil'])
    # use of the FUNCTION get_mSoil just need to be made one time for each FOR loop
    mtr.get_mSoil(nSoil)
    # FOR loop to execute the FUNCTION get_pF for each Theta
    for i in Theta:
        pF = mtr.get_pF(i, alpha, Thetar, Thetas, nSoil)
        soil_pF.append(pF)
    return soil_pF

soil_mst_3_9 = mtr.Output1Group1['hourly']['soil_moisture_3_9cm']

soil_mst_9_27 = mtr.Output1Group1['hourly']['soil_moisture_9_27cm']


pf = get_pF_forecast ( soil_mst_3_9, mtr.soils["2"])

print (pf)