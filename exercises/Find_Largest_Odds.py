x,y,z=1,1,1
if x%2 == 0:
    if y%2 == 0:
        if z%2 == 0:
            print 'None of the x, y, z are odd'
        else:
            print z
    elif z%2 ==0:
        print y
    elif z < y:
        print y
    else:
        print z
elif y%2 == 0:
    if z%2 == 0:
       print x
    elif x < Z:
       print z
    else:
        print x
else:
    if z%2 == 0:
        if x < y:
            print y
        else:
            print x
    else:
        if x < y:
           temp = y
        else:
           temp = x
        if temp < z:
           temp = z
           print temp
        else:
           print temp
           
           
        
        
        
        
