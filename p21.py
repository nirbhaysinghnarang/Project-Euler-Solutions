import math
def get_divisors(n):
	divisors = [1]
	for i in range(2,n):
		if(n%i==0):
			divisors.append(i)
	return divisors

def are_amicable(n1,n2):
	if sum(get_divisors(n1))==n2:
		if sum(get_divisors(n2))==n1:
			return True
	return False

sum = 0
for i in range(1,10001):
	for j in range(1,10001):
		if(i!=j):
			if(are_amicable(i,j)):
				sum+=i
				sum+=j

print(sum)
