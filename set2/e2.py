#!/bin/env python

# Implement CBC mode
# CBC mode is a block cipher mode that allows us to encrypt
# irregularly-sized messages, despite the fact that a block cipher
# natively only transforms individual blocks.
#
# In CBC mode, each ciphertext block is added to the next plaintext
# block before the next call to the cipher core.
#
# The first plaintext block, which has no associated previous
# ciphertext block, is added to a "fake 0th ciphertext block" called
# the initialization vector, or IV.
#
# Implement CBC mode by hand by taking the ECB function you wrote
# earlier, making it encrypt instead of decrypt (verify this by
# decrypting whatever you encrypt to test), and using your XOR
# function from the previous exercise to combine them.
#
# The file here is intelligible (somewhat) when CBC decrypted against
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

import base64
from lib import cbc_decrypt

def run():
    key = b'YELLOW SUBMARINE'
    buff = base64.b64decode(''.join([line.rstrip() for line in open('set2/e2.txt', 'r')]))
    iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    decoded = cbc_decrypt(key, buff, iv)

    print(decoded.decode('ascii'))