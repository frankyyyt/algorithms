# Given the string "this, is, a, list", return a list of string split by the delimited ",". Use a recursive function

sentence = "this, is, a, list"
delimiter = ","

def tokenizer(sentence, delimiter):
	if sentence == "":
		return 0

	if sentence[0] == delimiter:
		count = 1
	else:
		count = 0
	count += tokenizer(sentence[1:], delimiter)
	return count

print tokenizer(sentence, delimiter)
