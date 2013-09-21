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

from lib import do_mask

character_frequency = {
    'e': 12.702,
    't': 9.056,
    'a': 8.167,
    'o': 7.507,
    'i': 6.966,
    'n': 6.749,
    's': 6.327,
    'h': 6.094,
    'r': 5.987,
    'd': 4.253,
    'l': 4.025,
    'c': 2.782,
    'u': 2.758,
    'm': 2.406,
    'w': 2.360,
    'f': 2.228,
    'g': 2.015,
    'y': 1.974,
    'p': 1.929,
    'b': 1.492,
    'v': 0.978,
    'k': 0.772,
    'j': 0.153,
    'x': 0.150,
    'q': 0.095,
    'z': 0.074
}

def range_check(s):
    for i in s:
        if i < 32 or i > 126:
            return False

    return True

def frequency_check(s, f):
    totals = {}
    length = len(s)

    for i in s:
        if not i in totals:
            totals[chr(i)] = 0

        totals[chr(i)] += 1

    for (k,v) in totals.items():
        totals[k] = v / length

    diff = 0
    for (k,v) in f.items():
        if k not in totals:
            totals[k] = 0

        diff += abs(totals[k] - f[k])

    return diff


orig = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

results = []
for i in list(range(0,256)):
    seed = bytearray(b'\x00')
    seed[0] = i
    result = do_mask(orig, seed * len(orig))

    if range_check(result):
        diff = frequency_check(result, character_frequency)
        results.append({'diff': diff, 'mask': i, 'result': result})

s = sorted(results, key=lambda s: s['diff'])
print("mask %s: %s; diff %0.4f" % (s[0]['mask'], s[0]['result'], s[0]['diff'])) 