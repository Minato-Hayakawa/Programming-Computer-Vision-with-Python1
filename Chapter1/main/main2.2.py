from PIL import Image
from pylab import *

im1=array(Image.open('out/IMG_6417.jpg').convert('L'))

figure()

gray()

contour(im1,origin='image')
axis('equal')
axis('off')

figure()
hist(im1.flatten(),128)
show()