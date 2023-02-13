import material
def get_pF_forecast(Theta,soilType):
    """calculates soil tension (pF) for a given list of Volumetric Water Content and soil type

    Args:
        Theta (list): Volumetric Soil Content
        soilType (integer): 1-5 FAO class (1-coarse, 2-Medium, 3-Medium-Fine, 4-Fine, 5-Very Fine)

    Returns:
        list: of soil tension (pF) 
    """
    #use the material module provided to access function formula and soil parameters
    soil_pF =[]
    for idx,i in enumerate(Theta):
        alpha = float(material.soils[soilType]["alpha"])
        Thetar = float(material.soils[soilType]["thetar"])
        Thetas = float(material.soils[soilType]["thetas"])
        nSoil = float(material.soils[soilType]["nsoil"])
                                
        soil_pF.append(material.get_pF(Theta[idx], alpha, Thetar, Thetas,nSoil))
    return soil_pF