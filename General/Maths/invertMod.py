# 3 * d ≡ 1 mod 13
# to find this we need to understand what the multiplicative inverse is
# Definition:  The multiplicative inverse of a number x is 
# a number x−1 such that:x·x−1= 1.
# Division by x is really multiplication by x−1.
# Over the reals, all values have inverses but zero.
# Over the integers values Only 1 and −1 have inverses.

a = 3
p = 13

d = pow(a,p-2) % p 
print(d)