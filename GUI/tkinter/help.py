""" 
教程网址：https://www.delftstack.com/zh/howto/python-tkinter/
"""

from tkinter import *
from tkinter import filedialog

def a():
    print()

###---程序中的可变数据---###
list0 = ["<第一项>","<第二项>"]
list1 = StringVar()  # 程序中的可变数据
a1 = StringVar()
""" <变量名> = StringVar() """
list1.set(list0[0])  # 对它赋值
a1.set('')
""" <StringVar变量名>.set(<赋值内容>) """

###---基本窗口设置---###
app = Tk()  # 创建窗口
""" <窗口名> = Tk() """
app.geometry('0x0')  # 设置大小
""" <窗口名>.geometry('<长>x<宽>') """
app.title("Reader")  # 设置窗口名称
""" <窗口名>.title("<窗口名>") """

###---设置控件---###
""" <控件名> = <类名>(<窗口名>,<其他设置>) """  # 通用控件设置
x = Button(app,text="开始朗读",font=("微软雅黑",8),fg="green",command=a)  # 按钮
""" <按钮名> = Button(<窗口名>,text=<按钮文本>,font=("<字体名>",<字号>),fg="字体颜色",command=<事件名>) """
x0 = Text(app,font=("微软雅黑",10))  # 多行输入框（需要另外添加内容详见“Text设置”）
""" <多行文本框名> = Text(<窗口名>,font=("<字体名>",<字号>)) """
x = Entry(app,textvariable=a1,font=("微软雅黑",8),fg="green")  # 单行输入框
"""
<单行文本框名> = Text(<窗口名>,text=<文本>,font=("<字体名>",<字号>),fg="字体颜色")  # 数据不自动更新
<单行文本框名> = Text(<窗口名>,textvariable=<文本>,font=("<字体名>",<字号>))  # 数据自动更新
"""
x = Label(app,textvariable=a1,font=("微软雅黑",8),fg="green")
""" <文本框名> = Label(<窗口名>,text=<文本>,font=("<字体名>",<字号>),fg="字体颜色")  # 用户不能直接修改内容 """
x = OptionMenu(app,list1,*list0)  # 详见“菜单设置”
""" <菜单名称> = OptionMenu(<窗口名>,<默认显示名称（StringVar类）>,<*列表具体内容（列表）>) """

###---展示控件---###
x.place(x=0,y=0,height=0,width=0)  # 输入坐标
""" <控件名>.place(x=<横轴>,y=<纵轴>,height=<高>,width=<宽>) """

###---文件选择器---###
name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])  # 建议设置为按钮事件
""" <变量名（路径）> = filedialog.askopenfilename(filetypes=[("<文件类型>","<文件后缀>")]) """

###---菜单设置---###
def chose(*args):  # *args为必要参数
    global aaa  # 公开aaa变量
    aaa=list1.get()  # 获取变化项目
    """ <变量名（目标）> = <OptionMenu的默认选项>.get() """

list1.trace("w", chose)  # 检查到默认选项变化后触发chose函数
""" <OptionMenu的默认选项>.trace("w", <函数名>) """

###---Text设置---###
x0.insert(1.0,'') # 设置或替换默认值 
""" <Text控件名>.insert(<从第几个字开始（int 保留一位小数）>,'<需要的内容>') """
