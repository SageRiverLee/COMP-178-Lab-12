#Public Key Cryptography Example
import nacl.utils
from nacl.public import PrivateKey, Box
import socket
from base64 import b16encode
#Generate Keys
privKey = PrivateKey.generate()
pubKey = privKey.public_key
b = b16encode(bytes(pubKey))
print(b)
#Make Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'cyberlab.pacific.edu'
port = 12001

#Connect to server
s.connect((host, port))

#Send Request
request = "CRYPTO 1.0 REQUEST\r\nName: Sage Lee\r\nPublicKey: {}\r\n\r\n".format(b.decode('ascii'))
print("Sending request: ", request.encode())
s.send(request.encode())

#Recieve Message

response = s.recv(1024)

print(response)
