import math
def get_num_divisors(num):
	number_of_factors = 0
	for i in range(1, int(math.ceil(math.sqrt(n)))+1):
		if n % i == 0:
			number_of_factors +=2
		if i*i==n:
			number_of_factors -=1
	return number_of_factors



def generate_triangular_number(n):
	return (n*(n+1))/2


counter = 1
n = 1
while get_num_divisors(n)<500:
	counter+=1
	print('counter {}'.format(counter))
	n = generate_triangular_number(counter)
	print('{}th triangular number {}'.format(counter,n))

print(n)
print(get_num_divisors(n))
