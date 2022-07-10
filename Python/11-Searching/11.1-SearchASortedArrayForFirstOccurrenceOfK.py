# Similar LC: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def search_first_k(arr, k):
	left, right = 0, len(arr) - 1
	result = -1		# -1 being default value if k is not in the array
	
	while left <= right:
		mid = left + (right - left) // 2
		
		if k == arr[mid]:
			result = mid
			right = mid - 1
		elif k < arr[mid]:
			right = mid - 1
		else:
			left = mid + 1
	
	return result
	
