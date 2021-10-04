
def kadane(a):
	n = len(a)
	max_so_far = 0
	max_ending_here = 0
	for i in range(0, n):
		max_ending_here = max_ending_here + a[i]
		if (max_ending_here < 0):
			max_ending_here = 0
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here
	return max_so_far


def maxCircularSum(a):

	n = len(a)

	
	max_kadane = kadane(a)

	
	max_wrap = 0
	for i in range(0, n):
		max_wrap += a[i]
		a[i] = -a[i]

	
	max_wrap = max_wrap + kadane(a)

	
	if max_wrap > max_kadane:
		return max_wrap
	else:
		return max_kadane


a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print "Maximum circular sum is", maxCircularSum(a)

