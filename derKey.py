from Crypto.PublicKey import RSA
import OpenSSL.crypto

output = open('/home/b00131083/college/Secure-Communications/CryptoHack/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der','rb').read()
print(RSA.importKey(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_ASN1, OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, output).get_pubkey())).n)
