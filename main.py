import ctypes
import re
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileDialog
from PyQt5.uic import loadUi
from langdetect import detect


class MainWindow(QMainWindow, QTextEdit):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('mainwindow.ui', self)
        self.pushButton.clicked.connect(self.file_choose)
        self.pushButton_2.clicked.connect(self.main)
        self.pushButton_3.clicked.connect(self.saveFileDialog)
        self.pushButton_4.clicked.connect(self.clearAll)

    def clearAll(self):
        a = self.textEdit.toPlainText()

        if (self.textEdit.toPlainText() == '') or (self.textEdit.toPlainText() == ''):
            text = "Поля уже пустые"
            title = "Сообщение"
            style = 0
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        self.textEdit.clear()
        self.textEdit_2.clear()

    def file_choose(self):
        tex_pole = self.textEdit
        path = QFileDialog.getOpenFileName(parent=None, filter='text *.txt')[0]
        if path == '':
            text = "Файл для открытия не выбран"
            title = "Сообщение"
            style = 0
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        fil = open(path, 'r', encoding='utf-8')
        txt = fil.read()
        tex_pole.setText(txt)

    def saveFileDialog(self):

        if self.textEdit_2.toPlainText() == '':
            text = "Поле нормализованный текст пустое"
            title = "Сообщение"
            style = 0
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(parent=None, filter='text *.txt', options=options)

        if fileName == '':
            text = "Укажите название файла для сохранения текста"
            title = "Сообщение"
            style = 0
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)

        with open(fileName, 'w', encoding='utf-16') as f:
            text = self.textEdit_2.toPlainText()
            f.write(text)

    def main(self):

        if self.textEdit.toPlainText() == '':
            text = "Введите текст или загрузите его из файла"
            title = "Сообщение"
            style = 0
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)

        a_string = self.textEdit.toPlainText()
        a_string = a_string.lower()
        pattern = re.compile('[^a-zа-яёЁ\s^a-zA-Z0-9-]')
        a_string = re.sub(pattern, '', a_string)
        print(detect('1eet'))
        split_str = a_string.split()
        res_str = ''
        for word in split_str:
            if word.isdigit():
                continue

            else:
                if detect(word) != "en":
                    l2c = {u"o": u"о",
                           u"a": u"а",
                           u"e": u"е",
                           u"c": u"с",
                           u"x": u"х",
                           u"p": u"р",
                           u"0": u"о",
                           u"3": u"з",
                           u"4": u"ч",
                           u"6": u"б",
                           u"8": u"в",
                           u"1": u"l",
                           }
                    l2c_get = l2c.get
                    word = u"".join(
                        l2c_get(x, x) for x in word)
                    res_str += word + ' '
                else:
                    l2c = {u"о": u"o",
                           u"а": u"a",
                           u"е": u"e",
                           u"с": u"c",
                           u"х": u"x",
                           u"р": u"p",
                           u"1": u"l",
                           u"3": u"e",
                           u"7": u"t", }
                    l2c_get = l2c.get
                    word = u"".join(
                        l2c_get(x, x) for x in word)
                    res_str += word + ' '

        self.textEdit_2.setPlainText(res_str)


app = QApplication([])
window = MainWindow()
window.setStyleSheet("#MainWindow{background-color:white}")
window.show()
app.exec_()
