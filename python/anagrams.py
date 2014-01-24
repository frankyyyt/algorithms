'''
Input - List<String> ["star", "rats", "ice", "cie", "arts"] 
print all anagrams in buckets: 
["star", "rats", "arts"] 
["ice", "cie"] 
'''

input = ["star", "rats", "ice", "cie", "arts"] 

def is_anagram(word1, word2):
	word1 = sorted(list(word1))
	word2 = sorted(list(word2))

	if word1 == word2:
		return True
	else:
		return False

is_anagram("star", "rats") # should return true

master = {}

for word_1 in input:
	for word_2 in input:
		if word_1 != word_2:
			print word_1, word_2, is_anagram(word_1, word_2)
