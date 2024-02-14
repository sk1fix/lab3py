import datetime
import csv


# def get_data(my_date: datetime.date) -> str:
#     my_year = str(my_date.year)
#     my_month = str(my_date.month) if my_date.month > 9 else '0' + \
#         str(my_date.month)
#     my_day = str(my_date.day) if my_date.day > 9 else '0' + str(my_date.day)
#     return my_year + '/' + my_month + '/' + my_day


# def get_usd() -> None:
#     my_date = datetime.date.today()
#     my_date -= datetime.timedelta(days=1)
#     with open('X.csv', 'w', newline='', encoding="utf-8") as xfile:
#         with open('Y.csv', 'w', newline='', encoding="utf-8") as yfile:
#             while my_date.year > 2022:
#                 url = "https://www.cbr-xml-daily.ru/archive/" + \
#                     get_data(my_date) + "/daily_json.js"
#                 response = requests.get(url)
#                 data = json.loads(response.text)
#                 if 'Valute' not in data:
#                     my_date -= datetime.timedelta(days=1)
#                     continue
#                 valute_data = data['Valute']
#                 wrx = csv.writer(xfile)
#                 wry = csv.writer(yfile)
#                 for valute in valute_data.values():
#                     if valute['CharCode'] == 'USD':
#                         wrx.writerow(
#                             (f"Дата: {data['Date'][0:10]}").split(','))
#                         wry.writerow(
#                             (f"{valute['Name']} курс: {valute['Value']}").split(','))
#                 my_date -= datetime.timedelta(days=1)


def get_usd1(path: str, path1: str) -> None:
    f = open(path, 'r', encoding="utf-8")
    s = csv.reader(f)
    with open(path1 + '/X.csv', 'w', newline='', encoding="utf-8") as xfile:
        with open(path1 + '/Y.csv', 'w', newline='', encoding="utf-8") as yfile:
            for row in s:
                wrx = csv.writer(xfile)
                wry = csv.writer(yfile)
                wrx.writerow(row[0].split(','))
                wry.writerow(row[1].split(','))
