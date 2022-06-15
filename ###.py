from gooey import *
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice").Speak

def read():
    speaker()

# def txt():
#     name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])
#     file1 = open(name,'r',encoding='utf8')
#     speaker(file1.read())

@Gooey(program_name="Reader",encoding="utf-8",language='chinese')
def main():
    app = GooeyParser(description="对输入的内容或txt文本")
    app.add_argument('文件路径', widget="FileChooser")
    app.add_argument('请输入内容', widget="Textarea")  
    args = app.parse_args()
    print(args)
    

main()