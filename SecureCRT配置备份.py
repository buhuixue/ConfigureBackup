# $language = "Python"
# $interface = "1.0"
import time


def Huawei():

    crt.Session.Log(False)  # 关闭日志记录
    crt.Session.Log(True)  # 开启日志记录
    crt.Screen.Send("display current-configuration all\r\n")
    crt.Screen.IgnoreEscape = True  # 不获取特殊字符（回车、换行符号）
    msg = crt.Screen.ReadString(["^", "More", "Unknown"], 2)
    index = crt.Screen.MatchIndex

    if index == 1: #华三部分

        time.sleep(1)
        crt.Screen.Send("display current-configuration\r\n")
        while True:
            if crt.Screen.ReadString("More", 1):
                crt.Screen.Send(" ")
            else:
                break

    elif index == 2: #华为部分
        crt.Screen.Send("\r\n")
        while True:
            if crt.Screen.ReadString("More", 1):
                crt.Screen.Send(" ")
            else:
                break
    elif index == 3: #迪普部分
        crt.Screen.Send("show running-config\r\n")
        while True:
            if crt.Screen.ReadString("More", 3):
                time.sleep(0.5)
                crt.Screen.Send(" ")
            else:
                break
    else:
        crt.Dialog.MessageBox("未能判断设备")

    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString(">")  # 等待出现特定字符
    crt.Session.Log(False)  # 关闭日志记录
    crt.Dialog.MessageBox("备份完成！")


def Cisco():

    crt.Session.Log(False)  # 关闭日志记录
    crt.Session.Log(True)  # 开启日志记录
    crt.Screen.Send("show running-config\r\n")
    crt.Screen.IgnoreEscape = True  # 不获取特殊字符（回车、换行符号）
    while True:
        if crt.Screen.WaitForString("More", 1):
            crt.Screen.Send(" ")
        else:
            break
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("#")  # 等待出现特定字符
    crt.Session.Log(False)  # 关闭日志记录
    crt.Dialog.MessageBox("备份完成！")


def main():

    crt.Screen.Send("\r\n")
    DeviceType = crt.Screen.ReadString([">", "#"], 2)
    index = crt.Screen.MatchIndex
    if (index == 1):
        # crt.Dialog.MessageBox("huawei")
        col_num = crt.Screen.CurrentColumn  # 光标列坐标
        row_num = crt.Screen.CurrentRow  # 光标行坐标
        col2 = col_num - 2
        sw_name = crt.Screen.Get(row_num, 2, row_num, col2)  # 获取指定坐标
        crt.Session.LogFileName = sw_name+".log"  # 会话日志名字
        Huawei()

    elif (index == 2):
        col_num = crt.Screen.CurrentColumn  # 光标列坐标
        row_num = crt.Screen.CurrentRow  # 光标行坐标
        col2 = col_num - 2
        sw_name = crt.Screen.Get(row_num, 1, row_num, col2)  # 获取指定坐标
        crt.Session.LogFileName = sw_name+".log"  # 会话日志名字
        Cisco()

    # elif (index == 3):
    #     col_num = crt.Screen.CurrentColumn  # 光标列坐标
    #     row_num = crt.Screen.CurrentRow  # 光标行坐标
    #     col2 = col_num - 2
    #     sw_name = crt.Screen.Get(row_num, 2, row_num, col2)  # 获取指定坐标
    #     crt.Session.LogFileName = sw_name+".log"  # 会话日志名字
    #     Cisco()
        
    else:
        crt.Dialog.MessageBox("timeout")


main()
