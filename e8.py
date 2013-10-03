#!/bin/env python

# 8. Detecting ECB
#
# At the following URL are a bunch of hex-encoded ciphertexts:
#
#    https://gist.github.com/3132928
#
# One of them is ECB encrypted. Detect it.
#
# Remember that the problem with ECB is that it is stateless and
# deterministic; the same 16 byte plaintext block will always produce
# the same 16 byte ciphertext.

buffers = [bytes.fromhex(line.rstrip()) for line in open('e8.txt', 'r')]

totals = {}
for (line, buff) in enumerate(buffers):
	lbuff = int(len(buff) / 16)
	for i in list(range(0, lbuff)):
		for j in list(range(i+1, lbuff)):
			if buff[i * 16:(i + 1) * 16] == buff[j * 16:(j + 1) * 16]:
				if line not in totals:
					totals[line] = 0
				totals[line] += 1

sort = sorted(totals)
print("Line %d looks suspicious" % (sort[0]))
print(buffers[sort[0]])