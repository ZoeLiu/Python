import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset.  This mapper 
    should return a line for each UNIT, along with the number of ENTRIESn_hourly for that row.
    
    An example input to the mapper may would look like this:
    R002    1050105.0
    
    The mapper should emit a key and value pair separated by a tab, for example:
    R002\t105105.0
    """
    
    for line in sys.stdin:
        data = line.strip().split(",")
        #logging.info(data[1]+' '+ data[6])
        if data[1] == "UNIT" or len(data) != 22:
            logging.info("Header skipped or incorrect data")
            continue
        
        print "{0}\t{1}".format(data[1],data[6])
                                    

mapper()
