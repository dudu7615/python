import os
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QWidget,QProgressBar,QPushButton,QHBoxLayout,QApplication
import sys
class FileDestory(QWidget):
    def __init__(self):
        super(FileDestory, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('电脑垃圾清理器')
        self.setFixedWidth(550)
        self.setFixedHeight(80)

        self.process = QProgressBar()
        self.process.setRange(0, 5)

        self.start_btn = QPushButton()
        self.start_btn.setText('开始清理')
        self.start_btn.clicked.connect(self.start_btn_click)

        hbox = QHBoxLayout()
        hbox.addWidget(self.process)
        hbox.addWidget(self.start_btn)

        self.thread_ = WorkThread(self)
        self.thread_.finished.connect(self.finished)
        self.thread_.exec_step.connect(self.set_step)

        self.setLayout(hbox)

    def start_btn_click(self):
        self.start_btn.setEnabled(False)
        self.thread_.start()

    def finished(self, finished):
        if finished is True:
            self.start_btn.setText('清理已完成')
            self.start_btn.setEnabled(False)

    def set_step(self, step):
        self.process.setValue(step)

class WorkThread(QThread):
    # 定义好信号量用来向主线程中传递变量的变化信息，这样主线程就可以知道运行结果如何。

    # 子线程是否执行完成的信号变量
    finished = pyqtSignal(bool)

    # 子线程具体的步骤信号变量
    exec_step = pyqtSignal(int)

    def __init__(self, parent=None):
        '''
        子线程类的初始化函数
        :param parent: UI界面类对象
        '''
        super(WorkThread, self).__init__(parent)
        self.working = True
        self.parent = parent

    def __del__(self):
        '''
        线程执行是否需要进入等待过程
        :return:
        '''
        self.working = False
        self.wait()

    def run(self):
        '''
        子线程主要执行逻辑的业务函数
        :return:
        '''
        file_type = {
            '.tmp': '临时文件',
            '._mp': '临时文件_mp',
            '.log': '日志文件',
            '.gid': '临时帮助文件',
            '.chk': '磁盘检查文件',
            '.old': '临时备份文件',
            '.xlk': 'Excel备份文件',
            '.bak': '临时备份文件bak'
        }

        user_pro = os.environ['userprofile']

        def del_file_and_dir(root):
            try:
                if os.path.isfile(root):
                    os.remove(root)
                    print("文件", root, "已经被移除！")
                elif os.path.isdir(root):
                    os.rmdir(root)
                    print("文件夹", root, "已经被移除！")

            except WindowsError:
                print("该文件", root, "不能被移除！")

        def init_size(b):
            try:
                kb = b // 1024
            except:
                print("传入字节格式不对")
                return "Error"
            if kb > 1024:
                M = kb // 1024
                if M > 1024:
                    G = M // 1024
                    return "%dG" % G
                else:
                    return "%dM" % M
            else:
                return "%dkb" % kb

        class Clean(object):
            def __init__(self):
                self.del_info = {}
                self.del_file_paths = []
                self.total_size = 0
                for i, j in file_type.items():
                    self.del_info[i] = dict(name=j, count=0)

            def count_files(self):
                for roots, dirs, files in os.walk(user_pro):
                    for files_item in files:
                        file_extension = os.path.splitext(files_item)[1]
                        if file_extension in self.del_info:
                            file_full_path = os.path.join(roots, files_item)
                            self.del_file_paths.append(file_full_path)
                            self.del_info[file_extension]['count'] += 1
                            self.total_size += os.path.getsize(file_full_path)

            def show_del_files(self):
                re = init_size(self.total_size)
                for i in self.del_info:
                    print(self.del_info[i]["name"], "共计", self.del_info[i]["count"], "个")
                return re

            def delete_files(self):
                for path in self.del_file_paths:
                    print('准备处理文件路径：', path)
                    del_file_and_dir(path)

        self.exec_step.emit(1)
        clean = Clean()
        self.exec_step.emit(2)
        clean.count_files()
        self.exec_step.emit(3)
        re = clean.show_del_files()
        self.exec_step.emit(4)
        clean.delete_files()
        self.exec_step.emit(5)
        self.finished.emit(True)


app = QApplication(sys.argv)
main = FileDestory()
main.show()
sys.exit(app.exec_())
