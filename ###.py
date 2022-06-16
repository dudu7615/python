from colored import stylize, attr
from gooey import Gooey, GooeyParser
 
 
@Gooey(program_name="BattCommunicate_GUI")
def gui_main():
    parser = GooeyParser(description="BattCommunicate_GUI")
 
    subs_list = parser.add_subparsers(help="cmms", dest="command")
    sub_action1 = subs_list.add_parser("Run_Reset")
    sub_action1.add_argument("Reset_Cmms",metavar="reset",default="s reset")
    sub_action2 = subs_list.add_parser("Get_battery")
    sub_action2.add_argument("Get_battery_Cmms",metavar="getbatt",default="b status")
 
    args = parser.parse_args()
    print(args, flush=True)  
    print(stylize("This is bold.",attr("bold")))
    print(type(args))
    if "s reset" in args.Reset_Cmms : # 获取文本框的输入值
        print(">>> reset success.")
        
    else:
        print(">>> ERROR: reset fail.")


 
if __name__ == '__main__':
    gui_main()