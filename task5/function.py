import csv


class DataIterator:
    def __init__(self, filename):
        self.filename = filename
        self.index = 0
        self.data = []
        with open(self.filename, 'r',) as file:
            r = csv.reader(file)
            for row in r:
                self.data.append((row[0][10:], row[1][30:]))

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            date, data = self.data[self.index]
            self.index += 1
            if data:
                return (date, data)
        raise StopIteration


iterator = DataIterator('data.csv')
for date, data in iterator:
    print(f"Дата: {date}, Данные: {data}")
