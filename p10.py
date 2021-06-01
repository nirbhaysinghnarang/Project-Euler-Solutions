import math
UPPER_BOUND = 2e6


def is_prime(num):
	lim = int(math.sqrt(num))
	for i in range(2,lim):
		if(num%i==0):
			return False
	return True
sum = 0
num = 1
while(num<UPPER_BOUND):
	if(is_prime(num)):
		sum+=num
	num+=1
print(sum)
