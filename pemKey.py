from Crypto.PublicKey import RSA

inputFile = open('/home/b00131083/college/Secure-Communications/CryptoHack/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a(1).pem', 'r')
key = RSA.importKey(inputFile.read())

output = key.d

print(output)