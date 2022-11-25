import cdsapi

c = cdsapi.Client()

c.retrieve(
    'sis-agrometeorological-indicators',
    {
        'format': 'zip',
        'variable': 'precipitation_flux',
        'year': [
            '2014', '2018', '2022',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '05',
        ],
        'area': [
            40, -9, 36,
            -5,
        ],
    },
    'download.zip')