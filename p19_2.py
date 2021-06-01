from datetime import date

def num_sundays_on_first_of_month(year1, year2):
  num_sundays = 0
  for i in range(year1, year2+1):
      for j in range(1, 13):
          if date(i, j, 1).weekday() == 6:
              num_sundays += 1
  return num_sundays

if __name__ == '__main__':
    print(num_sundays_on_first_of_month(1901,2000))
