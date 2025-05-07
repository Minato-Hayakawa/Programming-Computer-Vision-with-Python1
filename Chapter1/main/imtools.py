from PIL import Image
import numpy as num
import matplotlib.pyplot as plt
from pylab import *
class imtools:
    def imresize(self,im,sz):
        pil_im=Image.fromarray(uint8(im))
        return num.array(pil_im.resize(sz))
    def histeq(self,im,nbr_bins=256):
        imhist,bins=num.histogram(im.flatten(),nbr_bins,density=True)
        cdf=imhist.cumsum()
        cdf=255*cdf/cdf[-1]
        im2=num.interp(im.flatten(),bins[:-1],cdf)
        return im2.reshape(im.shape),cdf
    def compute_average(self,imlist):
        averageim=num.array(Image.open(imlist[0]),'f') #'f'でfloat型に
        for imname in imlist[1:]: #imlistの1行目の値をすべてimnameに代入
            try:
                averageim+=array(Image.open(imname))
            except:
                print(imname+'....skipped')
        averageim/=len(imlist)
        return array(averageim,'uint8')