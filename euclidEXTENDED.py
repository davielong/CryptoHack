# implementation of Euclidian Extended algorithm for ax + by = GCD(a,b)

# define the function for ax + by = GCD(a,b) base case
def gcdExtended(a,b):
    if a == 0:
        
        return b, 0, 1
    
    gcd, x1, y1 = gcdExtended(b%a,a)

    #now use a recursive call to update the x and y
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


# set the input params for function
a = 26513
b = 32321
g, x, y = gcdExtended(a,b)

#print output to terminal
print("the GCD for gcd(",a,",",b,") = ",x ,'and ' ,y)