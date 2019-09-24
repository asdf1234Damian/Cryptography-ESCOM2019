import tkinter as tk
import base64, struct
from tkinter import filedialog
from PIL import Image
from cryptography.fernet import Fernet

#Get Key values
modes = ['a','a']
# print('Select mode:\n  a) Encrypt\n  b) Decrypt')
# modes.append(input())
# print('Select mode:\n  a) CBC\n  b) ECB')
# modes.append(input())

# keyPath = input('Initialization Key path:')
keyPath = './key'
key = open('./key','rb').read()
f= Fernet(key)
filename = 'japon.bmp'
imgIn = Image.open(filename)
imgOut = imgIn.copy()
pixels = imgOut.load()
print(str(modes))
if modes==list('aa'):
        print('Encrypting using CBC')
        for x in range(imgOut.size[0]):
                for y in range(imgOut.size[1]):
                        pixels[x, y] = ((f.encrypt(struct.pack('B',pixels[x, y][0])) % 256),
                                        (f.encrypt(struct.pack('B',pixels[x, y][1])) % 256),
                                        (f.encrypt(struct.pack('B',pixels[x, y][2])) % 256))
print('Done')
imgOut.save('./c_'+filename)
# elif str(modes) == 'ab':
#         for x in range(imgOut.size[0]):
#                 for y in range(imgOut.size[1]):
#                         pixels[x, y] = ((pixels[x, y][0] + keyr) % 256,
#                                         (pixels[x, y][1] + keyg) % 256,
#                                         (pixels[x, y][2] + keyb) % 256)
# elif str(modes)=='ba':
#         pass
# elif str(modes)=='bb':
#         pass

