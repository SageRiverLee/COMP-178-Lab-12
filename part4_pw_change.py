#Scrypt Password Change
import nacl.secret
import nacl.utils
import nacl.pwhash
import nacl.hash
new_password = b'cyberlab'
original_file = open("part4.ciphertext.bin", "rb")
old_password = b'swordfish'

kdf = nacl.pwhash.scrypt.kdf
salt = original_file.read(32)
ops = nacl.pwhash.SCRYPT_OPSLIMIT_INTERACTIVE
mem = nacl.pwhash.SCRYPT_MEMLIMIT_INTERACTIVE

old_key = kdf(nacl.secret.SecretBox.KEY_SIZE, old_password, salt, opslimit=ops, memlimit=mem)


#print("Key: ", key)
oldBox = nacl.secret.SecretBox(old_key)
outer_box = original_file.read(72)
#Key we need to keep
ranKey = oldBox.decrypt(outer_box)

new_key = kdf(nacl.secret.SecretBox.KEY_SIZE, new_password, salt, opslimit=ops, memlimit=mem)
newBox = nacl.secret.SecretBox(new_key)
encrypted_key = newBox.encrypt(ranKey)

inner_box = original_file.read(-1)

with open('part4.ciphertext-new.bin',  'wb') as new_file:
	new_file.write(salt + encrypted_key + inner_box)
	new_file.close()
	
