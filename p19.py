# Could have been trivial, but I didn't want to use datetime.
# Instead, I implemented the "mentalist approach" as described here:
# http://gmmentalgym.blogspot.de/2011/03/day-of-week-for-any-date-revised.html

def is_leapyear(n):
    if (n%100 == 0) and not (n%400 == 0):
        return False
    if n%4 == 0:
        return True
    return False

def leapyear_code(year):
    leapyear_table = [0, 5, 3, 1, 6, 4, 2]
    decade = year%100
    if (decade <= 52) and (decade >= 28):
        decade -= 28
    elif decade <= 80 and (decade >= 56):
        decade -= 56
    elif decade <= 96 and (decade >= 84):
        decade -= 84
    return leapyear_table[int(decade/4)]

def year_code(year, leapyear):
    if leapyear:
        return leapyear_code(year)
    i = 0
    while not is_leapyear(year):
        year -= 1
        i += 1
    return (leapyear_code(year) + i)%7

def month_code(month, leapyear):
    month_codes = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] # jan - dec
    month_codes_leap = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    return month_codes_leap[month-1] if leapyear else month_codes[month-1]

def century_code(year): # ugly, yes
    if year < 2000:
        test = 10 - int((year%1000)/100)
        if test%4 == 0:
            return 0
        if test%4 == 1:
            return 1
        if test%4 == 2:
            return 3
        if test%4 == 3:
            return 5
    if year >= 2100:
        test = int((year%1000)/100)
        if test%4 == 0:
            return 0
        if test%4 == 1:
            return 5
        if test%4 == 2:
            return 3
        if test%4 == 3:
            return 1
    return 0

def day_code(day, month, year):
    leap = is_leapyear(year)
    return (century_code(year) + day + month_code(month, leap) + year_code(year, leap))%7

def get_day(day, month, year):
    day_codes = [7, 1, 2, 3, 4, 5, 6]
    return day_codes[day_code(day, month, year)]

###############
# Solution

sum = 0
for year in range(1901, 2001):
    for month in range(12):
        if get_day(1, month, year) == 7:
            sum += 1
print(sum)
