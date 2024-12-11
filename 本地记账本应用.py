# 9-11行先取消注释来运行，创建本地txt之后再注释上重新运行

import json
import datetime
import PySimpleGUI as sg



# d = '[{"时间" : "2024/12/11 12:45:02" , "项目" : "收到货款" , "金额" : 20000, "分类" : "收入"}]'
# with open(r"data.txt", "w") as f:
#     f.write(d)

def readData(): #读取数据
    with open(r"data.txt", "r") as f:
        jsonData = f.read()
        dataList = json.loads(jsonData)
        return dataList

def writeData(dateList): #写入数据
    jsonData = json.dumps(dateList,ensure_ascii=False)  #把数据转换成json数据,保证数据里的汉字不会被篡改
    with open(r"data.txt","w") as f:
        jsonData = f.write(jsonData)
        sg.popup('账单录入成功')

# print(readData())
def showData(): #账单显示函数
    data = readData()
    dataLists = []
    for d in data:
        if d["分类"] == "收入":#收入和支出需要转换
            dataList = [d["时间"],d["项目"],d["金额"],d["分类"]]
            dataLists.append(dataList)
        else:
            dataList = [d["时间"], d["项目"], d["金额"]*-1, d["分类"]]
            dataLists.append(dataList)
    return dataLists

# print(showData())

def sumin(): #总收入计算
    sumin = 0
    data = readData()
    for d in data:
        if d["分类"] == "收入":
            sumin += d["金额"]
    return sumin
# print(sumin())

def sumout(): #总支出计算
    sumout = 0
    data = readData()
    for d in data:
        if d["分类"] == "支出":
            sumout += d["金额"]
    return sumout
# print(sumout())

def addData(content,amount,cla): #接收项目金额分类/增加数据函数
    dataList = readData()
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    data = {"时间":t,"项目":content,"金额":amount,"分类":cla}
    dataList.append(data)
    writeData(dataList)

#----------------------------------------------------------------------
def main():
    list = showData()
    sin =sumin()
    sout = sumout()
    layout = [
        [sg.T("账目清单:")],
        [sg.Table(list,headings=["时间","项目","金额","分类"],
                  key = "-show-",
                  justification = "c",
                  auto_size_columns = False,
                  def_col_width = 15
    )],
        [sg.T("总收入" + str(sin) + "元，总支出" + str(sout) + "元，结余" + str(sin - sout) + "元",key="-text-")],
        [sg.T("请输入账单项目:"),sg.In(key = "-content-")],
        [sg.T("请输入账单金额:"), sg.In(key = "-amount-")],
        [sg.T("请输入账单分类:")] + [sg.Radio(i,group_id=1,key=i) for i in ["收入","支出"]],
        [sg.B("确认提交")]

    ]

    window = sg.Window("记事本",layout)
    while True:
        event,values = window.read()
        if event == "确认提交":
            content = values["-content-"]
            amount = float(values["-amount-"])
            for k,v in values.items():
                if v == True:
                    cla = k
                    addData(content,amount,cla)
                    list = showData()
                    sin = sumin()
                    sout = sumout()
                    text ="总收入" + str(sin) + "元，总支出" + str(sout) + "元，结余" + str(sin - sout) + "元"
                    window["-show-"].update(values = list)
                    window["-text-"].update(value = text)
                    window["-content-"].update("")
                    window["-amount-"].update("")
        if event == None:
            break
    window.close()

main()
