"""
Generates ~ 1.5 Billion Passwords

useage:

gendict <file>

"""
from pathlib import Path

wordlist = ["canada"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "?", "<", ">", "~"]

midlist = []

outlist = []

"""=================================================
	Rules
================================================="""

def SymNumSym(w):
	for s1 in symbols:
		w1 = w + s1
		for i in range (0,10000):
			w2 = w1
			w2 += str(i)
			for s2 in symbols:
				w3 = w2 + s2
				outlist.append(w3)

def NumSymSymSym(w):
	for i in range (0,10000):
		w1 = w
		w1 += str(i)
		for s1 in symbols:
			w2 = w1 + s1
			for s2 in symbols:
				w3 = w2 + s2
				for s3 in symbols:
					w4 = w3 + s3
					outlist.append(w4)
def NumSymSym(w):
	for i in range (0,10000):
		w1 = w
		w1 += str(i)
		for s1 in symbols:
			w2 = w1 + s1
			for s2 in symbols:
				w3 = w2 + s2
				outlist.append(w3)

def SymSymWordNum(w):
	for s1 in symbols:
		w1 = s1 + w
		for s2 in symbols:
			w2 = s2 + w1
			for i in range (0, 10000):
				w3 = w2
				w3 += str(i)
				outlist.append(w3)

def WordSymSymNum(w):
	for s1 in symbols:
		w1 = w + s1
		for s2 in symbols:
			w2 = w1 + s2
			for i in range (0, 10000):
				w3 = w2
				w3 += str(i)
				outlist.append(w3)

def SymSymSymNum(w):
	for s1 in symbols:
		w1 = s1 + w
		for s2 in symbols:
			w2 = s2 + w1
			for s3 in symbols:
				w3 = s3 + w2
				for i in range (0, 10000):
					w4 = w3
					w4 += str(i)
					outlist.append(w4)

def NumSym(w):
	for i in range (0,10000):
		w1 = w
		w1 += str(i)
		for sym in symbols:
			w2 = w1 + sym
			outlist.append(w2)

def SymNum(w):
	for sym in symbols:
		w2 = w + sym
		for i in range (0,10000):
			w3 = w2
			w3 += str(i)
			outlist.append(w3)

"""
	Basics
"""
def BasicSym(w):
	for sym in symbols:
		outlist.append(w + sym)

def BasicSymSym(w):
	for sym in symbols:
		w1 = w + sym
		for sym in symbols:
			w2 = w1 + sym
			outlist.append(w2)

def BasicSymSymSym(w):
	for sym in symbols:
		w1 = w + sym
		for s1 in symbols:
			w2 = w1 + s1
			for s2 in symbols:
				w3 = w2 + s2
				outlist.append(w3)

def SymWord(w):
	for sym in symbols:
		w1 = sym + w 
		outlist.append(w1)

def SymSymWord(w):
	for s1 in symbols:
		w1 = s1 + w
		for s2 in symbols:
			w2 = s2 + w1
			outlist.append(w2)

def SymSymSymWord(w):
	for s1 in symbols:
		w1 = s1 + w
		for s2 in symbols:
			w2 = s2 + w1
			for s3 in symbols:
				w3 = s3 + w2
				outlist.append(w3)

def BasicNum(w):
	for i in range (0,10000):
		word = w
		word += str(i)
		outlist.append(word)

"""=================================================
	Core Structure
================================================="""

def CopyList(wlist):
	for word in wlist:
		midlist.append(word)
		midlist.append(word.capitalize())

		outlist.append(word)
		outlist.append(word.capitalize())


def main(argc = None, argv = None):

	CopyList(wordlist)

	cnt = 0

	for word in midlist:
		cnt += 1
		#print(f"Generating {cnt}/{len(midlist)}")
		BasicNum(word)
		BasicSym(word)
		BasicSymSym(word)
		BasicSymSymSym(word)

		SymWord(word)
		SymSymWord(word)
		SymSymSymWord(word)

		SymNum(word)
		NumSym(word)
		SymNumSym(word)

		WordSymSymNum(word)
		SymSymWordNum(word)
		NumSymSym(word)

		#SymSymSymNum(word)
		#NumSymSymSym(word)


	for password in outlist:
		print(password)
	#print("list length: ", len(outlist))


main(argc=None,argv=None)
