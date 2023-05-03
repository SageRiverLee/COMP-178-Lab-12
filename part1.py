#Python OTP decrypter
#Read file
key_file = open("part1.otp.bin", "rb")
message_file = open("part1.ciphertext.bin", "rb")
key = (key_file.read(-1))
encrypted_message = (message_file.read(-1))
print("Encrypted message: ", (encrypted_message))
print("\nOTP: ", (key))
#OTP decryption
decrypted_message = int.from_bytes(encrypted_message) ^ int.from_bytes(key)

#Convert to ascii

#Find number of bytes
byte_number = decrypted_message.bit_length() + 7 // 8

#Make array
binary_array = decrypted_message.to_bytes(byte_number)

#Convert 
ascii_text = binary_array.decode()

#Print in ascii
print("Message: ", ascii_text)

