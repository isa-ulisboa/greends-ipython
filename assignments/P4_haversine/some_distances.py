from haversine import haversine
from myhaversine import myhaversine

# Some locations
d={
'Lyon': (45.7597, 4.8422), # (lat, lon)
'Paris' : (48.8567, 2.3508),
'Santiago': ( -33.45, -70.67),
'North Pole': (90,0),
'South Pole': (-90,180)
}

# sort 
d = dict(sorted(d.items()))

# compare approximate functions with function from the haversine package
tol=1
for place1,coords1 in d.items():
    for place2,coords2 in d.items():
        if place1<place2:
            myH=round(myhaversine(coords1,coords2),tol)
            correctH=round(haversine(coords1,coords2),tol)
            print(f"From {place1} to {place2}, the distance is {myH} which compares to {correctH} kms")
