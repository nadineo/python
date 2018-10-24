import re
from re import sub

class RLEString(object):

	def __init__(self, string):
		#check if the string is valid
		if not re.match('^[a-zA-Z]+$',string):
			raise ValueError("Text has to consist of alphabetic characters (a-zA-Z))")
		else:
			self.__mystring = string
			self.__iscompressed = False


	def compress(self):
		#compress internal string
		#substitute function of regular expression in python
		#the (.)\1* is the syntax for finding backreferences -> finding all equal charactes in a row
		#the sub() function substitutes for example: EEEEE -> 5E
		if self.__iscompressed:
			raise RuntimeError("Mystring is already compressed!")
		else:
			self.__mystring = sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), self.__mystring)
			self.__iscompressed = True
			return self.__mystring
	

	def decompress(self):
		#substitute function of regular expression in python
		#the caputuring groups (\d+ = decimal digit group(1) and (\D = any non digit character group(2)) has
		#to be placed in the resulting "new" mystring. group(0) would result in any kind of: (5E), group(1): 5, group(2): E
		#decompressed is the result: EEEEE
		#the sub() function, substitutes 5E with E*(int)5 ->  EEEEE
		if not self.__iscompressed:
			raise RuntimeError("Mystring is already decompressed!")
		else:
			self.__mystring = sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), self.__mystring)
			self.__iscompressed = False
			return self.__mystring


	def iscompressed(self):
		if self.__iscompressed:
			return self.__iscompressed

	def __str__(self):
		return self.__mystring
