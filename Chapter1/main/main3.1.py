from PIL import Image
import numpy as num
im1=num.array(Image.open('out/IMG_6417.jpg'))
print (im1.shape ,im1.dtype)

im2=num.array(Image.open('out/IMG_6417.jpg').convert('L'),'f')

print(im2.shape ,im2.dtype)