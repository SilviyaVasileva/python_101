from math import gcd

def simplify_fractions(num):
	x = num[0]
	y = num[1]
	d = gcd(num[0], num[1])
	x = x // d
	y = y // d
	return (x,y)