import pickle 
import bz2

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
file_name = 'dogs' #file name must not have an extension

# Writing to the pickle file; 'b' for binary
outfile = open(file_name, 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()

# Opening the pickle file
infile = open(file_name, 'rb')
new_dict = pickle.load(infile)
infile.close()

# Compressing pickle files; can use bzip2 or gzip
# bzip2 is slower, gzip produces files about twice as large as bzip2

sfile = bz2.BZ2File('smallerfile', 'w')
pickle.dump(dogs_dict, sfile)