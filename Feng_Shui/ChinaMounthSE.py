from datetime import date, timedelta
import calendar

def get_number_of_days(year, month):
    if month in (1, 3, 11, 12):
        return 7
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 8
        else:
            return 7
    elif month in (4, 5, 10, 12):
        return 5
    elif month in (6, 9):
        return 6
    elif month in (7, 8):
        return 7

year = int(input("Введите год: "))
month = int(input("Введите месяц: "))

start_day_month = date(year, month, get_number_of_days(year, month))
end_day_month = start_day_month + timedelta(days=calendar.monthrange(year, month)[1])

print(start_day_month, end_day_month)
