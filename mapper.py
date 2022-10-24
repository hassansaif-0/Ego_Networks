"""mapper.py"""

import sys
import os


# input comes from STDIN (standard input)
maxval=0
circle=""

for line in sys.stdin:
	
    
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    
    if(len(words)-1)>maxval:
    	maxval=len(words)-1
    	circle=words[0]
filepath = os.environ['mapreduce_map_input_file']
filename = os.path.split(filepath)[-1]


	
print(filename+" "+circle+" "+str(maxval))
    
    
    

    
    
    
   
   
