from simply_fraction import simplify_fractions

def collect_fraction(num1, num2):
	x1 = num1[0]
	x2 = num2[0]
	y1 = num1[1]
	y2 = num2[1]

	first_num = x1 * y2 + x2 * y1
	second_num = y2 * y1

	return simplify_fractions((first_num,second_num))

