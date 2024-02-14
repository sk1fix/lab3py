import datetime
import csv


def get_usd(my_date: datetime.date, path: str) -> str:
    f = open(path, 'r')
    s = csv.reader(f)
    for row in s:
        if str(row[0][10:20]) == str(my_date):
            return (row[1][30:])
        if str(my_date) > row[0][10:20]:
            return None


def get_usd_XY(my_date: datetime.date) -> str:
    fx = open("X.csv", 'r')
    fy = open("Y.csv", 'r')
    sx = csv.reader(fx)
    sy = csv.reader(fy)
    countx = 0
    county = 0
    for row in sx:
        countx += 1
        print()
        if str(row[0][10:20]) == str(my_date):
            break
        if str(my_date) > row[0][10:20]:
            return None
    for row in sy:
        county += 1
        if countx == county:
            return str(row[0][30:])


def get_data_year() -> str:
    my_date = datetime.date.today()-datetime.timedelta(days=1)
    my_year = str(my_date.year)
    my_month = str(my_date.month) if my_date.month > 9 else '0' + \
        str(my_date.month)
    my_day = str(my_date.day) if my_date.day > 9 else '0' + str(my_date.day)
    return my_year + my_month + my_day


def get_usd_year(my_date: datetime.date) -> str:
    year = str(my_date.year)
    try:
        f = open(year + '0101_' + year + '1231.csv', 'r')
    except:
        f = open(year + '0101_' + get_data_year() + '.csv')
    s = csv.reader(f)
    for row in s:
        if str(row[0][10:20]) == str(my_date):
            return (row[1][30:])
        if str(my_date) > row[0][10:20]:
            return None


def get_data_week(my_date: datetime.date) -> str:
    my_year = str(my_date.year)
    my_month = str(my_date.month) if my_date.month > 9 else '0' + \
        str(my_date.month)
    my_day = str(my_date.day) if my_date.day > 9 else '0' + str(my_date.day)
    return my_year + my_month + my_day


def get_usd_week(my_date: datetime.date) -> str:
    my_week = my_date.weekday()
    try:
        f = open(get_data_week(my_date-datetime.timedelta(days=my_week)) + '_' +
                 get_data_week(my_date+datetime.timedelta(days=6 - my_week)) + '.csv')
    except:
        f = open(get_data_week(my_date-datetime.timedelta(days=my_week)) + '_' +
                 get_data_week(my_date) + '.csv')
    s = csv.reader(f)
    for row in s:
        if str(row[0][10:20]) == str(my_date):
            return (row[1][30:])
        if str(my_date) > row[0][10:20]:
            return None
