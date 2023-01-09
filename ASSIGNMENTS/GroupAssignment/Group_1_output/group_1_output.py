import requests
import json

def getHourlyWeatherForescast(lat,lon):
    
    """Accesses open-meteo.com and retrieves, for location Lat, Lon the current weather and the hourly forecast for :
       temperature_2m
       relativehumidity_2m
       precipitation
       soil_moisture_3_9cm
       soil_moisture_9_27cm
       vapor_pressure_deficit
       et0_fao_evapotranspiration   
    Args:
        lat (float): Latitude in deimal degrees
        lon (float): Longitude in decimal degrees
    Returns:
        dictionary: A dictionary with retrieved data from open-meteo
    """

# set URL of API

    original_url = 'https://api.open-meteo.com/' 

# convert the inputs of latitude and longitude into strings (necessarz for concatenation in next step)

    lat = str(lat)
    lon = str(lon)

# concatenate the URL for all data we want to retrieve

    url = original_url + 'v1/forecast?' + 'latitude=' + lat + '&longitude=' + lon + '&current_weather=true&hourly=temperature_2m,relativehumidity_2m,precipitation,soil_moisture_3_9cm,soil_moisture_9_27cm,vapor_pressure_deficit,et0_fao_evapotranspiration'

# request the data from the API

    resp = requests.get(url)

# use the builtin JSON decoder from requests library to create dictionary from the response (JSON data)

    Output1 = resp.json()

# return the output
    return Output1
    

print(getHourlyWeatherForescast(52.52, 13.41))




    
    

    
    
    


    