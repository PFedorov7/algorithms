def quickSort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quickSort(less) + [pivot] + quickSort(greater)
		
print(quickSort([4,6,7,32,4,5,9,8,77]))