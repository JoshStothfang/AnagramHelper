import sys
from collections import Counter
import itertools

input = sys.argv[1]

#Remove spaces and capitalize all letters
input = input.replace(" ", "").upper()

#Create list of characters
inputChars = [char for char in input]

#Create Counter of characters
counter = Counter(inputChars)

print(counter)

results = itertools.permutations(inputChars, 3)

for result in results:
    print(result)