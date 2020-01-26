def recurseMax(elem):
	maxValue = elem[0]
	if(len(elem) == 0):
		return 0
	pos = 0
	for single in elem:
		if(maxValue < single):
			maxValue = recurseMax(elem[pos:])
		pos += 1
	return maxValue

print(recurseMax([7,11,2,4,5,99]))