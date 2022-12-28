# update log----------------0.0.0
# add basic codes,import os
import os

# show the welcome
print("welcome to the OS!Now ,you can use it!!!")
print("please type 'help' to show the help")
# the main body of the os
while True:
    input_code: str = input(">>>")  # get ready to receive the code
    # help screen
    if input_code == 'help':
        print("欢迎使用本窗口，没想到吧，此OS支持（仅支持)中文呦""但由于python的问题，所以暂且还是需要输入英文指令~~~")
        print("about:关于此OS" "  ""help：显示此帮助" "  " "exit：退出此OS" "  " "open:打开本地文件")
    # exit the os
    elif input_code == "exit":
        exit()
    # about screen
    elif input_code == "about":
        print("版本号：0.0.0")
    # os model to open files
    elif input_code == "open":
        path = input("请输入文件路径及文件名(\请用双\代替。)")
        os.system(path)  # path为文件路径，本目录下可直接写文件名  os 为本地模块不需再行安装
