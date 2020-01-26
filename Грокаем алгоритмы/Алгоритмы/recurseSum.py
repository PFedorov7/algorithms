def recurseSum(elements):
	if(len(elements) == 0):
		return 0
	else:
		current = elements.pop()
		return current + recurse_sum(elements)

print(recurse_sum([1]))