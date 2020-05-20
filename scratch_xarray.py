import numpy as np
import pandas as pd 
import xarray as xr 

data = xr.DataArray(np.random.randn(2, 3),dims=('x', 'y'), coords={'x': [10, 20]})
# data.values
# data.dims
# data.coords
# data.attrs

# # indexing
# data[0, :]
# data.loc[10]
# data.isel(x=0)
# data.sel(x=10)

# add attribute metadata
data.attrs['long_name'] = 'random velocity'
data.attrs['units'] = 'm/s'
data.attrs ['description'] ='A random variable'
data.attrs['random_attribute'] = 123

#can add metadata to coordinates
data.x.attrs['units'] = 'x units'

#transpose
#data.T

# # arithmetic operation
# a = xr.DataArray(np.random.randn(3), [data.coords['y']])
# b = xr.DataArray(np.random.randn(4), dims='z')
# # generates a 3x4 tensor with the first row being individual sum of the first 
# # entry of a and each entry of b
# # the second row is the sum of the second entry of a and each entry of b and 
# # likewise for the third row
# a+b

# # exploring GroupBy
# labels = xr.DataArray(['E', 'F', 'E'], [data.coords['y']], name='labels')

# data.plot()


# ds = xr.Dataset({'foo': data, 'bar': ('x', [1, 2]), 'baz': np.pi})
# ds = xr.Dataset({'foo': data, 'bar': ('x', [1, 2]), 'baz': np.pi})

sds_name = 'nitrogendioxide_tropospheric_column'

no2 = xr.open_dataset('/export/data/scratch/tropomi/no2/S5P_OFFL_L2__NO2____20200505T171512_20200505T185642_13270_01_010302_20200507T092201.nc',
                     group='PRODUCT')[sds_name]
print(no2)
no2.plot()