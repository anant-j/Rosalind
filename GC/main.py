# stream character by character from a file
inputFile = "rosalind_gc.txt"

import sys
store = { }
output = ""

def main():
    global output
    with open(inputFile) as fileobj:
        for line in fileobj:  
            if line[0] == ">":
                key = line[1:].rstrip('\n')
                store[key] = ""
            else:
                store[key] += line.rstrip('\n')
            
main()
maxKey = ""
maxValue = 0
for (key,value) in store.items():
    currVal = (value.count("G") + value.count("C"))/len(value)
    if currVal > maxValue:
        maxKey = key
        maxValue = currVal

print(maxKey, maxValue*100, sep='\n')