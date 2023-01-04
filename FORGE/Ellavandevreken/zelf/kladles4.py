#les 21.10 (miss is dit les 5)
#uitleg assignment 6
#hoe extra kolom toevoegen aan een list
import csv
lst = [1,2,3]
lst.append(4)
print(lst)
lst1 = ["1,2,3,4"]
lst1.append("1,2,3,4")
lst1.append("1,2,3,4")
lst1.append("1,2,3,4")
#lst1 is nu een list met 4 elementen nl 4 strings "1,2,3,4"
#uitleg, split
lst2 = []
##lst2.append(lst1[0], split(","))
lst2[0] = [1,2,3,4]

#als je csv wilt importeren en je krijgt een string en je wilt die splitsen bij een bepaald teken kan je commando split.file(seperator) ofzo iets gebruiken

# normaal terminal vanboven: new terminal en typ:
#  pip install netcfd4 
#  maar werkt niet bij

#uitleg bij file iPython-lesson-3-4
import netCDF4 as nc
#gemist hoe je ds aanmaakt en wat het is, overgeschreven van zijn doc
lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
time = ds.variables['time'][:]
precipitation = ds.variables['WDEP_PREC'][:] #2 meter tempeture
print(precipitation)

#another way to read and make a quick map to see it (eerst weer pip install xarray in terminl als je dat nog niet deed)
import xarray as xr
emep = xr.open_dataset("FORGE/EMEP01_rv4.42_year.2019met_2019emis.nc")
#print(prec)
prec = emep.WDEP_PREC
#print(prec)
precgrid = prec.isel(time = 0)  #select one layer (there is only layer in this case nl yearly value)
#... gemist

#uitleg over debuggen, klink op cijfer van een lijn links en maak de bol rood, als je op F5 klikt wordt het script doorlopen tot op bol
#uitleg over hoe je een klok toevoegt (gemist)
#sommige mensen konden niet debuggen een soort programmafout ofzo en dan vroeg python om iets te doen met jameson ofzo, let's hope dat ik die prob niet heb
#uitleg over het rechthoekig balkje met symbolen dat je te zien krijgt als je debugt: 
#   3e icoon = step into  dan ga je naar iets gaan kijken op een andere plaats zoals een functie bvb die gebruikt in huidige file

#assinment 6 verder
import csv 
import myFunctions

with open('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv') as file:
    csvreader = csv.reader(file)
    counter = 0
    header = []
    for day in csvreader:
        if counter<2:
            header.append(day) #eerste 2 lijnen van excel file zitten nu is header (dus het wordt een list met als eerste element de links en als tweede de kolomtitels)
        else: 
            tmin = day[4]  #vanaf dat de counter 2 is gaan we naar dit blok het 4e element van de 3e rij (= gegevens dag 1), erna van de 4e rij (=geg dag2),...
            tmax = day[3]
            rh = day[5]
            vpd = myFunctions.calculate_vpd(tmin, tmax, rh) #vpd van die dag berekenen (ik moet die functie nog maken, was huiswerk)
            day.append(vdp) #aan de list met gegevens van die dag (=list van alles op de lijn van die dag in excelfile) wordt nu achteraan de vpd van die dag toegevoegd
            print(day)
            #thuis: nu moet je deze dag toevoegen aan een list of file waar we alle dagen storen
        counter +=1   #counter elke loop verhogen met 1
    print(header)
    #thuis: nu moet je header nog samenvoegen met alle nieuwe gegevens, "glue them together"

#uitleg over creating folders zie document test.py (of miss foto iphone 21.10)
