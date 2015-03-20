import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should return one row
    per unit, along with the total number of ENTRIESn_hourly over the course of may. 
    
    You can assume that the input to the reducer is sorted by UNIT, such that all rows 
    corresponding to a particular UNIT are group together.

    '''
    
    old_key = None
    total_hour = 0
    
    for line in sys.stdin:
        data = line.strip().split("\t")
    
        if len(data) != 2:
            logging.info("key-value pair is incorrect")
            continue
    
        this_key, count = data 
        #logging.info(str(old_key) + ' ' + str(this_key) + ' ' + str(count) + ' ' + str(total_hour))
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, total_hour)
            total_hour = 0 
            
        old_key = this_key
        total_hour += float(count)
    
    if old_key != None:
        print "{0}\t{1}".format(old_key,total_hour)
        
       
reducer()
