import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(600, 300)
        self.setWindowTitle('创建按钮和按钮点击事件的例子')
        self.button1 = QPushButton('按键1', self)
        self.button1.clicked.connect(self.clickButton)
    def clickButton(self):
        sender = self.sender()
        print(sender.text() + '被点击')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
