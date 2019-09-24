from PIL import Image
import numpy as np 

filename = 'japon.bmp'
imgIn = Image.open(filename)
imgOut = imgIn.copy()
pixels = imgOut.load()
keyr = int(input('Key value for red: '))
keyg = int(input('Key value for green: '))
keyb = int(input('Key value for blue: '))
for x in range(imgOut.size[0]):
    for y in range(imgOut.size[1]):
        pixels[x,y]=((pixels[x, y][0] + keyr ) % 256,
        (pixels[x, y][1] + keyg) % 256,
        (pixels[x, y][2] + keyb) % 256)
imgOut.save('./c_'+filename)

