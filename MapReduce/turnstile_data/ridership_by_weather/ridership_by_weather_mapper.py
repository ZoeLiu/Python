import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    '''
    Compute the average value of the ENTRIESn_hourly column 
    for different weather types. Weather type will be defined based on the 
    combination of the columns fog and rain (which are boolean values).
    For example, one output of our reducer would be the average hourly entries 
    across all hours when it was raining but not foggy.

    '''

    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that should output. 
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )

    for line in sys.stdin:
    	data = line.strip().split(',')
    
        if data[1] == "UNIT" or len(data) != 22:
            logging.info("Skip header or data input error")
            continue
        #logging.info(format_key(float(data[14]),float(data[15])))
                     
        print "{0}\t{1}".format(format_key(float(data[14]),float(data[15])), data[6])

mapper()
