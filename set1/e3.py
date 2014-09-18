#!/bin/env python

# 3. Single-character XOR Cipher
#
# The hex encoded string:
#
#       1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736,
#
# ... has been XOR'd against a single character. Find the key, decrypt
# the message.
#
# Write code to do this for you. How? Devise some method for "scoring" a
# piece of English plaintext. (Character frequency is a good metric.)
# Evaluate each output and choose the one with the best score.
#
# Tune your algorithm until this works.

from lib import find_best_xor_match

def run():
    match = find_best_xor_match(bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))[0]
    print(match)