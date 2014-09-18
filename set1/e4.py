#!/bin/env python

# 4. Detect single-character XOR
#
# One of the 60-character strings at:
#
#  https://gist.github.com/3132713
#
# has been encrypted by single-character XOR. Find it. (Your code from
# 3 should help.)

from lib import find_best_xor_match

def run():
    matches = [item for sublist in [find_best_xor_match(bytes.fromhex(line.rstrip()), 1) for line in open('set1/e4.txt', 'r')] for item in sublist]

    print("Found %d total possible matches" % len(matches))

    sorted_matches = sorted(matches, key=lambda s: s.diff)

    for match in sorted_matches[0:40]:
        print(match)