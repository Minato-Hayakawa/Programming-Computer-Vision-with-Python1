from PIL import Image
import numpy as num
from pylab import *
im1=num.array(Image.open('out/IMG_6417.jpg'))
print (im1.shape ,im1.dtype)

im2=num.array(Image.open('out/IMG_6417.jpg').convert('L'),'f')
#'f'でfloatにしている。
im3=255-im2 #画像を反転
im4=(100.0/255)*im1+100
im5=255.0*(im1/255.0)**2
show()
def imresize(im,sz):
    pil_im=Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

print(im2.shape ,im2.dtype)