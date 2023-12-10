import sys
from PyQt5 import QtWidgets
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        
        select_folder_button = QtWidgets.QLineEdit()
        
        create_annotation_button = QtWidgets.QPushButton('Получить данные в формате YYYY-MM-DD', self)
        create_annotation_button.clicked.connect(self.check_date)
