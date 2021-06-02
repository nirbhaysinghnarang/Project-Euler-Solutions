import string

with open('p022_names.txt', 'r') as f:
    data = f.read()
names_arr = data.split(",")
clean_arr = []
for name in names_arr:
	clean_arr.append(name.replace('"',""))

clean_arr.sort()


alphabet =list(string.ascii_uppercase)

def get_index(item,list):
	for i in range(0,len(list)):
		if(list[i]==item):
			return i
	return -1

def name_sum(name):
	name_sum = 0
	for char in name:
		char_index = get_index(char,alphabet)+1
		name_sum+=char_index
	return name_sum

running_sum = 0
index = 1
for name in clean_arr:
	running_sum+=(index*name_sum(name))
	index+=1

print(running_sum)
