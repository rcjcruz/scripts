import imageio
import glob

images = []
for filename in glob.glob("/home/rcruz/scripts/tropomi_figures/*.png"):
    images.append(imageio.imread(filename))
imageio.mimsave('tropomi_figures/animation.gif', images, duration=1)