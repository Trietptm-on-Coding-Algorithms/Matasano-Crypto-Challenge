#!/usr/bin/env python

# #######################
# Single-byte XOR cipher
# #######################
# 
# The hex encoded string:
# 
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
# 
# You can do this by hand. But don't: write code to do it for you.
# 
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency
# is a good metric. Evaluate each output and choose the one with the best score.

from base64 import b16decode, b16encode
from ngrams.ngrams import N_Gram

def byte_xor(data, key):
	'xor string of data with a single-byte key'
	if isinstance(key, str): key = ord(key)
	return ''.join(chr(ord(c) ^ key) for c in data)

def crack_byteXOR(encoded, ngram=N_Gram(), verbose=False):
	encoded = b16decode(encoded.upper())
	max_score = -float('inf')
	for key in xrange(256):
		decoded = byte_xor(encoded, key)
		score = ngram.score(decoded.upper())
		if verbose: print key, score, decoded
		if score > max_score:
			max_score = score
			best = decoded
			best_key = key
	return best, max_score, best_key

if __name__ == "__main__":
	data = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	ngram = N_Gram()
	print crack_byteXOR(data, ngram)