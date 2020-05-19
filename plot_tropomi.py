### Importing libraries
import glob
import netCDF4 as nc 
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
import numpy as np 
import sys

# Remove deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# #This finds the user's current path so that all hdf4 files can be found
# try:
#     # inventory.txt must be in the same directory as plot_tropomi.py
#     fileList=open('inventory.txt','r')
# except:
#     print('Did not find a text file containing file names (perhaps name does not match)')
#     sys.exit()

# # Create an empty list
# ncfiles = []

# # Iterate over the files in the no2 directory and append them to the list
# for file in glob.glob("/export/data/scratch/tropomi/no2/*.nc"):
#     ncfiles.append(file)

# my_example_nc_file = ncfiles[1]

# Create a dataset for TROPOMI netCDF4 file
fh = nc.Dataset('/export/data/scratch/tropomi/no2/S5P_OFFL_L2__NO2____20200505T070610_20200505T084741_13264_01_010302_20200507T000819.nc', mode='r')
grp = 'PRODUCT'
# Longitude
lons = fh.groups[grp].variables['longitude'][:][0,:,:]
# Latitude
lats = fh.groups[grp].variables['latitude'][:][0,:,:]
# NO2 data from nitrogendioxide_tropospheric_column 
no2 = fh.groups[grp].variables[
    'nitrogendioxide_tropospheric_column'][0,:,:]
map_label='mol/$m^2$'

# # Print shapes of lists
# print(lons.shape)
# print(lats.shape)
# print(no2.shape)

# Units for NO2
no2_units = fh.groups[grp].variables['nitrogendioxide_tropospheric_column'].units

# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()

### FROM THE TUTORIAL ONLINE
# m = Basemap(width=5000000,height=3500000,
#             resolution='l',projection='stere',\
#             lat_ts=40,lat_0=lat_0,lon_0=lon_0)

# FROM READ_AND_MAP_TROPOMI_NO2_AI.PY
m = Basemap(projection='cyl', resolution='l',
            llcrnrlat=-90, urcrnrlat = 90,
            llcrnrlon=-180, urcrnrlon = 180)

xi, yi = m(lons, lats)

# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(no2),norm=LogNorm(), cmap='jet')

# Add Grid Lines
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180, 180., 45.), labels=[0, 0, 0, 1])

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(no2_units)

# Add Title
plt.title("NO2 in atmosphere")
plt.show()