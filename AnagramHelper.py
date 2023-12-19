import sys
from collections import Counter

input = sys.argv[1]

#Remove spaces and capitalize all letters
input = input.replace(" ", "").upper()

#Create list of characters
inputChars = [char for char in input]

#Create Counter of characters
counter = Counter(inputChars)

