# name = input('What is your name?\n')
# print ('Hi, %s.' % name)

# def hello():
#     return 'Hi :)'

# print(hello())

###### GETTING A LIST OF FILES FROM A DIRECTORY
import glob

ncfiles = []
for file in glob.glob("/export/data/scratch/tropomi/no2/*.nc"):
    ncfiles.append(file)

print(ncfiles)