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

from lib import do_mask, range_check, frequency_check

orig = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

results = []
for i in list(range(0,256)):
    seed = bytearray(b'\x00')
    seed[0] = i
    result = do_mask(orig, seed * len(orig))

    if range_check(result):
        diff = frequency_check(result)
        results.append({'diff': diff, 'mask': i, 'result': result})

s = sorted(results, key=lambda s: s['diff'])
print("mask %s: %s; diff %0.4f" % (s[0]['mask'], s[0]['result'], s[0]['diff'])) 