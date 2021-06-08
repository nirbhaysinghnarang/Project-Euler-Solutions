UPPER_LIM = int(10e6)

def is_palindrome(num):
	return (str(num)==str(num)[::-1])

def to_binary(num):
	return bin(num).replace("0b", "")

def is_bin_palindrome(num):
	num = to_binary(num)
	return is_palindrome(num)

sum = 0
for i in range(0,UPPER_LIM+1):
	if(is_palindrome(i) and is_bin_palindrome(i)):
		sum+=i

print(sum)
