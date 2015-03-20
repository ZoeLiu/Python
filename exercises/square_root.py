x=0.25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

#while abs(ans**2 - x) >= epsilon and ans <= max(1,x):
#    ans +=step
#    numGuesses +=1

#print 'numGuesses =', numGuesses

#if abs(ans**2-x) >= epsilon:
#    print 'Failed on square root of',x
#else:
#    print ans, 'is close to square root of', x


##### Bisection search


low = 0
high = max(1.0,x)
  
ans = (low+ high)/2
while abs(ans**2 -x) >= epsilon:
    print 'low=',low,'high=',high,'ans=',ans
    numGuesses  += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2
print 'numGuesses=',numGuesses
print ans, 'is close to square root of',x

