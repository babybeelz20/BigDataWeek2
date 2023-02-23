# Import the required libraries
import sys;
from itertools import groupby;

# Create a map function
def mapfunc(w):
    # Let us remove all puncuation and spaces.  
    cleanword = ''.join([i for i in w if i.isalpha()])
    return [cleanword,1];
    
# Create a reduce function
def reducefunc(key, values):
    counts = [x[1] for x in values];
    return [key,sum(counts)];
    
# Download the data
!wget https://www.gutenberg.org/cache/epub/1777/pg1777.txt -O romeojuliet.txt

# Split the document into single word
with open("romeojuliet.txt") as f:
    words=[word for line in f for word in line.split()]
    
#print(words)

map_result = map(mapfunc, words)

map_result_sorted = sorted (map_result, key = lambda x: x[0])

reduce_result = [];
for k, g in groupby(map_result_sorted, key = lambda x: x[0]):
    reduce_result.append(reducefunc(k, list(g)))
    
print(reduce_result)
