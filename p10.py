import math
UPPER_BOUND = 2e6
def is_prime(num):
	lim = int(math.sqrt(num))
	for i in range(2,lim+1):
		if(num%i==0):
			return False
	return True
sum = 0
num = 2
while(num<UPPER_BOUND):
	if(is_prime(num)):
		print("NUMBER FOUND {}".format(num))
		sum+=num
		print("SUM UPDATED TO {}".format(sum))
	num+=1
print(sum)
