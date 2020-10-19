#This programme is hanging and needs to fixed 
#Better exit needed and clean up
#Comments to be added
#
#

import json
import base64
import socket
import codecs
import crypto
import random

# set host and port 
host = "socket.cryptohack.org"
port = 13377

#create socket setup
def netcat(hostname, port, message):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(hostname, port)
    soc.sendall(message)
    soc.shutdown(socket.SHUT_WR)
#run socket in loop
    while 1:
        data = soc.recv(1024)
        if data =="":
            break
    soc.close()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))

while 1:
    data = json.loads(soc.recv(1024))
    if 'flag' in data:
        print(data['flag'])
    encoding = data['type']
    print(encoding)

    if encoding == "base64":
        encoded = bytes.decode(base64.b64decode(data['encoded']))
    elif encoding == "bigint":
        encoded = bytearray.fromhex(data['encoded'][2:]).decode()
        print(encoded)
    elif encoding == "rot13":
        encoded = codecs.decode(data['encoded'], 'rot13')
        pass
    elif encoding == "hex":
        encoded = bytearray.fromhex(data['encoded']).decode()
    elif encoding == "utf-8":
        encoded = bytes.decode(bytes(''.join([chr(i) for i in data['encoded']]), "UTF-8"))


    encodedJson = json.JSONEncoder().encode({"decoded": str(encoded)})
    print(encodedJson)
    soc.sendall(bytes(encodedJson, "UTF-8"))
