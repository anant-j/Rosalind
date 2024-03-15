# stream character by character from a file

import sys
output = ""

def main():
    global output
    with open("rosalind_rna.txt") as fileobj:
        for line in fileobj:  
            for ch in line: 
                if ch == "T":
                    output += "U"
                elif ch == "U":
                    output += "T"
                else:
                    output += ch
main()
print(output)