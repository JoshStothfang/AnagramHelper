import sys
from collections import Counter
import itertools

input = sys.argv[1]

#Remove spaces and capitalize all letters
input = input.replace(" ", "").upper()

#Create array of tuples
tupleResults = itertools.permutations(input, len(input))

#Create array of strings and alphabetize
stringResults = []

for result in tupleResults:
    stringResults.append("".join(result))

stringResults.sort()

#Print all results
counter = 0

for result in stringResults:
    if counter != 9:
        print(result, end="  |  ")
        counter += 1
    else:
        print(result)
        counter = 0

print("")