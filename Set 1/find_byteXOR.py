#!/usr/bin/env python

# #############################
# Detect single-character XOR
# #############################
# 
# One of the 60-character strings in "4.txt" has been encrypted by single-character XOR.
# 
# Find it.
# 
# (Your code from #3 should help.)

from byteXOR import crack_byteXOR, byte_xor
from ngrams.ngrams import N_Gram

def detect_byteXOR(candidates, n=1):
	ngram = N_Gram(n)
	best = max((c for c in candidates), key=lambda x: crack_byteXOR(x, ngram)[1])
	print crack_byteXOR(best, ngram)
	return best

if __name__ == "__main__":
	with open("4.txt") as f:
		data = f.read().split('\n')
	print detect_byteXOR(data)