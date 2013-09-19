#!/bin/env python

import base64

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
h = ''
for i in b64decoded:
	h += hex(i)[2:]

print(h)