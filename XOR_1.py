test = "label"
num = 13
output = ""

for i in test:
    output = output + chr(num ^ ord(i))
   
print(output)