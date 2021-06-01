def pythagoreanTriplets():
	c, m = 0, 2
	while True:
		for n in range(1, m) :
			a = m * m - n * n
			b = 2 * m * n
			c = m * m + n * n
			if(a+b+c==1000):
				print(a*b*c)
				break
		m+=1

pythagoreanTriplets()
