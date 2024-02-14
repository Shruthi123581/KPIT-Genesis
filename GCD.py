def gcd_euclid(a,b):
	if (b == 0):
		return a
	else:
		return gcd_euclid(b, a%b)

		
print(gcd_euclid(15, 4))