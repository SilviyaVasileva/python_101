def sort_fraction(arr):
	res = []
	for num in arr:
		i = ((num),num[0]/num[1])
		res.append(i)

	sorted_list = sorted(res, key = lambda tup: tup[1])
	
	result = []
	for n in sorted_list:
		result.append(n[0])
	return result