# XOR a byte array with a mask
def xor(orig, mask):
    return bytearray([a ^ b for a,b in zip(orig, mask)])

# Check if a bytearray only contains printable characters
# Range 32 to 126 are printable chars, 9, 10, and 13 are \n \r \t
def range_check(s):
    for i in s:
        if (i < 32 and (i != 9 and i != 10 and i != 13)) or i > 126:
            return False

    return True

# english character frequencies
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

class XOR_Match:
    def __init__(self, diff, mask, result):
        self.diff = diff
        self.mask = mask
        self.result = result

    def __str__(self):
        return "mask %s: %s; diff %0.4f" % (self.mask, self.result, self.diff)

# XORs a string with all the possible values and returns
# the top most english results
byte_range = list(range(0, 256))
def find_best_xor_match(orig, num=1):
    l_orig = len(orig)
    results = []
    for i in byte_range:
        result = xor(orig, bytearray([i] * l_orig))

        if range_check(result):
            results.append(XOR_Match(frequency_check(result), bytearray([i]), result))

    if not results:
        return []

    return sorted(results, key=lambda s: s.diff)[0:num]

import math
def key_encode(orig, key):
    kl = len(key)
    list_range = int(math.ceil(len(orig) / kl))

    return b''.join([xor(orig[i * kl:(i + 1) * kl], key) for i in list(range(0, list_range))])

def hamming(a, b):
    return sum([sum([int(j) for j in str(bin(c ^ d))[2:]]) for c,d in zip(a,b)])

def pad(text, length):
    diff = length - len(text)
    return bytearray(text) + bytearray([diff] * diff)

def unpad(text):
    last_char = text[-1:][0]
    text_length = len(text)

    padded = True
    for i in range(0, last_char):
        if text[text_length -1 - i] != last_char:
            padded = False

    if padded:
        text = text[:-last_char]

    return text

from Crypto.Cipher import AES
def ecb_encrypt(key, buff, iv):
    cipher = AES.new(key, AES.MODE_ECB, iv)
    return cipher.encrypt(buff)

def ecb_decrypt(key, buff, iv):
    cipher = AES.new(key, AES.MODE_ECB, iv)
    return cipher.decrypt(buff)

def cbc_decrypt(key, encoded, iv):
    plaintext = bytearray();
    number_of_chunks = int(math.ceil(len(encoded) / AES.block_size))

    for i in range(0, number_of_chunks):
        chunk = encoded[i * AES.block_size:(i + 1) * AES.block_size]

        # Decrypt the chunk and XOR it against the IV/encrypted chunk from last round
        decoded = xor(ecb_decrypt(key, chunk, iv), iv)

        plaintext = plaintext + decoded

        # Use the still encrypted chunk as the IV for the next round
        iv = chunk

    return unpad(plaintext)

def cbc_encrypt(key, plaintext, iv):
    decoded = bytearray();

    # Must pad input buffer to a multiple of AES.block_size first
    plaintext = pad(plaintext, len(plaintext) +(AES.block_size - (len(plaintext) % AES.block_size)))

    number_of_chunks = int(math.ceil(len(plaintext) / AES.block_size))

    for i in range(0, number_of_chunks):
        chunk = plaintext[i * AES.block_size:(i + 1) * AES.block_size]

        # XOR iv and chunk and encrypt
        cipher = ecb_encrypt(key, bytes(xor(chunk, iv)), iv)

        decoded = decoded + cipher

        # Use the encoded chunk as IV for next round
        iv = cipher

    return decoded