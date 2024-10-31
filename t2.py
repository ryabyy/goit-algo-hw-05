def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	iterations = 0

	while low <= high:
		iterations += 1
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			return (iterations, mid)
	if arr[mid] > x:
		return (iterations, mid)
	else:
		return (iterations, -1)

arr = [2, 3, 4, 10, 40]
x = 4.1
result = binary_search(arr, x)
if result[1] != -1:
	if x == arr[result[1]]:
		print(f"The exact number, {arr[result[1]]}, is found at position {result[1]} after {result[0]} iterations.")
	else:
		print(f"The number's upper bound, {arr[result[1]]}, is found at position {result[1]} after {result[0]} iterations.")
else:
	print("The element or its upper bound is not found in the array")