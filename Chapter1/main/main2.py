from PIL import Image
from pylab import *

im1 = array(Image.open('out/IMG_6417.jpg'))
imshow(im1)
x=[50,40,30,20]
y=[40,40,30,40]

plot(x,y,'b*')
plot(x[:2],y[:2])

title('plotting:"ebara.jpg"')
show()