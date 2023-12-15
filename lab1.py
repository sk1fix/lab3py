import datetime
import json
import csv

import requests


def get_data(my_date: datetime.date) -> str:
    my_year = str(my_date.year)
    my_month = str(my_date.month) if my_date.month > 9 else '0' + \
        str(my_date.month)
    my_day = str(my_date.day) if my_date.day > 9 else '0' + str(my_date.day)
    return my_year + '/' + my_month + '/' + my_day


def get_usd() -> None:
    my_date = datetime.date.today()
    my_date -= datetime.timedelta(days=1)
    with open('data.csv', 'w', newline='', encoding="utf-8") as file:
        while my_date.year > 2021:
            url = "https://www.cbr-xml-daily.ru/archive/" + \
                get_data(my_date) + "/daily_json.js"
            response = requests.get(url)
            data = json.loads(response.text)
            if 'Valute' not in data:
                my_date -= datetime.timedelta(days=1)
                continue
            valute_data = data['Valute']
            wr = csv.writer(file)
            for valute in valute_data.values():
                if valute['CharCode'] == 'USD':
                    wr.writerow((f"Дата: {data['Date'][0:10]} ").split(
                        ',') + (f"{valute['Name']} курс: {valute['Value']}").split(','))
            my_date -= datetime.timedelta(days=1)


def main() -> None:
    get_usd()
