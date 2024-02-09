import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from function import get_usd


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.folderpath = None
        self.main_date = None
        self.label = QtWidgets.QLabel("Выберите исходный CSV")
        self.select_folder_button = QtWidgets.QPushButton("Выбрать папку")
        self.select_folder_button.clicked.connect(self.select_folder)

        # self.create_dataset_button = QtWidgets.QPushButton("Создать датасет")
        # self.create_dataset_button.clicked.connect(self.create_dataset)

        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.get_data_button = QtWidgets.QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.get_date)

        '''Layout'''
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_folder_button)
        # layout.addWidget(self.create_dataset_button)
        layout.addWidget(self.date_input)
        layout.addWidget(self.get_data_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку')
        QtWidgets.QMessageBox.information(
            self, 'Папка выбрана', self.folderpath)
        self.folderpath += "/data.csv"

    def get_date(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Выберите папку с исходным файлом')
            return

        main_date = self.date_input.date().toString(QtCore.Qt.ISODate)
        self.find_course(main_date)

    def create_dataset(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        self.destination_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для нового датасета')
        if self.destination_folder:
            self.menu = NewData(self)
            self.menu.show()
    def find_course(self, main_date):
        course = get_usd(main_date)
        if course == None:
            QtWidgets.QMessageBox.information(
                self, 'Данные не получены', f'Курса доллара на {main_date} нет')
        else:
            QtWidgets.QMessageBox.information(self, 'Данные получены',
                                              f'Курс доллара на {main_date} равен {course} руб')

class NewData(QtWidgets.QDialog):
     def __init__(self, Main: Window = None):
        super(NewData, self).__init__(Main)
        self.setModal(True)

        if Main is not None:
            self.Main = Main

        layout = QtWidgets.QVBoxLayout()

        self.button1 = QtWidgets.QPushButton("Разделить на X и Y")
        self.button1.clicked.connect(self.but1)
        self.button2 = QtWidgets.QPushButton("Разделить по годам")
        self.button2.clicked.connect(self.but2)
        self.button3 = QtWidgets.QPushButton("Разделить по неделям")
        self.button3.clicked.connect(self.but3)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

        def but1(self):
            split_by_columns(self.Main.folderpath)
            QtWidgets.QMessageBox.information(self, 'Датасет создан',
                                            f'Датасет создан и сохранен в {self.Main.destination_folder}')
            self.close()

        def but2(self):
            split_by_years(self.Main.folderpath, self.Main.destination_folder)
            QtWidgets.QMessageBox.information(self, 'Датасет создан',
                                            f'Датасет создан и сохранен в {self.Main.destination_folder}')
            self.close()

        def but3(self):
            split_by_weeks(self.Main.folderpath, self.Main.destination_folder)
            QtWidgets.QMessageBox.information(self, 'Датасет создан',
                                            f'Датасет создан и сохранен в {self.Main.destination_folder}')
            self.close()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
