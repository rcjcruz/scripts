#%%
# Importing libraries
import glob
import netCDF4 as nc 
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
import numpy as np 

# Remove deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Create an empty list
ncfiles = []

# Iterate over the files in the no2 directory and append them to the list
for file in glob.glob("/export/data/scratch/tropomi/no2/*.nc"):
    ncfiles.append(file)

my_example_nc_file = ncfiles[1]
fh = nc.Dataset(my_example_nc_file, mode='r')
# print (fh)

# # Print groups
# print(fh.groups)

# # Print the variables
# print(fh.groups['PRODUCT'].variables.keys())

# # Print information about the data
# print (fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'])

# Longitude
lons = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
# Latitude
lats = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
# NO2 data from nitrogendioxide_tropospheric_column 
no2 = fh.groups['PRODUCT'].variables[
    'nitrogendioxide_tropospheric_column'][0,:,:]

# # Print shapes of lists
# print(lons.shape)
# print(lats.shape)
# print(no2.shape)

# Units for NO2
no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'].units

# Plotting on top of England
lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)

xi, yi = m(lons, lats)

# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(no2),norm=LogNorm(), cmap='jet')

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(no2_units)

# Add Title
plt.title('NO2 in atmosphere')
plt.show()

# %%
