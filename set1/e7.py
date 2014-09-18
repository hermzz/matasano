#!/bin/env python

# 7. AES in ECB Mode
#
# The Base64-encoded content at the following location:
#
#     https://gist.github.com/3132853
#
# Has been encrypted via AES-128 in ECB mode under the key
#
#     "YELLOW SUBMARINE".
#
# (I like "YELLOW SUBMARINE" because it's exactly 16 bytes long).
#
# Decrypt it.
#
# Easiest way:
#
# Use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

import base64
from Crypto.Cipher import AES
from Crypto import Random

def run():
    buff = base64.b64decode(''.join([line.rstrip() for line in open('set1/e7.txt', 'r')]))

    key = b'YELLOW SUBMARINE'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB, iv)
    msg = cipher.decrypt(buff)

    print(msg)