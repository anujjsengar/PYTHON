#An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(y):
    if y%4==0 and y%400==0 and y%100!=0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))
