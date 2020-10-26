# V2 try to make it a bit less messy 
from pwn import * # pip install pwntools
import json
import codecs
import base64
import Crypto

# create socket
r = remote("socket.cryptohack.org", 13377, level = "debug")

# define receive function for json
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

# define send function for json
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

#run loop for 100 rounds
for c in range(101):

    received = json_recv()
    encoding = received["type"]
    print(received)

    if "flag" in received:
        print(received["flag"])
    if received["type"] == "base64":
        decoded = bytes.decode(base64.b64decode(received["encoded"]))
    elif received["type"] == "bigint":
        decoded = bytearray.fromhex(received["encoded"][2:]).decode()
    elif received["type"] == "rot13":
        decoded = codecs.decode(received["encoded"], 'rot13')
    elif received["type"] == "hex":
        decoded = bytearray.fromhex(received["encoded"]).decode()
    elif received["type"] == "utf-8":
        decoded = bytes.decode(bytes("".join([chr(i) for i in received["encoded"]]), 'UTF-8'))
    
    
    text_to_send = { "decoded": decoded}    
    
    json_send(text_to_send)

print(received["flag"])