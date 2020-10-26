# implement simple Euclidian algorithm for GCD(a,b)
#

# set the input params for function
a = 66528
b = 52920
 
# define the function for GCD(a,b)
def gcd(a,b):
    if a == 0:
        
        return b
    #run function b modulo a 
    return gcd(b%a,a)

#print output to terminal
print("the GCD for gcd(",a,",",b,") = ",gcd(a,b))