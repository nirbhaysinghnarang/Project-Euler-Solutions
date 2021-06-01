def sum_squares(num):
		return (n*(n+1)*(2*n+1))/6

def sum_squared(num):
	return sum([i for i in range(num+1)])**2


n = 100
print(sum_squared(n)-sum_squares(n))
