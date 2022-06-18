
import sys
from PyQt5.QtWidgets import *
 
# 1. 创建应用实例
app = QApplication(sys.argv)
# 2. 创建应用窗口
w = QWidget()
w.resize(900, 500)
w.setWindowTitle("第一个PyQt5程序")
# 3. 显示窗口
w.show()
# 4. 启动程序主循环
sys.exit(app.exec_())