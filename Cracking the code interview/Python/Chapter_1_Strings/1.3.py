# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string. 
# Hints: #53,0118

# Input: "Mr 3ohn Smith 13 Output: "Mr%203ohn%20Smith" Hints: #53,0118


def URLify(string):
	new_string = ''
	for char in string:
		if char == ' ':
			new_string += '%20'
		else:
			new_string += char
	return new_string

if __name__ == "__main__":
	string = 'Mr 3ohn Smith'
	print(URLify(string))