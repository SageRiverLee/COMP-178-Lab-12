#Scrypt Password Hashing
import nacl.secret
import nacl.utils
import nacl.pwhash
import nacl.hash


encrypted_file = open("part4.ciphertext.bin", "rb")
password = b'swordfish'
#Testing password change
#encrypted_file = open("part4.ciphertext-new.bin", "rb")
#password = b'cyberlab'


kdf = nacl.pwhash.scrypt.kdf
salt = encrypted_file.read(32)
ops = nacl.pwhash.SCRYPT_OPSLIMIT_INTERACTIVE
mem = nacl.pwhash.SCRYPT_MEMLIMIT_INTERACTIVE

key = kdf(nacl.secret.SecretBox.KEY_SIZE, password, salt, opslimit=ops, memlimit=mem)
#print("Key: ", key)
genBox = nacl.secret.SecretBox(key)

outer_box = encrypted_file.read(72)
#print("Salt: ", salt)
#print("outer_box_key: ", outer_box)

ranKey = genBox.decrypt(outer_box)
print("Len: ", len(ranKey))
#print("genBox: ", genBox)

inner_box = encrypted_file.read(-1)

genBox2 = nacl.secret.SecretBox(ranKey)
payload = genBox2.decrypt(inner_box)

HASHER = nacl.hash.sha256
digest = HASHER(payload)
with open('payload_file',  'wb') as payload_file:
	payload_file.write(payload)
	payload_file.close()
print("Saved to payload_file")
print("MPEG-4 Video File, viewable through typical video players, e.g  Parole Media Player") 
print("File content: Mr.Robot Season 2 Finale video clip: Dom Shows Darlene The Evidence")
print("Available through youtube:https://www.youtube.com/watch?v=smVVIDWoaxc")

print("SHA-256 hash: ", digest)



