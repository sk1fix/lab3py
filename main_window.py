import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from function import get_usd
from function1 import get_usd1
from function2 import get_usd2
from function3 import get_usd3


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.folderpath = None
        self.menu = None
        self.main_date = None
        self.destination_folder = None
        self.label = QtWidgets.QLabel("Выберите исходный CSV")
        self.select_folder_button = QtWidgets.QPushButton("Выбрать папку")
        self.select_folder_button.clicked.connect(self.select_folder)

        self.create_dataset_button = QtWidgets.QPushButton("Создать датасет")
        self.create_dataset_button.clicked.connect(self.create_dataset)

        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.get_data_button = QtWidgets.QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.get_date)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_folder_button)
        layout.addWidget(self.create_dataset_button)
        layout.addWidget(self.date_input)
        layout.addWidget(self.get_data_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_folder(self) -> None:
        """
            a function for selecting a folder
        """
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку')
        QtWidgets.QMessageBox.information(
            self, 'Папка выбрана', self.folderpath)
        self.folderpath += "/data.csv"

    def get_date(self) -> None:
        """
            choosing a date and receiving a subsequent course
        """
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Выберите папку с исходным файлом')
            return

        main_date = self.date_input.date().toString(QtCore.Qt.ISODate)
        self.find_course(main_date)

    def create_dataset(self) -> None:
        """
            selecting a folder for a new dataset
        """
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        self.destination_folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку для нового датасета')
        if self.destination_folder:
            self.menu = SubWindow(self)
            self.menu.show()

    def find_course(self, main_date) -> None:
        """
            function for course output
        """
        course = get_usd(main_date, self.folderpath)
        if course == None:
            QtWidgets.QMessageBox.information(
                self, 'Данные не получены', f'Курса доллара на {main_date} нет')
        else:
            QtWidgets.QMessageBox.information(self, 'Данные получены',
                                              f'Курс доллара на {main_date} равен {course} руб')


class SubWindow(QtWidgets.QDialog):
    def __init__(self, Main: Window = None) -> None:
        super(SubWindow, self).__init__(Main)
        self.setModal(True)
        self.main_window = Main
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

    def but1(self) -> None:
        """
            creating x and y datasets
        """
        get_usd1(self.main_window.folderpath,
                 self.main_window.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан')
        self.close()

    def but2(self) -> None:
        """
            creating a dataset by year
        """
        get_usd2(self.main_window.folderpath,
                 self.main_window.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан')
        self.close()

    def but3(self) -> None:
        """
            creating a dataset by week
        """
        get_usd3(self.main_window.folderpath,
                 self.main_window.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан')
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
