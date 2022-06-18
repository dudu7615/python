""" 
FileChooser       文件选择器  
MultiFileChooser  文件多选器 
DirChooser        目录选择器 
MultiDirChooser   目录多选器 
FileSaver         文件保存      
DateChooser       日期选择      
TextField         文本输入框      
Dropdown          下拉列表      
Counter           计数器      
CheckBox          复选框      
RadioGroup        单选框      
"""


from gooey import *

@Gooey(program_name="程序名",encoding="utf-8",language='chinese')
def main():
    parser = GooeyParser(description="介绍")
    parser.add_argument('文件路径', widget="FileChooser")      # 文件选择框
    parser.add_argument('日期', widget="DateChooser")          # 日期选择框
    args = parser.parse_args()                                 # 接收界面传递的参数
    print(555)

main()