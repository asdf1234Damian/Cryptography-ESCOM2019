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
        pixels[x,y]=(pixels[x, y][0] + keyr,
        pixels[x, y][1] + keyg,
        pixels[x, y][2] + keyb)
imgOut.save('./c_'+filename)
# imgIn.show()
# pixels = img.load()  # Create the pixel map
# for i in range(img.size[0]):    # For every pixel:
#     for j in range(img.size[1]):
#         pixels[i, j] = (i, j, 100)  # Set the colour accordingly

# img.show()

