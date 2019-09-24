
a = 5
b = 4
z = 12
while(True):
    c = input('char: ')
    c = ord(c)-ord('a')
    print(c , chr(ord('a')+((a*c+b) % z)))
