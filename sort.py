for i in range(len(source)):
    mini = min(source[i:]) 
    min_index = source[i:].index(mini) 
    source[i + min_index] = source[i] 
    source[i] = mini                
print source

source = [4,2,1,10,5,3,100]