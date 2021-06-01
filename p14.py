def collatz_length(num):
	chain = [num]
	index = 0
	while(chain[-1]!=1):
		if(chain[index]%2==0):
			chain.append(chain[index]/2)
		else:
			chain.append(3*chain[index]+1)
		index+=1
	return len(chain)

sizes = []

for i in range(2,1000000):
	sizes.append(collatz_length(i))


max_size = max(sizes)
for i in range (len(sizes)):
	if(sizes[i]==max_size):
		max_val = [j for j in range(2,1000000)][i]


print("STARTING NUM {} HAS MAX CHAIN SIZE {}".format(max_val,max_size))
