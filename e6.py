#!/bin/env python

# 6. Break repeating-key XOR
#
# The buffer at the following location:
#
#  https://gist.github.com/3132752
#
# is base64-encoded repeating-key XOR. Break it.

import base64, math
from lib import find_best_xor_match, key_encode

def hamming(a, b):
	return sum([sum([int(j) for j in str(bin(a[i] ^ b[i]))[2:]]) for i in range(0,len(a))])

buff = base64.b64decode(''.join([line.rstrip() for line in open('e6.txt', 'r')]))

# Number of sample blocks we want to use to calculate hamming dist
avg_blocks = 4
keys = []
for key_size in range(2,41):
	# Grab first X number of buffer blocks
	blocks = [buff[i * key_size:(i * key_size) + key_size] for i in list(range(0, avg_blocks))]

	# Calculate hamming dist between them
	hamm = sum([hamming(blocks[i], blocks[j]) for i in list(range(0, avg_blocks)) for j in list(range(i, avg_blocks))])

	keys.append({'size': key_size, 'hamming': hamm / key_size})

skeys = sorted(keys, key=lambda s: s['hamming'])
key_size=skeys[0]['size']
print("Key size: %d" % key_size)

# Transpose the buffer into key_size number
# 	eg: for ks: 4 and buff: '123456789' -> ['159', '26', '37', '48']
len_buff=len(buff)
blocks = [bytearray([buff[(key_size * j) + i] for j in range(0, math.ceil((len_buff - i) / key_size))]) for i in range(0, key_size)]

key = bytearray()
for i in list(range(0, len(blocks))):
	res = find_best_xor_match(blocks[i], 1)
	key += res[0]['mask']

print("Key: %s" % key)
print(key_encode(buff, key))