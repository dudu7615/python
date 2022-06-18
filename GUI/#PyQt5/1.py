import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
 
 
# 继承QWidget
class main(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        # 调整窗口大小
        self.resize(900, 500)
        # 窗口居中
        self.center()
        # 窗口标题
        self.setWindowTitle("PyQt5用面向对象实现")
        # 显示窗口
        self.show()
 
    # 实现居中
    def center(self):
        f = self.frameGeometry()
        c = QDesktopWidget().availableGeometry().center()
        f.moveCenter(c)
        self.move(f.topLeft())
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = main()
    sys.exit(app.exec_())