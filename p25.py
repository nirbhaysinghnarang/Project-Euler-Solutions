def count_digits(num):
	digits = 0
	while(num!=0):
		num = num//10
		digits+=1
	return digits

def main():
	fib1 = 1
	fib2 = 1
	nextFib = fib1+fib2
	index = 3
	while(count_digits(nextFib)<1000):
		fib1 = fib2
		fib2 = nextFib
		nextFib = fib1 + fib2
		index+=1
	print(index)

main()
