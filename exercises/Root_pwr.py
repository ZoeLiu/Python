x = int(raw_input('Enter a positive integer: '))
root =1
pwr =1
while root**pwr <= abs(x):
    
    while pwr<6 :
        
          if root**pwr < abs(x):
             #print 'pwr is '+ str(pwr)
             pwr = pwr +1
          else:
             break
          #print 'The Root of ' + str(x) + ' is ' + str(root) + 'and the pwr is '+ str(pwr)    
    #if root*pwr == abs(x):
# 
         
    #print 'root is '+ str(root)
    root = root + 1
    pwr =1 
     

if root**pwr !=abs(x):
    print "No such pair of integers exists"
else:
    print 'The Root of ' + str(x) + ' is ' + str(root) + 'and the pwr is '+ str(pwr)
       

    
    
