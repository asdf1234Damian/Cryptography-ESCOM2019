fileName = './himno.txt'
cipher = './cipher.txt'
print('Select an option')
print('1.- Encrypt')
print('2.- Decode')
if input() == '1':
    with open(fileName, mode='rb') as file:
        n = int(input('Number of shifts:'))
        n = n % 26
        print('Message shifted '+ str(n) + ' times')
        cipherFile = open(cipher, '+w',encoding="utf-8")
        for ch in file.read().decode('utf-8'):
            cipherFile.write(chr(ord(ch)+n))

else:
    with open(cipher, mode='rb') as file:
        n = int(input('Number of shifts:'))
        n = n % 26
        print('Message shifted ' + str(n) + ' times')
        for ch in file.read().decode('utf-8'):
            print(chr(ord(ch)-n),end='')

