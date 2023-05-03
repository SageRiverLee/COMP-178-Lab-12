#Symmetric Key Cryptography
import nacl.secret
import nacl.utils
#Read file
key_file = open("part2.key.bin", "rb")
message_file = open("part2.ciphertext.bin", "rb")
key = (key_file.read(-1))
encrypted_message = (message_file.read(-1))

print("Encrypted message: ", (encrypted_message))
print("\nKey: ", (key))
#Decrypt message
box = nacl.secret.SecretBox(key)

decrypted_message = box.decrypt(encrypted_message)

print("Message: ", decrypted_message)


