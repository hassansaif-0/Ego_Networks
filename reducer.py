"""reducer.py"""

from operator import itemgetter
import sys

maxval=0
res=""
filename=""
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    words = line.split()
    if int(words[2])>maxval:
    	maxval=int(words[2])
    	filename=words[0]
    	circle=words[1]
    	
    	
print(filename+" "+circle+" "+str(maxval))
   
    


