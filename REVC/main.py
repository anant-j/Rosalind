# stream character by character from a file
inputFile = "rosalind_revc.txt"

import sys
store = { "A" : "T", "C" : "G", "G" : "C", "T" : "A"}
output = ""

def main():
    global output
    with open(inputFile) as fileobj:
        for line in fileobj:  
            for ch in line: 
                if ch in store:
                    output += store[ch]
                else:
                    print("Error: invalid character")
main()
print(output[::-1])