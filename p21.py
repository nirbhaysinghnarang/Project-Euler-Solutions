import math
# def get_divisors(n):
# 	divisors = []
# 	for i in range(1,int(math.sqrt(n) + 1)):
# 		if(n%i==0):
# 			divisors.append(i)
# 		if (i*i!=n and i!=1):
# 			divisors.append(int(n/i))
# 	return divisors
#
# def are_amicable(n1,n2):
# 	if sum(get_divisors(n1))==n2:
# 		if sum(get_divisors(n2))==n1:
# 			return True
# 	return False
#
# sum = 1
# for i in range(1,10001):
# 	for j in range(1,10001):
# 		if(i!=j):
# 			if(are_amicable(i,j)):
# 				sum+=i
# 				sum+=j


def sum_div(n):
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

def amicable_numbers(limit):
    for a in range(limit):
        b = sum_div(a)
        if a != b and sum_div(b) == a:
            yield a

print(sum(amicable_numbers(10000)))
