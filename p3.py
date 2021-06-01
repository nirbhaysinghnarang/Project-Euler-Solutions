import math
num = 600851475143


def is_prime(num):
	lim = int(math.sqrt(num))
	for i in range(2,lim):
		if(num%i==0):
			return False
	return True

def get__largest_prime_factors(num):
	lim = int(math.sqrt(num))
	pf = []
	for i in range(2,lim):
		if(num%i==0):
			if(is_prime(i)):
				pf.append(i)
	print(pf[-1])

get__largest_prime_factors(num)
