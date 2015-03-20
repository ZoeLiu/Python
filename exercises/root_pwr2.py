x = int(raw_input('Enter a positive integer: '))
root =1
pwr =2
ans = False
while root**pwr <= abs(x):
    
    while pwr<6 :
        
       if root**pwr == abs(x):
          print 'The Root of ' + str(x) + ' is ' + str(root) + ' and the pwr is '+ str(pwr)
          ans= True
       
       #print 'pwr is '+ str(pwr)
       pwr = pwr + 1


         
    #print 'root is '+ str(root)
    root = root + 1
    pwr =2


    
if ans ==False:
   print "No such pair of integers exists"
       

    
    
