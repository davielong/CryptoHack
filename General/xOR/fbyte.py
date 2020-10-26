# to solve this one we just need to convert the string from hex to a byte array
# and then grab the char for each value in the byte array anf xor it 

decode_message = bytearray.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

flag = ""

for i in decode_message:
    flag+= chr(i ^ 16)
print(decode_message)
print(flag)