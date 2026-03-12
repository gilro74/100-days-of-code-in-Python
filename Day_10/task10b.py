def is_leap_year(num):
    year = int(num)
    if year % 4== 0:
        if year % 100 == 0 :
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(input("Please type the year you would like to check if it is a leap year: ")))