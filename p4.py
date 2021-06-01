def is_palindrome_num(num):
	if(str(num)==(str(num)[::-1])):
		return True

palindrome_nums = []
for i in range(100,1000):
	for j in range(100,1000):
		if(i!=j):
			if(is_palindrome_num(i*j)):
				palindrome_nums.append(i*j)

print(max(palindrome_nums))
