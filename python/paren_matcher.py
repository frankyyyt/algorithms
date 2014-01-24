# check if there are the same number of ( and ) in a string
# '(x)' = true
# 'x)' = false

char = '('

def character_counter(string, char):
	count = 0
	if len(string) > 0:	
		print string[:1]
		count += character_counter(string[1:], char)
		if string[:1] == char:
			return count + 1
		else:
			return count
	else:
		return 0
print character_counter("((x))", "(")
print character_counter("((x))", ")")
