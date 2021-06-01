def single_dig(num):
	if(num==1):
		return 'one'
	elif(num==2):
		return 'two'
	elif(num==3):
		return 'three'
	elif(num==4):
		return 'four'
	elif(num==5):
		return 'five'
	elif(num==6):
		return 'six'
	elif(num==7):
		return 'seven'
	elif(num==8):
		return 'eight'
	elif(num==9):
		return 'nine'

def dbl_digit(num):
	if(num==10):
		return 'ten'
	if(num==11):
		return 'eleven'
	elif(num==12):
		return 'twelve'
	elif(num==13):
		return 'thirteen'
	elif(num==14):
		return 'fourteen'
	elif(num==15):
		return 'fifteen'
	elif(num==16):
		return 'sixteen'
	elif(num==17):
		return 'seventeen'
	elif(num==18):
		return 'eighteen'
	elif(num==19):
		return 'nineteen'
	elif(num//10==2):
		if(num/10==2):
			return 'twenty'
		pre_ten = 'twenty'
		return pre_ten + single_dig(num%10)
	elif(num//10==3):
		if(num/10==3):
			return 'thirty'
		pre_ten = 'thirty'
		return pre_ten + single_dig(num%10)
	elif(num//10==4):
		if(num/10==4):
			return 'forty'
		pre_ten = 'forty'
		return pre_ten + single_dig(num%10)
	elif(num//10==5):
		if(num/10==5):
			return 'fifty'
		pre_ten = 'fifty'
		return pre_ten + single_dig(num%10)
	elif(num//10==6):
		if(num/10==6):
			return 'sixty'
		pre_ten = 'sixty'
		return pre_ten + single_dig(num%10)
	elif(num//10==7):
		if(num/10==7):
			return 'seventy'
		pre_ten = 'seventy'
		return pre_ten + single_dig(num%10)
	elif(num//10==8):
		if(num/10==8):
			return 'eighty'
		pre_ten = 'eighty'
		return pre_ten + single_dig(num%10)
	elif(num//10==9):
		if(num/10==9):
			return 'ninety'
		pre_ten = 'ninety'
		return pre_ten + single_dig(num%10)



def convert_num_to_words(num):
	pre_ten = 'nil'
	pre_hundo = 'nil'
	#number is max 1000
	if(num<10):
		#single-digit
		return single_dig(num)
	elif(num<100):
		#double-digits
		return dbl_digit(num)
	else:
		#triple-digits
		if(num//100==1):
			if(num/100==1):
				return 'onehundred'
			pre_hundo = "onehundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)

		if(num//100==2):
			if(num/100==2):
				return 'twohundred'
			pre_hundo = "twohundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==3):
			if(num/100==3):
				return 'threehundred'
			pre_hundo = "threehundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==4):
			if(num/100==4):
				return 'fourhundred'
			pre_hundo = "fourhundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==5):
			if(num/100==5):
				return 'fivehundred'
			pre_hundo = "fivehundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==6):
			if(num/100==6):
				return 'sixhundred'
			pre_hundo = "sixhundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==7):
			if(num/100==7):
				return 'sevenhundred'
			pre_hundo = "sevenhundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==8):
			if(num/100==8):
				return 'eighthundred'
			pre_hundo = "eighthundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num//100==9):
			if(num/100==9):
				return 'ninehundred'
			pre_hundo = "ninehundredand"
			if(num%100>9):
				return pre_hundo + dbl_digit(num%100)
			else:
				return pre_hundo+single_dig(num%100)
		if(num/100==10):
			return 'onethousand'

count = 0
for i in range(1,1001):
	print("{} = {}".format(i,convert_num_to_words(i)))
	count += len(convert_num_to_words(i))
print('fin count ',count)
