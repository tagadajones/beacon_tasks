#!/usr/bin/env python
#Task 1 : Caesar Cipher

from string import ascii_uppercase

#encrypted and uncrypted characters
encrypted = ascii_uppercase
plain = encrypted[3:]+encrypted[:3] #Shift list by 4

def encrypt(text):
	"""Caesar cipher encrypting
	text : plain text to encrypt
	returns : encrypted text
	"""
	t = []
	for l in text.upper():
		if l in plain:	t.append(encrypted[plain.index(l)])		#encrypt letter if it's not punctuation 
		else:			t.append(l)								#else: append punctuation
	return  ''.join(t)