# $language = "Python"
# $interface = "1.0"
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

objTab = crt.GetScriptTab()
nowtime = time.strftime('%Y%m%d')
nowmonth = time.strftime('%Y-%m')
backupDir = "D:\\数通设备备份\\"


def os():
    """
    判断设备厂家
    return swType
    """
    objTab.Screen.Synchronous = True
    objTab.Screen.IgnoreEscape = True
    objTab.Screen.IgnoreCase = True
    objTab.Screen.Send("\r\n")
    swType_list = []
    symbol = objTab.Screen.WaitForStrings(["#", ">"], 3)
    if symbol == 1:
        objTab.Screen.Send("show version" + "\r")
        if objTab.Screen.WaitForString("Ruijie", 5):
            # crt.Dialog.MessageBox("1")
            swType_list.append("Ruijie")
    elif symbol == 2:
        objTab.Screen.Send("display version | include Copyright\r")
        swType = objTab.Screen.WaitForStrings(
            ["Unknown command", "HUAWEI", "H3C", "Ruijie"], 5)  # 迪普命令行特殊，>
        if swType == 1:
            objTab.Screen.Send("show version" + "\r")
            swType = objTab.Screen.WaitForStrings(
                ["Unknown command", "HUAWEI", "H3C", "Ruijie", "DPtech"], 5)
            if swType == 5:
                swType_list.append("DPtech")
        if swType == 2:
            swType_list.append("HUAWEI")
        elif swType == 3:
            swType_list.append("H3C")
        elif swType == 4:
            swType_list.append("Ruijie")
    # crt.Dialog.MessageBox("swtype"+str(swType_list))
    return swType_list


def Huawei():
    objTab.Screen.WaitForString(">")
    objTab.Screen.Send("screen-length 0 temporary" + "\r")
    objTab.Screen.WaitForString(">")
    objTab.Screen.Send(
        "display current-configuration | include sysname" + "\r")
    time.sleep(0.1)
    get_sysname = objTab.Screen.ReadString(">")  # str
    get_sysname_list = get_sysname.split('\r\n')  # list
    for i in get_sysname_list:
        if ('sysname' in i):
            sysname_list = i.split()
            sysname = sysname_list[-1]
    objTab.Session.LogFileName = backupDir + nowmonth + \
        "\\" + sysname + "_" + nowtime + ".log"
    objTab.Session.Log(False)
    objTab.Session.Log(True)
    objTab.Screen.Send("display current-configuration" + "\r")
    objTab.Screen.WaitForString("<" + sysname + ">")
    objTab.Screen.Send("\r")
    objTab.Screen.WaitForString("<" + sysname + ">")
    objTab.Session.Log(False)
    objTab.Screen.Send("undo screen-length temporary" + "\r")
    crt.Dialog.MessageBox("华为设备配置备份完成！目录D:\数通设备备份")


def H3C():
    objTab.Screen.WaitForString(">")
    objTab.Screen.Send("screen-length disable" + "\r")
    objTab.Screen.WaitForString(">")
    objTab.Screen.Send(
        "display current-configuration | include sysname" + "\r")
    get_sysname = objTab.Screen.ReadString(">")  # str
    get_sysname_list = get_sysname.split('\r\n')  # list
    for i in get_sysname_list:
        if ('sysname' in i):
            sysname_list = i.split()
            sysname = sysname_list[-1]
    objTab.Session.LogFileName = backupDir + nowmonth + \
        "\\" + sysname + "_" + nowtime + ".log"
    objTab.Session.Log(False)
    objTab.Session.Log(True)
    objTab.Screen.Send("display current-configuration" + "\r")
    objTab.Screen.WaitForString("<" + sysname + ">")
    objTab.Screen.Send("\r")
    objTab.Screen.WaitForString("<" + sysname + ">")
    objTab.Session.Log(False)
    objTab.Screen.Send("undo screen-length disable" + "\r")
    crt.Dialog.MessageBox("华三设备配置备份完成！目录D:\数通设备备份")


def ruijie():
    objTab.Screen.WaitForString("#")
    objTab.Screen.Send("terminal length 0" + "\r")
    objTab.Screen.WaitForString("#")
    objTab.Screen.Send(
        "show running-config | include hostname" + "\r")
    get_sysname = objTab.Screen.ReadString("#")  # str
    # crt.Dialog.MessageBox(get_sysname)
    get_sysname_list = get_sysname.split('\r\n')  # list
    for i in get_sysname_list:
        if ('hostname' in i):
            sysname_list = i.split()
            sysname = sysname_list[-1]
            # crt.Dialog.MessageBox(sysname)
    objTab.Session.LogFileName = backupDir + nowmonth + \
        "\\" + sysname + "_" + nowtime + ".log"
    objTab.Session.Log(False)
    objTab.Session.Log(True)
    objTab.Screen.Send("show running-config" + "\r")
    objTab.Screen.WaitForString(sysname + "#")
    objTab.Screen.Send("\r")
    objTab.Screen.WaitForString(sysname + "#")
    objTab.Session.Log(False)
    objTab.Screen.Send("terminal no length" + "\r")
    crt.Dialog.MessageBox("锐捷设备配置备份完成！目录D:\数通设备备份")


def DPtech():
    objTab.Screen.WaitForString(">")
    objTab.Screen.Send("terminal line 0" + "\r")  #取消分屏显示
    objTab.Screen.WaitForString(">")
    objTab.Screen.Send(
        "show running-config | include sysname" + "\r")
    get_sysname = objTab.Screen.ReadString(">")  # str
    get_sysname_list = get_sysname.split('\r\n')  # list
    for i in get_sysname_list:
        if ('sysname' in i):
            sysname_list = i.split()
            sysname = sysname_list[-1]
    objTab.Session.LogFileName = backupDir + nowmonth + \
        "\\" + sysname + "_" + nowtime + ".log"
    objTab.Session.Log(False)
    objTab.Session.Log(True)
    objTab.Screen.Send("show running-config" + "\r")
    objTab.Screen.WaitForString(sysname + ">")
    objTab.Screen.Send("\r")
    objTab.Screen.WaitForString(sysname + ">")
    objTab.Session.Log(False)
    #objTab.Screen.Send("terminal line 100" + "\r")
    crt.Dialog.MessageBox("迪普设备配置备份完成！目录D:\数通设备备份")


def main():
    swType_list = os()
    for i in swType_list:
        if i == "HUAWEI":  # 华为
            Huawei()
        elif i == "H3C":  # 华三
            H3C()
        elif i == "Ruijie":  # 锐捷
            ruijie()
        elif i == "DPtech":
            DPtech()  # 迪普


main()
