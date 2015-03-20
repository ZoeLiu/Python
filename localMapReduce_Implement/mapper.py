import string

'''
create a mapper function to apply to each line
'''

def map(line):

    '''initiate an empty list to store all key-value pairs in a line
       this will be an output from mapper and input for combiner'''
    line_key_value = []
    
    ''' remove leading and trailing blanks of each line'''
    clean_line = line.strip()
    ''' split each line into words with document splitter(space)'''
    words = clean_line.split(" ")
    
    ''' cycle through each word splitted by separater and create (key,1) pair'''	
    for word in words:  
            
	''' remove the punctuation in words and change all words to lower case.
            assign the 'cleaned' words as keys'''
	key = word.translate(string.maketrans("",""),string.punctuation).lower()
            
			
        ''' store the key-value pair(key,1) in a list'''
        this_key_value = [key,1]
        
        '''add the current key-value pair to the list of key-value pairs of the line'''
        line_key_value.append(this_key_value)

    return line_key_value

