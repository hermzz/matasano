#!/bin/env python

# 1. Convert hex to base64 and back.
#
# The string:
#
#   49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# should produce:
#
#   SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# Now use this code everywhere for the rest of the exercises. Here's a
# simple rule of thumb:
#
#  Always operate on raw bytes, never on encoded strings. Only use hex
#  and base64 for pretty-printing.

import base64, binascii

# Convert hex to bytes
string = bytes.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
print(string)

# Encode into base64
b64encoded = base64.b64encode(string)
print(b64encoded)

# Decode from base64
b64decoded = base64.b64decode(b64encoded)
print(b64decoded)

# Convert bytes into hex
print(binascii.hexlify(b64decoded))