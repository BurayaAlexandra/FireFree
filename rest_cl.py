import sys
from PyQt5.QtWidgets import QFileDialog
from Interface import *
from PyQt5 import QtWidgets
import cv2
import os
from Server import serv

"""
Класс MyWin используется для работы в окне интерфейса
"""


class MyWin(QtWidgets.QMainWindow):
    """
    Инициализация главного рабочего окна. Изначально пользователь из кнопок видит
    только кнопку "Выбрать директорию".
    """
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.select_directory)
        self.ui.pushButton2.clicked.connect(self.analyze)
        self.ui.pushButton2.hide()
        self.ui.pushButton1.clicked.connect(self.show_fire)

    """"
    Функция, привязвнная к кнопке "Выбрать директорию". Данная функция открыает проводник, получает абсолютный путь 
    до выбранной директории, записывает его в специально отведенное для этого место и делает кнопку "Анализировать"
    видимой.
    """
    def select_directory(self):
        self.dirname = QFileDialog.getExistingDirectory(self, "Выбрать папку", "./testing")
        self.ui.folder_path.setText(self.dirname)
        self.ui.pushButton2.show()
    """
    функция, привязвнная к кнопке "Анализировать". Данная функция первым действием отчищает таблицу с результататми 
    анализа от всех имеющихся записей. Затем считывает все файлы подходящего расширения из выбранной ранее директории,
    аналитически обрабатывает считанные изображения и заносит результаты анализа в таблицу. В случае, если результат 
    аналитической обработки изображения положительный, наименование данного изображения заносится в сеелектор.
    """
    def analyze(self):
        num_of_row = 0
        self.ui.tableWidget1.setRowCount(0)
        self.ui.fireImg.clear()
        for image_path in os.listdir(self.dirname):
            if image_path[-4:] != '.jpg' and image_path[-4:] != '.png':
                continue

            file_path = self.dirname + '/' + image_path
            image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
            verdict = serv(image)
            self.ui.update_table(num_of_row, image_path, verdict)
            if verdict:
                self.ui.fireImg.addItem(image_path)
            num_of_row += 1
    """
    Функция, привязвнная к кнопке "Показать". Данная функция отображает пользователю изображение, выбранное в селекторе.
    """
    def show_fire(self):
        img = cv2.imread(self.dirname + '/' + self.ui.fireImg.currentText(), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (640, 360))
        cv2.imshow('alert', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


"""
Запуск приложения.
"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
