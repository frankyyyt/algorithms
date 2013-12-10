def convert_ones(n):
	lookup_dictionary = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6:"six", 7:"seven", 8:"eight", 9: "nine"}
	return lookup_dictionary[n]

def convert_teens(n):
	lookup_dictionary = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17: "seventeen", 18: "eighteen", 19:"nineteen"}
	return lookup_dictionary[n]

def convert_tens(n):
	lookup_dictionary = {2: "twenty", 3: "thirty", 4: "forty", 5:"fifty", 6:"sixty", 7:"seventy", 8: "eighty", 9:"ninety"}
	return lookup_dictionary[n]

def convert_hundreds(n):
	lookup_dictionary = {1: "one hundred", 2:"two hundred", 3:"three hundred", 4: "four hundred", 5: "five hundred", 6: "six hundred", 7: "seven hundred", 8: "eight hundred", 9: "nine hundred"}
	return lookup_dictionary[n]

def count_letters(number_name):
	letters = {}
	for letter in number_name:
		if letter in letters:
			letters[letter] += 1
		else:
			letters[letter] = 1
	if " " in letters:
		letters.pop(" ")
	if "-" in letters:
		letters.pop("-")
	return sum(letters.values())

n = 1000
letters_grand_total = 0
while n > 0:
	n_list = [int(i) for i in str(n)]
	length = len(n_list)
	number_name = ""
	if length == 4:
		number_name = "one thousand"
	elif length == 3:
		hundreds_n = n_list[0]
		tens_n = n_list[1]
		ones_n = n_list[2]
		if tens_n == 1:
			 number_name = convert_hundreds(hundreds_n) + " and " + convert_teens(int(str(tens_n) + str(ones_n)))
		elif tens_n == 0 and ones_n == 0:
			number_name = convert_hundreds(hundreds_n)
		elif tens_n == 0:
			number_name = convert_hundreds(hundreds_n) + " and " + convert_ones(ones_n)
		else:
			if ones_n == 0:
				number_name = convert_hundreds(hundreds_n) + " and " + convert_tens(tens_n)
			else:
				number_name = convert_hundreds(hundreds_n) + " and " + convert_tens(tens_n)  + "-" + convert_ones(ones_n)
	elif length == 2:
		tens_n = n_list[0]
		ones_n = n_list[1]
		if tens_n == 1:
			number_name = convert_teens(n)
		else:
			if ones_n == 0:
				number_name = convert_tens(tens_n)
			else:
				number_name = convert_tens(tens_n) + "-" + convert_ones(ones_n)
	elif length == 1:
		number_name = convert_ones(n)
	print number_name, count_letters(number_name)
	letters_grand_total += count_letters(number_name)
	n -= 1

print letters_grand_total
