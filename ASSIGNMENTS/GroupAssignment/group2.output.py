# Group2 is responsible to provide a function with the calculation of Soil Tension equation (van Genuchten, 1980) 
# The function should be independent of external modules (e.g. endpoint should not need to import material.py module).
# material.py provides the pF equation as van Genuchten (Further reading of van Genuchten equation : https://bit.ly/3V2RPT6 )

def get_pF_forecast(Theta,soilType):
    """calculates soil tension (pF) for a given list of Volumetric Water Content and soil type
    Args:
        Theta (list): Volumetric Soil Content
        soilType (integer): 1-5 FAO class (1-coarse, 2-Medium, 3-Medium-Fine, 4-Fine, 5-Very Fine)
    Returns:
        list: soil tension (pF) 
    """
    #use the material module provided to access function formula and soil parameters
    soil_pF =[]
    
    return soil_pF