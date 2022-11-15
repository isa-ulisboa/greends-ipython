import cdsapi

c = cdsapi.Client()

c.retrieve('sis-agrometeorological-indicators',
    {
        'format': 'zip',
        'variable': 'solar_radiation_flux',
        'year': '2021',
        'month': [
            '03', '04', '05',
            '06', '07', '08',
            '09', '10', '11',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'area': [
            42, -10, 36,
            -5,
        ],
    },
    'download.zip')