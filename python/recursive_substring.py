# Given the string "For I dipt into the future...", write a recursive algorithm that finds the substring "future".

sentence = "For I dipt into the future..."
substring = "future"

# Write the base case
# Move towards the base case 
# Call function recursively

def substringer(sentence, substring):
	found = False
	if sentence == "":
		return False
	substring_length = len(substring)
	if sentence[:substring_length] == substring:
		return True 

	found = substringer(sentence[1:], substring)
	return found
print substringer(sentence, substring)
