import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    compute the average value of ENTRIESn_hourly by weather
    '''

    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        #logging.info(data)
        if len(data) != 2:
            logging.info('key-value pair invalid')
            continue
        
        this_key, count = data

        if old_key and old_key != this_key:  
            avg = riders/num_hours
            print "{0}\t{1}".format(old_key, avg)
            riders = 0
            num_hours = 0
            
        old_key = this_key
        num_hours += 1
        riders += float(count) 
        avg = riders/num_hours
     
    if old_key != None:
        print "{0}\t{1}".format(old_key,avg)
        
                
reducer()
