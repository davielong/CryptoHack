# what we want to do here is to encode the known or plain text and xor it with the input string
# then we need to xor the the result with the input string and dont forget to decode from bytes for print out
from pwn import *

inputString = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
known_pText = "crypto{"

#xor the input with plain text 
temp = (xor(inputString,known_pText.encode())).decode()
# xor the result of plainttext and input string to get flag
flag = xor(inputString,known_pText.encode())
print(flag.decode())
