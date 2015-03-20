x=0.001
epsilon = 0.0001
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

#-0.25    0    0.25
#-8       0      8
#8:    0 - 8
#0.25:   0 - 1
#-8:   -8 - 0
#-0.25: -1,0

f1 = min(-1.0,x)
f2 = max(1.0,x)

if x >=0:
   low = 0
   high = f2
else:
   low = f1
   high = 0
   
#positive: 0, f2
#negative: f1,0

ans = (low+ high)/2
while abs(ans**3 -x) >= epsilon:
    print 'low=',low,'high=',high,'ans=',ans
    numGuesses  += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2
print 'numGuesses=',numGuesses
print ans, 'is close to cube root of',x
