UPPER_LIM = 1000000
const = "0."
offset = 1
index_arr = [10**(i) for i in range(7)]
product = 1
for j in range(1,UPPER_LIM+1):
	const += str(j)
for index in index_arr:
	product*=int(const[offset+index])
print(product)
