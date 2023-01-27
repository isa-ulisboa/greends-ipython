

# Group2 is responsible to provide a function with the calculation of Soil Tension equation (van Genuchten, 1980) 
# The function should be independent of external modules (e.g. endpoint should not need to import material.py module).
# material.py provides the pF equation as van Genuchten (Further reading of van Genuchten equation : https://bit.ly/3V2RPT6 )



soils={
    "1":{"name": "Coarse","alpha":"0.0383","ks":"600","nsoil":"1.3774","thetas":"0.403","thetar":"0.025"},
	"2":{"name": "Medium","alpha":"0.0314","ks":"120.61","nsoil":"1.1804","thetas":"0.439","thetar":"0.01"},
	"3":{"name": "Medium-Fine","alpha":"0.0083","ks":"22.72","nsoil":"1.2539","thetas":"0.43","thetar":"0.01"},
	"4":{"name": "Fine","alpha":"0.0367","ks":"248","nsoil":"1.1012","thetas":"0.52","thetar":"0.01"},
	"5":{"name": "Very-Fine","alpha":"0.0265","ks":"150","nsoil":"1.1033","thetas":"0.614","thetar":"0.01"}
}

#import ASSIGNMENTS.GroupAssignment.material as soil 

import sys
sys.path.insert(1, "/Users/afonsomarques/1_s_mestrado/IPY/greends-ipython/ASSIGNMENTS/GroupAssignment/material.py")

import mod

print (mod.soils)


x = str(soils)

#soilType = soils[x]

#print (soilType["2"])

def get_pF_forecast(Theta,soilType):
    #import soils from "ASSIGNMENTS/GroupAssignment/material.py" as soil 

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