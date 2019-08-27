from cryptography.fernet import Fernet
fileName= './himno.txt'
key = Fernet.generate_key()
f = Fernet(key)
print(key)
with open(fileName, mode='rb') as file: 
    fileContent = file.read()
    token = f.encrypt(fileContent)
    output = open('ciphertext','wb')
    output.write(token)
 
