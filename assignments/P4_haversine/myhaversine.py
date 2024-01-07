from myfunctions import mysqrt, mycos, myarcsin, mysin, get_decimal,deg2rad

def main():
    lat1=get_decimal('Latitude 1st point in decimal degrees',-90,90)
    lon1=get_decimal('Longitude 1st point in decimal degrees',-180,180)
    lat2=get_decimal('Latitude 2nd point in decimal degrees',-90,90)
    lon2=get_decimal('Longitude 2nd point in decimal degrees',-180,180)
    print(f"The distance between points is {myhaversine((lat1,lon1),(lat2,lon2))} km")

def myhaversine(p1,p2):
    R=6371
    lat1,lon1=p1 # degrees
    lat2,lon2=p2
    A=mysin((lat2-lat1)/2)
    B=mysin((lon2-lon1)/2)
    C=A*A+mycos(lat1)*mycos(lat2)*B*B
    C=(C<0)*0+(C>=0)*C # prevents C<0
    H=mysqrt(C)
    H=(-1<H<1)*H+(H<=-1)*(-1)+(H>=1)*1 # prevents H<-1 or H>1
    return 2*R*deg2rad(myarcsin(H))
    
if __name__ == "__main__":
    main()
