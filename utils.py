import cdsapi
import geopandas as gpd
import matplotlib.pyplot as plt
from rasterio import features
from affine import Affine
import numpy as np

# Baixar dados de precipitação e temperatura do ERA5
def download_era5_data(variable, year, month):
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'variable': variable,
            'year': year,
            'month': month,
            'day': ['01', '02', '03', '04', '05', '06', '07',
                    '08', '09', '10', '11', '12', '13', '14', '15',
                    '16', '17', '18', '19', '20', '21', '22', '23',
                    '24', '25', '26', '27', '28', '29', '30', '31'],
            'time': ['00:00', '06:00', '12:00', '18:00'],
            'area': [-33.5, -73.0, 5.3, -34.0],  # Lat/Long para o Brasil
            'format': 'netcdf',
        },
        f'{variable}_{year}_{month}.nc')