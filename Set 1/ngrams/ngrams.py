#!/usr/bin/env python

from __future__ import division
from math import log10
from os import path
import re

n_key = {1 : 'english_monograms.txt',
	 2 : 'english_bigrams.txt',
	 3 : 'english_trigrams.txt',
	 4 : 'english_quadgrams.txt',
	 5 : 'english_quintgrams.txt',
	 'word' : 'english_words.txt',
	 'words' : 'english_words.txt'
	}

this_dir = path.dirname(path.abspath(__file__))

class N_Gram(object):
	def __init__(self, n = 1):
		"loads log probabilities from frequencies in the n-gram's text file"
		filename = path.join(this_dir, n_key[n])
		self.ngrams = {}
		with open(filename, 'r') as f:
			for line in f.readlines():
				gram, freq = line.rstrip().split('\t')
				self.ngrams[gram] = int(freq)
		self.n = n
		total = sum(self.ngrams.itervalues())
		# calculate log probabilities
		for key, val in self.ngrams.items():
			self.ngrams[key] = log10(val / total)
		self.floor = log10(0.01/total)
	
	def score(self, text):
		"score text based on english n-gram frequencies"
		score = 0
		ngrams = self.ngrams
		for i in xrange(len(text) - self.n + 1):
			if text[i:i+self.n] in ngrams:
				score += ngrams[text[i : i+self.n]]
			else:
				score += self.floor
		return score


def p_to_odds(p):
	'converts a probablilty, p (a number between 0 and 1), to odds'
	return p / (1 - p) if p != 1 else float("inf")


if __name__ == '__main__':
	text = "Thisissomewonderfulenglishtextbrother".upper()
	gibb = "ipywetmzbcxiujgoweweboiubiuqwetykjhds".upper()
	print N_Gram().score(text)
	print N_Gram().score(gibb)
	
	