import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from win32com.client import Dispatch
import gui
speaker = Dispatch("SAPI.SpVoice").Speak

def read():
    Text = ui.text.text()
    speaker(Text)

def open_txt():
    name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])
    file1 = open(name,'r',encoding='utf8')
    r3.insert(1.0,file1.read())

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = gui.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.opentxt.clicked.connect(open_txt)
ui.read.clicked.connect(read)

sys.exit(app.exec_())