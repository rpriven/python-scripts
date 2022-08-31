#!/usr/bin/python3

# Secrets is for creating cryptographically strong passwords and tokens
# as apposed to the random module which is commonly used incorrectly 
# because it is not meant for security or privacy.

import secrets, os, string

# Number of Characters you want it to be
rand = 25

try:
    from secrets import token_hex
    print('Try:', secrets.token_hex(rand))
except ImportError:
    from os import urandom
    def token_hex(nbytes=None):
        return print('Error! Not Secure, fallback to Random \
            \nExcept:', urandom(nbytes).hex())

print(token_hex(rand))
