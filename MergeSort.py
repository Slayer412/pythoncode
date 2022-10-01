

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, left, m, right):
	n1 = m - left + 1
	n2 = right - m

	# create temp arrays
	LEFT = [0] * (n1)
	RIGHT = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		LEFT[i] = arr[left + i]

	for j in range(0, n2):
		RIGHT[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if LEFT[i] <= RIGHT[j]:
			arr[k] = LEFT[i]
			i += 1
		else:
			arr[k] = RIGHT[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = LEFT[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = RIGHT[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, left, right):
	if left < right:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = left+(right-left)//2

		# Sort first and second halves
		mergeSort(arr, left, m)
		mergeSort(arr, m+1, right)
		merge(arr, left, m, right)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i]),

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i]),

# This code is contributed by DSP
