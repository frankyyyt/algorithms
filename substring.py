# substring function

string = "I must not fear"

substring = "fear"

length = len(substring)
i = 0
for l in string:
	if string[i:length+i] == substring:
		print "I found it at position", i
	i += 1