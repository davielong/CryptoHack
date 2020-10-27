# there are 2 solution here that I can see the first is to send 
# both are receiving the n value from from a converted key file
# we convert to pem and then extract or display the key.n 
  
from Crypto.PublicKey import RSA
import OpenSSL.crypto

# solution 1
# this time we read in the file using the rb rather than r arg this means read bytes not just read
output = open("/home/b00131083/college/Secure-Communications/CryptoHack/General/DataFormats/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der","rb").read()
# this is where the key.n value i displayed
print(RSA.importKey(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_ASN1, OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, output).get_pubkey())).n)
print()
print()


# solution 2
# first we need to convert the .der file to a .pem file 
# we do this with the following command, it needs to be entered in terminal
# openssl x509 -in 
#           /home/b00131083/college/Secure-Communications/CryptoHack/General
#           /DataFormats/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der 
#           -inform der -outform pem -out keyfile.pe
# this will convert the file from .der to .pem and then the script below will extract the key.n value 

# notice how we do not read in the file as bytes here it only the "r" arg
keyFile = open("/home/b00131083/college/Secure-Communications/CryptoHack/General/DataFormats/keyfile.pem","r")
key = RSA.importKey(keyFile.read())
print(key.n)