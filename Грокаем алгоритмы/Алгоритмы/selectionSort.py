def findSmallest(arr):
	smallest_value = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if(arr[i] < smallest_value):
			smallest_value = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	newArr = []
	for i in range (len(arr)):
		smallest = findSmallest(arr)
		newArr.append((arr.pop(smallest)))
	return newArr

testlist = [1,7,'g',2,'a']
testlist = [1,7,4,2,3]
print(selectionSort(testlist))
