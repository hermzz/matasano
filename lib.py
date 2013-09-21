def do_mask(orig, mask):
	i=0
	result = bytearray(len(orig))
	while i<len(orig):
		result[i] = orig[i] ^ mask[i]
		i += 1

	return result