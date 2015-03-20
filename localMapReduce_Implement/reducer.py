'''
create a reducer function to take in key, list(values)
and sum the values in list(values) for each key
'''

def reduce(all_line_key_valueList):


    '''initialize an empty list to store all words' count in the document
       this will be an output from reducer'''
    doc_key_count = []
    

    '''cycle through all [key, list(values)] lists '''
    for pair in all_line_key_valueList:
        
        ''' initialize count'''
        count = 0
       
        ''' cycle through each element in the [key.list(values)] list'''
        for each in pair:
   
            ''' if the element in the pair is numeric, then add it to count
                if not -which means it is the key, then assign it to key '''
            if isinstance(each, (int, long, float, complex)) == True:
                count += each
            else:
                key = each	
  
        ''' add the final count pair to the doc_key_count list '''
        doc_key_count.append([key,count])    
        
    return doc_key_count
                      
