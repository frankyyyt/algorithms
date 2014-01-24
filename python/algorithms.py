import random

def sort_strings_by_length():
	description = "Sort an array of strings by the length of the string in Python"
	print description

	l = ['carefully', 'care', 'tub', 'sneeze', 'a', 'far']
	print l
	l = [(len(s), s) for s in l]
	l.sort()
	l = [i[1] for i in l]
	print l

def reverse_string():
	description = "Write an iterative function to reverse a string."

	s = "tarp" # starting variable
	result = "" # empty result string

	n = 0 # place marker
	start = 0 # place marker

	while s[n:] != "": # while the string, from place marker to end, is not empty
		while s[n:] != "" and s[n] != " ": # AND while the place marker value is not a space
			n += 1 							# move place marker forward
			result = s[start:n] + result # old marker to new marker
			print result, "start=", start, "n=", n
			start = n
	
def reverse_string_recursive(s='tarp'):
	description = "Write a recursive function to reverse a string."
	print s
	if s == "":
		return s
	else:
		return reverse_string_recursive(s[1:]) + s[0]

	pass

def ascii_characters():
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

def sort_dict():
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


def reverse_words_in_place():
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

def missing_number():
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

#print reverse_string_recursive()
primes()
