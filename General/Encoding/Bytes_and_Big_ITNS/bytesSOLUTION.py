#to solve this we need to convert the input to a byte stream and decode to plain text
from Crypto.Util.number import long_to_bytes

input_string =  long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)

print(input_string.decode())

# flag = crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}