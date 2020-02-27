### Check Permutation: Given two strings, write a method
### to decide if one is a permutation of the other.
### Hints: f t , #84, #122, #131


def permutation_1(string_1, string_2):
	if len(string_1) != len(string_2):
		return 0

	sorted_string_1 = sorted(list(string_1))
	sorted_string_2 = sorted(list(string_2))

	for i in range(len(string_1)):
		if sorted_string_1[i] != sorted_string_2[i]:
			return 0
	return 1

def permutation_2(string_1, string_2):
	if hash(''.join(sorted(list(string_1)))) == hash(''.join(sorted(list(string_2)))):
		return 1
	return 0


if __name__ == "__main__":
	string_1 = 'worldr'
	string_2 = 'worldr'
	print(permutation_1(string_1, string_2))
	print(permutation_2(string_1, string_2))
