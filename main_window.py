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


        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.get_data_button = QtWidgets.QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.get_date)

        '''Layout'''
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_folder_button)
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

    
    def find_course(self, main_date):
        course = get_usd(main_date)
        if course == None:
            QtWidgets.QMessageBox.information(
                self, 'Данные не получены', f'Курса доллара на {main_date} нет')
        else:
            QtWidgets.QMessageBox.information(self, 'Данные получены',
                                              f'Курс доллара на {main_date} равен {course} руб')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
