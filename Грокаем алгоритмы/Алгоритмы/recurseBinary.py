def recurseBinary(sorted_list, value):
	midIndex = len(sorted_list) / 2
	if(sorted_list[midIndex] == value):
		return midIndex
	if(value > sorted_list[midIndex]):
		return midIndex + recurseBinary(sorted_list[midIndex:], value)
	else:
		return recurseBinary(sorted_list[:midIndex], value)

print(recurseBinary([0,1,2,3,4,5,6,7,8,9], 5))