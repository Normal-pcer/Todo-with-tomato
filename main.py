import time
import os

username = ""
tasklist = []
temp = {}

while True:
    with open("config.json", "r") as f:
        temp = f.read()
        temp = eval(temp)
        username = temp["username"]
        tasklist = temp["list"]
    print("Hello, "+username)
    print("*"*8+"任务列表"+"*"*8)
    for i in range(len(tasklist)):
        print("*", str(i+1)+".", tasklist[i])

    print("*"*8+"功能"+"*"*8)
    print("* 1. 添加任务")
    print("* 2. 删除任务")
    print("* 3. 启动番茄钟")
    ch = int(input("* 请选择:  "))
    if ch == 1:
        ch = input("* 请输入要添加的任务名: ")
        with open("config.json", "w") as f:
            temp["list"] = temp["list"] + [ch]
            f.write(str(temp).replace("'", '"'))
    elif ch == 2:
        ch = int(input("* 要删除任务的编号: "))
        tasklist.pop(ch-1)
        with open("config.json", "w") as f:
            temp["list"] = tasklist
            f.write(str(temp).replace("'", '"'))
    else:
        ch1 = int(input("* 要进行任务的编号: "))
        ch2 = int(input("* 每个番茄钟的时间(分钟): "))
        ch3 = int(input("* 休息时间(分钟): "))
        while True:
            for m in range(ch2-1, -1, -1):
                for s in range(59, -1, -1):
                    os.system("cls")
                    print("休息")
                    print("倒计时:", m, ":", s)
                    time.sleep(1)
    os.system("cls")
