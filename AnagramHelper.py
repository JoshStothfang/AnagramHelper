import sys
from collections import Counter
import itertools

input = sys.argv[1]

#Remove spaces and capitalize all letters
input = input.replace(" ", "").upper()

results = itertools.permutations(input, len(input))

print(results)

for result in results:
    print("".join(result))