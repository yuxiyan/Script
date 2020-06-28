


import os
import time


def start_server():
    stop_server()
    cmd=f'appium -a 127.0.0.1 -p 4723 --log startlog.log --local-timezone  & '   #mac需要加&,不加后续程序无法运行
    os.system(cmd)
    print("启动成功")
    time.sleep(3)


def stop_server():

    p = os.popen(f'lsof -i tcp:4723')
    p0 = p.read()
    if p0.strip() != '':
        p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
        os.popen(f'kill {p1}')  # 结束进程
        print('appium server已结束')


start_server()














