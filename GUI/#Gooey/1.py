from gooey import *
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice").Speak

def read_text():
    speaker()

# def read_file():
#     name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])
#     file1 = open(name,'r',encoding='utf8')
#     speaker(file1.read())

@Gooey(program_name="Reader",encoding="utf-8",language='chinese',default_size=(600,450))
def main():
    app = GooeyParser(description="对输入的内容或txt文本进行朗读")
    app.add_argument("运行方式",choices=['本地程序','baidu-api'], default='本地程序')
    app.add_argument('文件路径', widget="FileChooser")
    app.add_argument('请输入内容', widget="Textarea")  
    args = app.parse_args()
    print(args)
    


main()