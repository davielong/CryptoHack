# 3 * d ≡ 1 mod 13
# to find this we need to understand what the multiplicative inverse
# 

a = 3
p = 13

d = pow(a,p-2) % p 
print(d)