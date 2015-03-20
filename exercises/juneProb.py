import random

def juneProb(numTrials):
    june48 = 0.0
    for trial in range(numTrials):
        june = 0.0
        for i in range(446):
            if random.choice([1,2,3,4,5,6,7,8,9,10,11,12])==6:
                             june +=1
        if june >=48:
           june48 +=1
    jProb = str(june48/numTrials)
    print 'Probability of at least 48 births in June =' + jProb
                             

