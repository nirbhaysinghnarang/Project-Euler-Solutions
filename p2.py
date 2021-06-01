max_size = 4e6
fib_series = [1,2]
index = 2
sum = 2
while True:
	if(fib_series[-1]>max_size):
		break
	fib_series.append(fib_series[index-2]+fib_series[index-1])
	if(fib_series[index]%2==0):
		sum+=fib_series[index]
	index+=1

print(sum)
