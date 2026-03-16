"""
file in (Contains important items)

assume 1 word to start



[word][]
[word][symbol][Number]


xX_Slayer_Xx



"""


wordlist = ["matthew", "matt", "sisi", "spike", "zena", "spot", "hockey"]



symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "?", "<", ">"]

#Forwards, Backwards, Replace Special Letters

#Random Capitaliztion

#Functions
	#Add all words backwords

	#Add all words with letter replacement

	#Random

outlist = []


def Cap(w):
	outlist.append(w.upper())

def CopyList(wlist):
	for word in wlist:
		outlist.append(word)



def main():

	CopyList(wordlist)

	for word in wordlist:
		Cap(word)


	print(outlist)


main()