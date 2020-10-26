# to solve this challenge we simply need to convert the given string of hex to a bytes
# and then into plain text 

hex_text = bytearray.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
    
print(hex_text.decode())