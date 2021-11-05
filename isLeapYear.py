
def isLeapYear(year):
    '''returns if a year is a leap year'''
    print("is", year, "a leapyear?")
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0



print(isLeapYear(1922))


print(isLeapYear(2004))

print(isLeapYear(2009))

print(isLeapYear(2000))

