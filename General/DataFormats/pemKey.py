from Crypto.PublicKey import RSA

#read in the .pem key file
inputFile = open("General/DataFormats/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "r")
key = RSA.importKey(inputFile.read())

#print the key in decimal form 
print(key.d)