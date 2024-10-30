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
    	#	if i > 30:
    	#		break
    		
    
    	#print(frenchDict)
    	# test
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
#def searchDict(letters, frenchDict):
#	while True:
#		currentWord = q.get()
#		if len(currentWord) >= len(letters) + 1:
#			print("Current word is", currentWord)
#			if (len(currentWord) > 14):
#				print("Failed to find word!")
#				sys.exit()
#			if currentWord != 'DRACHME':
#				if isAMatch(currentWord, letters, frenchDict):
#					return currentWord
#		for letter in letters:
#			q.put(currentWord + letter)
#			

def isAMatch(currWord, letters, frenchDict):
	#if (currWord == "IMPORTE"):
	#	print('Debug!!')
		
	if (not (currWord in frenchDict)):
		#if (currWord == "IMPORTE"):
		#	print('FAILED!!')
		#	print(frenchDict)
		#	sys.exit()
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