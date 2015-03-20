'''
create a combiner function to sum counts of words in each line
'''

def combine(line_key_value):

    ''' Sort procedure: sort each element in the key-value pairs list
        so that the same keys are ordered together'''

    line_key_value.sort()
    
    
    ''' initialize an empty list to store all key-sum(value) pairs in a line
        this will be an output from combiner '''
    line_key_sumValue = []

    '''initialize key and word count value'''
    old_key = None
    value_count = 0 

    '''cycle through all (key,1) pairs in a line'''
    for pair in line_key_value:

        '''create separate variables for key and count from the key-value pair list'''
        this_key, count = pair
       
        
        ''' if old_key exists and if current key is not the same as previous key,
            create a list ([key, sum(value)]) of previous key to add to the line_key_sumValue list;
            initialize a new word count for the new key'''
        
        if old_key and old_key != this_key: 
            line_key_sumValue.append([old_key,value_count])
            value_count = 0 
            
        '''assign present key to previous key, and add up the counts'''    
        old_key = this_key
        value_count += float(count)

    '''add the [key, sum(value)] to line_key_sumValue  list for the last key'''
    if old_key != None:
        line_key_sumValue.append([old_key,value_count])

    return line_key_sumValue
            
