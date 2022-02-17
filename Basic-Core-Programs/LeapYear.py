
def LeapYear(year):
    '''
    Check wheather given year is leap year or not
    :param year: Year which we have to check
    :return: isTrue
    '''
    isTrue = 0
    if (year % 400 == 0):
       isTrue = 1
       return isTrue

    elif (year % 4 ==0) and (year % 100 != 0):
        isTrue = 1
        return isTrue

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return isTrue


year = int(input("Enter Year you have to evaluate:"))
year_out = LeapYear(year)
if year_out == 1:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")