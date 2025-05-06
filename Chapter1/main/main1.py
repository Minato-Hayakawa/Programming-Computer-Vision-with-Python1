from PIL import Image

im1=Image.open('main/photo/IMG_6417.jpg').convert('L')
im1g=im1.convert('L')
im1g.save('out/IMG_6417.png')