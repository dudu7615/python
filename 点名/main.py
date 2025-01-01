from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtGui import QIcon,Qt
from PySide6.QtCore import Qt
from pathlib import Path
import random
import sys
import pickle
from Ui.Ui_ui import Ui_MainWindow

ROOT = Path(__file__).parent
DATA =  ROOT

if not DATA.exists():
    DATA.mkdir(exist_ok=True, parents=True)

names: list[str] = pickle.load((DATA / "names.pkl").open("rb"))


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("点名")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.run.clicked.connect(self.run)
        self.setStyleSheet((ROOT / "style.qss").read_text(encoding="utf-8"))
        self.ui.showName.setText("点名")
        self.ui.showName.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def run(self):
        name = random.choice(names) if names else "没有名字了，重启程序以继续"
        # try:
        #     names.remove(name)
        # except:
        #     ...
        self.ui.showName.setText((name))
        self.ui.showName.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # def saveData(self):
    #     code = base64.encodebytes(str(names).encode("utf-8"))
    #     (DATA / "names").write_text(code.decode("utf-8"), encoding="utf-8")


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(str(ROOT / "icon.png")))

    ui = UI()
    ui.show()

    sys.exit(app.exec())
