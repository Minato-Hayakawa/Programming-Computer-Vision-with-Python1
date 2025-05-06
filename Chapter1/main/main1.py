from PIL import Image

im1=Image.open('main/photo/IMG_6417.jpg')
im1g=im1.convert('L')
im1g.save('out/IMG_6417.png')
im1g.thumbnail((128,128))
im1g.save('out/IMG_6417(2).png')
range=(100,100,100,100)
im1g.crop(range)
im1g.save('out/IMG_6417c.png')
im2g=im1g.transpose(Image.ROTATE_90)
im2g.save('out/IMG_6417_rot90.png')
im1g.paste(im2g)
im1g.save('out/IMG_6417_(3).png')