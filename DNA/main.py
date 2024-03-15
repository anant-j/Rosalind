# stream character by character from a file

import sys
store = {}

def main():
    with open("rosalind_dna.txt") as fileobj:
        for line in fileobj:  
            for ch in line: 
                if ch in store:
                    store[ch] += 1
                else:
                    store[ch] = 1

main()
print(store["A"], store["C"], store["G"], store["T"])