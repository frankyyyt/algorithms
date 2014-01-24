# How many ways can we decode messages with the caesar cipher, recursively
# examples: "1012": ["JAB", "JL"], "933" => "ICC"

enc = "1012"

def numDecodings(enc):
	# we have 933
	# test if the input is a letter
	if not enc:
		return 1

	if int(enc[0]) > 0 and int(enc[0]) <= 26:
		print enc[0]
		numDecodings(enc[1:])
	else:
		numDecodings(enc[1:])

numDecodings(enc)
