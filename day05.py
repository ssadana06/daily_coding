#finding out which year is a leap year(true) or not(false)
def leap_year():
	year=int(input("enter the year you want to check\n"))
	if year%4!=0:
		return False
	elif year%400==0:
		return True
	elif year%100==0:
		return False
print(leap_year())