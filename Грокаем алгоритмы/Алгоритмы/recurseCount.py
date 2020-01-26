def recurseCount(elem):
	if(len(elem) == 1):
		return 1
	else:
		return 1 + recurseCount(elem[0:-1:])

print(recurseCount([1,2,3,4,5,7,8,9]))