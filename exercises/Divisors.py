#"def findDivisors (n1,n2):"
    #"""assumes that n1 and n2 are positive ints
#       returns a tuple containing common divisors of n1 & n2 """
#    divisors = () #the empty tuple
#    for i in range(1,min(n1,n2)+1):
#        if n1%i == 0 and n2%i == 0:
#            divisors = divisors + (i,)
#    return divisors

#divisors = findDivisors(20,100)
#total = 0
#for d in divisors:
#    total +=d
#print total
#print divisors


def findExtremeDivisors(n1,n2):
    divisors = ()
    minVal,maxVal = None, None
    for i in range(2,min(n1,n2)+1):
        if n1%i == 0 and n2%i ==0:
            if  i < minVal:
                minVal = i
            if  i > maxVal:
                maxVal = i
    return (minVal, maxVal)

minDivisor,maxDivisor = findExtremeDivisors(100,200)
print minDivisor,maxDivisor
