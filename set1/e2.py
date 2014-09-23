#!/bin/env python

# 2. Fixed XOR
#
# Write a function that takes two equal-length buffers and produces
# their XOR sum.
#
# The string:
#
#  1c0111001f010100061a024b53535009181c
#
# ... after hex decoding, when xor'd against:
#
#  686974207468652062756c6c277320657965
#
# ... should produce:
#
#  746865206b696420646f6e277420706c6179

from lib import xor

def run():
    orig = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    mask = bytes.fromhex('686974207468652062756c6c277320657965')
    check = bytes.fromhex('746865206b696420646f6e277420706c6179')

    result = xor(orig, mask)

    print(check)
    print(result)
    print(check == result)