import os
del_extension = {
    '.tmp': '临时文件',
    '._mp': '临时文件_mp',
    '.log': '日志文件',
    '.gid': '临时帮助文件',
    '.chk': '磁盘检查文件',
    '.old': '临时备份文件',
    '.xlk': 'Excel备份文件',
    '.bak': '临时备份文件bak'
}
del_userprofile = ['cookies', 'recent', 'Temporary Internet Files', 'Temp']
del_windir = ['prefetch', 'temp']
SYS_DRIVE = os.environ['systemdrive'] + '\\'
USER_PROFILE = os.environ['userprofile']
WIN_DIR = os.environ['windir']
 
def del_dir_or_file(root):
    try:
        if os.path.isfile(root):
            os.remove(root)
            print ("file",root,"removed")
        elif os.path.isdir(root):
            os.rmdir(root)
            print("dir",root,"removed")
 
    except WindowsError:
        print("failure",root,"can't remove")
 
def formatSize(b):
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
 
class DiskClean(object):
    def __init__(self):
        self.del_info = {}
        self.del_file_paths = []
        self.total_size = 0
        for i,j in del_extension.items():
            self.del_info[i] = dict(name = j,count = 0 )
 
    def scanf(self):
        for roots,dirs,files in os.walk(USER_PROFILE):
            for files_item in files:
                file_extension = os.path.splitext(files_item)[1]
                if file_extension in self.del_info:
                    file_full_path = os.path.join(roots,files_item)
                    self.del_file_paths.append(file_full_path)
                    self.del_info[file_extension]['count'] += 1
                    self.total_size += os.path.getsize(file_full_path)
 
    def show(self):
        re = formatSize(self.total_size)
        for i in self.del_info:
            print(self.del_info[i]["name"],"共计",self.del_info[i]["count"],"个")
        return re
 
    def delete_files(self):
        for i in self.del_file_paths:
            print(i)
            del_dir_or_file(i)
if __name__ == "__main__":
    print("初始化清理垃圾程序")
    cleaner = DiskClean()
    print("开始扫描垃圾文件请耐心等待\n")
    cleaner.scanf()
    print("扫描成功，结果如下")
    re = cleaner.show()
    cleaner.delete_files()