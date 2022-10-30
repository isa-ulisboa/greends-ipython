import math



#Crop transpiration (VPD: Vapour pressure deficit) - Function

def calculate_vpd(Tmax,Tmin,RHmean):
        
    #variávies
    e_Tmax= 0.6108**(17*Tmax/(Tmax+237.3))
    e_Tmin= 0.6108**(17*Tmin/(Tmin+237.3))

    #saturation vapour pressure & actual vapor pressure (kPa)
    es=(e_Tmax + e_Tmin)/2
    ea=es*RHmean/100
    vpd=(es - ea)
    
    return vpd
    