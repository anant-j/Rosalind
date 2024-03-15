# stream character by character from a file
inputFile = "rosalind_hamm.txt"

import sys
output = 0

def main():
    global output
    with open(inputFile) as fileobj:
        line1 = fileobj.readline().strip()
        line2 = fileobj.readline().strip()
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                output += 1
                
main()
print(output)