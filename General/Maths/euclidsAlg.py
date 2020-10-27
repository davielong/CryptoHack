# implement simple Euclidian algorithm for GCD(a,b)
# so we know the base properties of the Euclidian algorithm are as follows
# if A = 0 then GCD(A,B) = B, I.E GCD(0,B)=B   
# also if B = 0 we have the same result
# now what is needed first is to split the largest number into a quotient and remainder
# we write this like so  (A = BQ + R)
# knowing this we can either loop or use recursion 
# using GCD(B,R) for a better understanding please see khanacademy.org 


# set the input params for function
a = 66528
b = 52920
 
# define the function for GCD(a,b)
#this function uses recursion 
def gcd(a,b):
    if a == 0:
        
        return b
    #run function b modulo a this is the Euclidian devision part of the algorithm    
    return gcd(b%a,a)

#print output to terminal
print("the GCD for gcd(",a,",",b,") = ",gcd(a,b))