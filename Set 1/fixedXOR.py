#!/usr/bin/env python

# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# 
# If your function works properly, then when you feed it the string:
# 
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 
# 686974207468652062756c6c277320657965
# ... should produce:
# 
# 746865206b696420646f6e277420706c6179

from base64 import b16decode, b16encode

def fixedXOR(data, key):
	'''XOR encryption of <data> with <key>. Both arguments are strings encoded in hex.
	<data> and <key> must be same length in bytes.'''
	if len(data) != len(key):
		raise ArgumentError, "data and key must be of same length in bytes."
		return
	data = b16decode(data.upper())
	key = b16decode(key.upper())
	return ''.join([chr(ord(data[i]) ^ ord(key[i])) for i in xrange(len(data))])
	
if __name__ == "__main__":
	data = "1c0111001f010100061a024b53535009181c"
	key = "686974207468652062756c6c277320657965"
	res = b16encode(fixedXOR(data, key))
	print res
	if res == "746865206b696420646f6e277420706c6179".upper():
		print "Test Pass"
	else:
		print "TEST FAIL"