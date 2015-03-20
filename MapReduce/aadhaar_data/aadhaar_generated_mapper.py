import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
   '''
    Tokenize each row using the 
    commas, and emit (i.e. print) a key-value pair containing the 
    district (not state) and Aadhaar generated, separated by a tab. 
    Skip rows without the correct number of tokens and also skip 
    the header row.
   ''' 

    for line in sys.stdin:
        data = line.strip().split(",")
        
        #skip the header
        if data[0] == "Registrar":
            logging.info("Header Skipped: %s", data)
            continue
            
        if len(data) != 12:
            logging.info("Incorrect number of columns")
            continue
            #cleaned_data = i.translate(string.maketrans("",""), string.punctuation)
         
        print "{0}\t{1}".format(data[3],data[8])

mapper()
