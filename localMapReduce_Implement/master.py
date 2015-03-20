
'''Import functions'''
import mapper
import combiner
import reducer


def master(file):
    

    ''' Step 1:  Input
        Read the document file and
        read each line as an element'''
    with open(file) as f:
        content = f.readlines()
       
  
    ''' Step2: Map & Combine
        Apply the mapper function and combiner function for each line'''

    ''' initialize an empty list to store key-sum(value) pairs created by combiner for ALL lines ;
        this serves as an input for the reducer'''
    all_line_key_sumValue = []


    for line in content:

        ''' call map function to create key-value pair for the line.
            this function output a list(all_key_value) of all (key,1) pairs in a line'''
        line_key_value = mapper.map(line)    
        
        '''call combine function to sum values(counts of each word) for the line.
           this function takes the output from map() and
           output list(line_key_sumValue) that stores counts of words in a line'''
        line_key_sumValue = combiner.combine(line_key_value)   
        

       ''' store all key-sum(value) pairs from ALL lines into one list'''
        for pair in line_key_sumValue:    
            all_line_key_sumValue.append(pair)
            

    ''' Step 3: Shuffle & Sort

        Sort procedure: sort the key-sum(value) pairs for ALL lines (in all_line_key_sumValue list)
        so that the same keys from different lines are ordered together'''
    all_line_key_sumValue.sort()
    
    
    ''' Combine lists of the same key into one as (key, list(values)) pair. 
        e.g. ["a",2],["a",1],["a",5] will combine into ["a", 2, 1, 5] '''

    ''' initialize the new list for (key, list(values)) pair '''   
    all_line_key_valueList = []
    
    ''' initialize old_key to record previous key in the loop '''
    old_key = None

    for pair in all_line_key_sumValue:
        
        '''create separate variables for key and value from the key-sum(value) pairs'''
        this_key, value = pair


        '''if current key is not the same as previous key, add the key to the list
           if the current key is the same as the old key, add the value to the list '''
        
        if old_key != this_key:

            ''' initialize a new list to store key-list(values) if new key is not the same as old key  '''
            key_valueList = []

            ''' add key_valueList to a larger list for the document '''
            all_line_key_valueList.append(key_valueList) 
            
            ''' add the key to the list '''
            key_valueList.append(this_key)
            ''' add # of occurance to the list '''
            key_valueList.append(value)
            
        elif old_key == this_key:
            key_valueList.append(value)

        old_key = this_key
   

    ''' Step 4: 
        Apply reducer to sorted key-sum(value) pairs sent by combiner'''
    doc_key_count = reducer.reduce(all_line_key_valueList)

    ''' Output results. Store final count of all words into a txt file'''
    fo = open("alice_in_wonderland_wordCount.txt",'w')
    for pair in doc_key_count:
        key, value = pair
        print >>fo, key, value


''' run master function '''        
master("alice_in_wonderland.txt")
