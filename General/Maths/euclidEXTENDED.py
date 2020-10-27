# implementation of Euclidian Extended algorithm for ax + by = GCD(a,b)
# when we divide one integer by another (nonzero) integer we get an integer quotient (the "answer") plus a remainder (generally a rational number). For instance,
# 13/5 = 2 ("the quotient") + 3/5 ("the remainder").
# We can rephrase this division, totally in terms of integers, without reference to the division operation:
# 13 = 2(5) + 3.
# Note that this expression is obtained from the one above it by multiplying through by the divisor 5.
# We refer to this way of writing a division of integers as the Division Algorithm for Integers. More formally stated:
#    If a and b are positive integers, there exist integers unique non-negative integers q and r so that
#    a = qb + r , where 0[less than or equal]r < b.
# The greatest common divisor of integers a and b, denoted by gcd(a,b), is the largest integer that divides (without remainder) both a and b. So, for example:
#  gcd(15, 5) = 5,	gcd(7, 9) = 1,	gcd(12, 9) = 3,	gcd(81, 57) = 3.


# define the function for ax + by = GCD(a,b) base case
# again using recursion as this algorithm is best implemented using recursion 
def gcdExtended(a,b):
    if a == 0:
        
        return b, 0, 1
    
    gcd, x1, y1 = gcdExtended(b%a,a)

    #now use a recursive call to update the x and y
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

# set the input params for function
#Knowing that a and b are prime, the output should be 1
a = 26513
b = 32321
z, x, y = gcdExtended(a,b)
#print output in a nice format 
print(" gcd(",a,",",b,") = ",a ,"X",x," + ",b,"X",y, " = 1")

#1 10245 -8404
# gcd( 26513 , 32321 ) =  10245 and  -8404