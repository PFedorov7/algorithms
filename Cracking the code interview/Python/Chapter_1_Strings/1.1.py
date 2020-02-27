### Is Unique: Implement an algorithm to determine if a string has all unique characters. 
### What if you cannot use additional data structures?
### Hints: #44, #117, #132
def isUnique_1(string):
	unique_list = []
	for char in ''.join(string.split()):
		if char in unique_list:
			continue
		else:
			unique_list.append(char)
	return len(unique_list)

def isUnique_2(string):
	return len(set(list(string)))

def isUnique_3(string):
	cnt = 0
	chars = sorted(list(string))
	for index, char in enumerate(chars):
		if index == len(chars) - 1:
			cnt += 1
			break
		if char == chars[index + 1]:
			continue
		else:
			cnt += 1
	return cnt

def isUnique_4(string):
	unique = {}
	for char in list(string):
		unique[char] = None
	return len(unique.keys())



if __name__ == "__main__" :

	string = 'asdafghdgjkhlllkknkn'
	print(isUnique_1(string))
	print(isUnique_2(string))
	print(isUnique_3(string))
	print(isUnique_4(string))


