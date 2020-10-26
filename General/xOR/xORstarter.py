# we need to convert the string label by XORing it with the int 13 and then convert that to a string

message = "label"

temp = [(ord(c) ^ 13) for c in message]
flag = "".join([chr(i) for i in temp])
print("crypto{" + flag + "}")