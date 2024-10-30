import unicodedata
import queue
import sys

letters = "AEFLMOPRT"
root = "P"

q = queue.Queue()
q.put(root)

def main():
    with open('dictionary.txt') as reader:
    	frenchDict = set()
    	i = 0
    	for row in reader:
    		preprocess(row, frenchDict)
    		i = i + 1

    	if (not "100" in frenchDict):
    		print('ERROR!!! Missing word')
    		sys.exit()
    	word = searchDict(letters, frenchDict)
    	print(word)

def searchDict(letters, frenchDict):
	for word in frenchDict:
		if word[0] == root:
			if (wordHasAllLetters(word)):
				if wordHasOnlyLetters(word):
					return word

def wordHasAllLetters(word):
	for character in letters:
		if (not (character in word)):
			return False
	return True

def wordHasOnlyLetters(word):
	for character in word:
		if (not(character in letters)):
			return False
	return True

def isAMatch(currWord, letters, frenchDict):
		
	if (not (currWord in frenchDict)):
		return False
	for letter in letters:
		if (not currWord.count(letter)):
			return False
	return True
			

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')		
	
def preprocess(row, set):
	unaccented = strip_accents(row.strip())
	set.add(unaccented.upper())

main()
