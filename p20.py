def fac(n):
	if(n==1):
		return (1)
	else:
		return (n)*fac(n-1)



fac_100 = str(fac(100))
sum = 0
for char in fac_100:
	sum+=int(char)

print(sum)
