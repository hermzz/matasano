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
from Crypto import Random
from Crypto.Cipher import AES
from lib import ecb_decrypt

def run():
    buff = base64.b64decode(''.join([line.rstrip() for line in open('set1/e7.txt', 'r')]))
    print(ecb_decrypt(b'YELLOW SUBMARINE', buff, Random.new().read(AES.block_size)))