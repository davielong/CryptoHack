from pwn import xor

# 1st rule: key1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# 2nd rule: key1 ^ key2 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# 3rd rule: key2 ^ key3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# 4th rule: 
#   FLAG ^ key1 ^ key2 ^ key3 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

key2 = xor(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'), key1)

key3 = xor(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'), key2)

kxr1_2 = xor(key1,key2)
kxr1_2_3 = xor(kxr1_2,key3)

flag = xor(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'),kxr1_2_3)

print(flag)