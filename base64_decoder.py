#!/usr/bin/python3

# Base64 Decoder for Python
# Created as a challenge for TryHackMe Scripting

import base64

# Read input from a file
f = input('Enter the name of the file to decode: ')
# If no file is entered, use default file 'b64.txt'
if f == '':
    f = '../../Desktop/b64.txt'

# Loop x amount of times
iter = int(input('Enter the amount of decoding loops: '))
# Default to 50 if nothing is entered
if not iter:
    iter = 50

# Decode the file
with open(f) as file:
    for line in file.readlines():
        i = 1
        decoded = base64.b64decode(line)
        # print(decoded)
        while i < iter:
            i += 1
            decoded = base64.b64decode(decoded)
    print('Decoded file', f, iter, 'times and the result is:', decoded)
