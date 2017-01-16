#!/usr/bin/env python

# ########################
# Break repeating-key XOR
# ########################
#
# It is officially on, now.
# This challenge isn't conceptually hard, but it involves actual error-prone
# coding. The other challenges in this set are there to bring you up to speed.
# This one is there to qualify you. If you can do this one, you're probably
# just fine up to Set 6.
#
# There's a file here. It's been base64'd after being encrypted with
# repeating-key XOR.
#
# Decrypt it.
#
# Here's how:
#
# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
# Write a function to compute the edit distance/Hamming distance between two
# strings. The Hamming distance is just the number of differing bits. The
# distance between:
#
# this is a test
#
# and
#
# wokka wokka!!!
#
# is 37. Make sure your code agrees before you proceed.
#
# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
# KEYSIZE worth of bytes, and find the edit distance between them. Normalize
# this result by dividing by KEYSIZE.
#
# The KEYSIZE with the smallest normalized edit distance is probably the key.
# You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4
# KEYSIZE blocks instead of 2 and average the distances.
#
# Now that you probably know the KEYSIZE: break the ciphertext into blocks of
# KEYSIZE length.
#
# Now transpose the blocks: make a block that is the first byte of every
# block, and a block that is the second byte of every block, and so on.
#
# Solve each block as if it was single-character XOR. You already have code
# to do this.
#
# For each block, the single-byte XOR key that produces the best looking
# histogram is the repeating-key XOR key byte for that block. Put them together
# and you have the key.

# This code is going to turn out to be surprisingly useful later on. Breaking
# repeating-key XOR ("Vigenere") statistically is obviously an academic
# exercise, a "Crypto 101" thing. But more people "know how" to break it than
# can actually break it, and a similar technique breaks something much more
# important.
#
# No, that's not a mistake.
# We get more tech support questions for this challenge than any of the other
# ones. We promise, there aren't any blatant errors in this text. In
# particular: the "wokka wokka!!!" edit distance really is 37.

from base64 import b64decode
from numpy import mean
from byteXOR import crack_byteXOR
from repeating_key_xor import rep_xor
from itertools import izip_longest


def bin_hamm_dist(a, b):
    'Calculates the Hamming distance between two binary strings'
    if len(a) != len(b):
        raise ValueError("Hamming distances can only be computed for values "
                         "of equal length!\n len a = %d, len b = %d\na = %s"
                         "\nb = %s" % (len(a), len(b), a, b))
    dist = 0
    for i in xrange(len(a)):
        x = ord(a[i]) ^ ord(b[i])
        while x != 0:
            dist += 1
            x &= x - 1
    return dist


def crack_xor(data):
    'cracks repeating key xor encryption'
    key_len = get_key_lengths(data)[0]
    grid = transpose(chunker(data, key_len))
    key = ''.join([chr(crack_byteXOR(''.join(row))[2]) for row in grid])
    return key_len, key, rep_xor(data, key)


def transpose(table):
    return tuple(izip_longest(*table, fillvalue=''))


def chunker(seq, size):
    'breaks a sequence into chunks of length "size"'
    return tuple(seq[pos:pos + size] for pos in xrange(0, len(seq), size))


def get_key_lengths(data, max_key_len=40):
    '''Tries various key lengths and returns list of candidates sorted by
    Hamming weights'''
    max_n = min(max_key_len, len(data) // 2)

    def calc_key_hamm(n):
        return mean([bin_hamm_dist(part[:n], part[n:]) / float(n * 8)
                    for part in chunker(data, n * 2)
                    if len(part) == n * 2])
    return sorted((n for n in xrange(1, max_n + 1)), key=calc_key_hamm)

if __name__ == "__main__":
    # a = "this is a test"
    # b = "wokka wokka!!!"
    # print "Binary Hamming Distance: %d" % bin_hamm_dist(a, b)

    # with open('XORAlice.txt', 'r') as f:
    #     alice = f.read()[:5000] # Alice in Wonderland XORed with "WONDERLAND"
    # print crack_xor(alice)

    with open('6.txt', 'r') as f:
        enc = b64decode(f.read())
    print crack_xor(enc)
