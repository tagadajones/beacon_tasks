#!/usr/bin/env python
#Task 1 : Caesar Cipher

from string import ascii_uppercase

#encrypted and uncrypted characters
encrypted = ascii_uppercase
plain = encrypted[3:]+encrypted[:3] #Shift list by 4