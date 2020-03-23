
def sort(interable = None, ascending = True, keY = None):
	if type(interable) is list:
		if interable == []:
			return interable
		if type(interable[0]) is int:
			interable.sort(reverse = not ascending)
			return interable
		if type(interable[0]) is dict:
			if keY is None:
				key_temp = []
				for k in interable[0].keys():
					key_temp.append(k)
				keY = key_temp[0]
			res = sorted(interable, key=lambda k: k[keY])
			if not ascending:
				return res
			return res[::-1]
	return [] #interable