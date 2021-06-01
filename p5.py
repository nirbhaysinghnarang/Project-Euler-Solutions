def evenly_divisible(num):
	if(num%2!=0):
		return False
	for i in range(1,21):
		if(num%i!=0):
			return False
	return True

x = 2520
while True:
	if(evenly_divisible(x)):
		print(x)
		break
	x+=10
