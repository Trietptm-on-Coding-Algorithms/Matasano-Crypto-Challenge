#!/usr/bin/env python

# ########################################
# Convert hex to base64
# ########################################
# 
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# 
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# 
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
# 
# Cryptopals Rule:
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

from base64 import b16decode, b64encode

def hexto64(hex_str):
	'''converts hex string into base64 encoded string'''
	return b64encode(b16decode(hex_str.upper()))
	
if __name__ == "__main__":
	hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	print hexto64(hex_str)