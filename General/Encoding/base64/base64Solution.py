# to solve this challenge we need to convert to a byte array and then encode it to base 64
import base64 as b

# hex_input = 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

flag = b.b64decode("crypto/Base+64+Encoding+is+Web+Safe/")
#flag.decode()    

print(flag)
