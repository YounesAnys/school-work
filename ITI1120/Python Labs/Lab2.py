import math

#First Python Thing
def repeater(s1, s2, n):
    x = "_" + n * (s1 + s2) + "_"
    return x

#Second Python Thing
def roots(a, b, c):
    des = (b**2)-4*a*c
    q = (-b + (des**(0.5))/2*a)
    w = (-b + (des**(0.5))/2*a)
    if des <0:
        print("Sorry, a quadratic equation with these coefficients have no real roots")
    elif des == 0:
        print("You have a double root. The roots to this equation \n are ", q, "and", w)
    else:
        print("The roots to this equation \n are", q, "and", w)    

#Third Python Thing
def real_roots(a,b,c):
    x = (b**2)-(4*a*c)
    if x >= 0:
        print(real_roots == real_roots)
    else:
        print(real_roots == "Why you always lyin?")

#Fourth Python Thing
def reverse(x):
    firstdig = x % 10
    seconddig = x // 10
    finalans = str(firstdig) + str(seconddig)
    finalans = int(finalans)
    return(finalans)
#as an alternative, you could have done 2nd digit * 10, then + 1st digit
