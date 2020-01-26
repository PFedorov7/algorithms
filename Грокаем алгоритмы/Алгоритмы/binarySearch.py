def binarySearch(sorted_list, value):
	low = 0 #List first elem
	high = len(sorted_list) - 1 #List last elem
	while low <= high :
		mid = (low + high) / 2 #rounding down
		guess = sorted_list[mid]
		if guess == value:
			return mid
		if guess < value: 
			low = mid + 1
		else:
			high = mid - 1
	return None

	
print(binarySearch([1,2,'m',4,5], 'm'))
print(binarySearch([1,2,3,4,5], 4))
