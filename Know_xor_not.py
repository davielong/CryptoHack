from pwn import*

hString1 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
hString2 = bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
known_pText = 'crypto{'

def find_key(cipher: bytearray, plain_text: str):

    key = ''
    for i in range(len(plain_text)):
        key += chr(cipher[i] ^ ord(plain_text[i]))
    return key


def find_flag(encripted_text: bytearray, key ):
    flag = ''
    key_length = len(key)
    for i in range(len(encripted_text)):
        flag += chr(encripted_text[i] ^ ord(key[i%key_length]))
    return flag

key = find_key(hString1, known_pText) + 'y'
flag = find_flag(hString1, key)

print(flag)