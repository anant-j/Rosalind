# stream character by character from a file
inputFile = "rosalind_subs.txt"

import sys

output = []

def main():
    global output
    with open(inputFile) as fileobj:
        dna = fileobj.readline().strip()
        sub = fileobj.readline().strip()
        for i in range(len(dna)):
            if dna[i:i+len(sub)] == sub:
                output.append(i+1)
            

main()

for i in output:
    print(i, end=" ")