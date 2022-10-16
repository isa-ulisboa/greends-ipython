# Test with clay:0.2, silt: 0.2, bulk density: 1.3, om: 0.05, topsoil: 1
# result should be 0.606

import myFunctions
c = 0.2 # clay
s = 0.1 # silk
d = 1.3 # bulk density
om = 0.05
topsoil = 1

result = myFunctions.vol_water_content_saturated(c,d,s,om,topsoil)
print(result)
