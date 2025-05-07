from PIL import Image
import numpy as num
from pylab import *
class imtools:
    def imresize(im,sz):
        pil_im=Image.fromarray(uint8(im))
        return num.array(pil_im.resize(sz))
    def histeq(im,nbr_bins=256):
        imhist,bins=num.histogram(im.flatten(),nbr_bins,normed=True)
        cdf=imhist.cumsum()
        cdf=255*cdf/cdf[-1]
        im2=num.interp(im.flatten(),bins[:-1],cdf)
        return im2.reshape(im.shape),cdf

imtoolsobj=imtools()
im1=num.array(Image.open('out/IMG_6417.jpg'))
im2,cdf=imtoolsobj.histeq(im1)