import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from function import get_usd


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку')
        QtWidgets.QMessageBox.information(
            self, 'Папка выбрана', self.folderpath)
        self.folderpath += "/data.csv"
    def find_course(self,main_date):
        course = get_usd(main_date)
        if course == None:
            QtWidgets.QMessageBox.information(self, 'Данные не получены', f'Курса доллара на {main_date} нет')
        else:
            QtWidgets.QMessageBox.information(self, 'Данные получены',
                                              f'Курс доллара на {main_date} равен {course} руб')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
