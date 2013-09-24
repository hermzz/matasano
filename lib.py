# XOR a byte array with a mask
def do_mask(orig, mask):
    i=0
    result = bytearray(len(orig))
    while i<len(orig):
        result[i] = orig[i] ^ mask[i]
        i += 1

    return result

# Check if a bytearray only contains printable characters
def range_check(s):
    for i in s:
        if (i < 32 and (i != 9 and i != 10 and i != 13)) or i > 126:
            return False

    return True

character_frequency = {
    ' ': 13.000,
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

from collections import Counter

# Return the distance of a string to standard english character frequencies
# The lower the number the more english the text is
def frequency_check(s):
    totals = {}
    length = len(s)

    totals = {}
    for (k,v) in Counter(s.lower()).items():
        totals[chr(k)] = (v / length) * 100

        if k not in character_frequency:
            character_frequency[k] = 0

    diff = 0
    for (k,v) in character_frequency.items():
        if k not in totals:
            totals[k] = 0

        diff += abs(totals[k] - character_frequency[k])

    return diff

# XORs a string with all the possible values and returns
# the top most english result
byte_range = list(range(0,256))
def find_best_xor_match(orig, num=1):
    results = []
    for i in byte_range:
        seed = bytearray(b'\x00')
        seed[0] = i
        result = do_mask(orig, seed * len(orig))

        if range_check(result):
            diff = frequency_check(result)
            results.append({'diff': diff, 'mask': seed, 'result': result})

    if not results:
        return []

    return sorted(results, key=lambda s: s['diff'])[0:num]