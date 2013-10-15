import random

def sortStringsByLength():
	description = "Sort an array of strings by the length of the string in Python"
	print description

	l = ['carefully', 'care', 'tub', 'sneeze', 'a', 'far']
	print l
	l = [(len(s), s) for s in l]
	l.sort()
	l = [i[1] for i in l]
	print l

def reverseString():
	description = "Write an iterative function to reverse a string. Do the same thing as a recursive function."

	s = "tarp"
	s = list(s)
	s.reverse()
	s = "".join(s)
	

def asciiCharacters():
	description = "Write a for loop that prints out the ascii characters in a string s"
	print description

	s = "For I dipt into the future, far as human eye could see..."
	t = []
	for l in s:
		t.append(ord(l))
	print t
	print ' '
	print map(ord, s)
	print ' '
	print [ord(l) for l in s]

def sortDict():
	description = "for loop that prints dict items in ascending order"
	print description

	d = {"coffee": 5, "tea": 9, "milkshake": 4}

	l = d.keys()
	l.sort()
	for i in l:
		print i, d[i]

def primes():
	description = "Print out the prime numbers between 1 and 100.:"
	print description

	n = 1
	while n <= 100:
		print n
		i = 2
		while i <= n:
			if n % i == 0:
				print i
				n += 1
		n += 1


def reverseWordsInPlace():
	description = "Reverse a string, in place (not in place yet)"
	print description

	s = "I must not fear fear is the mind killer"
	sn = ''
	i = 1
	j = 0
	for l in s:
		print "at", i
		if l == ' ' or i == len(s): 
			print 'word detected from', j, 'to', i, s[j:i]
			sn = s[j:i] + sn
			j = i
		i += 1
	print sn

def missingNumber():
	description = "Suppose you have an array of 99 numbers. The array contains the digits 1 to 100 with one digit missing. "
	print description
	r = random.randint(0, 100)
	l = range(1, 100)
	del l[r+1]
	print r, l

def palindrome():
	description = "Write a function that takes an integer and returns the smallest number that is greater than the given number which is a palendrome."
	print description
	input = 338

	stop = False
	while stop == False:
		input += 1
		if str(input) == str(input)[::-1]: 
			stop = True
	else:
		print input

def tokenize_string():
	description = "Write a function, tokenize_string(input_string, delimiter_list) that returns a list of strings that are separated by the delimiters."
	print description
	
	s = " string,to toke,nize uhh yea"
	s = s.rstrip()
	s = s.lstrip()
	delimeter = ','
	result = list()

	last = 0
	for i, l in enumerate(s):
		if l == delimeter: 
			result.append(s[last:i])
			last = i
		if i+1 == len(s):
			result.append(s[last:i+1])
		
	print result

#sortStringsByLength()
#reverseString()
#asciiCharacters()
#sortDict()
#primes()
#reverseWordsInPlace()
#missingNumber()
#palindrome()
tokenize_string()