import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cems-glofas-seasonal-reforecast',
    {
        'variable': 'river_discharge_in_the_last_24_hours',
        'format': 'grib',
        'area': [
            42, -9, 36,
            -6,
        ],
        'system_version': 'version_3_1',
        'hyear': '2020',
        'hmonth': 'august',
        'leadtime_hour': '5088',
        'hydrological_model': 'lisflood',
    },
    'download.grib')
