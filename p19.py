st_yr = 1901
#1 jan 1901 = tuesday


def isLeapYr(yr):
	if(yr % 4) == 0:
		if (yr % 100) == 0:
			if (yr % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


def daysInAMonth(month_index,yr):
	leapYear = False
	if(isLeapYr(yr)):
		leapYear = True
	if(month_index==0 or month_index==8 or month_index==3 or month_index==5 or month_index==10):
		return 31
	if(month_index==1 and leapYear):
		return 29
	elif(month_index==1 and not leapYear):
		return 28
	else:
		return 30


day_index = 1
month_index = 0
sunday_first_day_of_month_count = 1


for year in range(st_yr,2001):
	print(year)
	for month in range(0,12):
		daysInThisMonth = daysInAMonth(month,year)
		day_index += daysInThisMonth%7
		day_index = day_index%7
		if(day_index==6):
			sunday_first_day_of_month_count+=1




print(sunday_first_day_of_month_count)
