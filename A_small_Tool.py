#要在cmd里运行
import getopt
import sys
import datetime
import os
import psutil
import threading
import time

list_of_disk = []
for disk in psutil.disk_partitions():
    list_of_disk.append(disk.device)

def Find0():
    i = 0
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass

def Find1():
    i = 1
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass

def Find2():
    i = 2
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass

def Find3():
    i = 3
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass

def Find4():
    i = 4
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass

def Find5():
    i = 5
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass

def Find6():
    i = 6
    if i < len(list_of_disk):
        for dirname, subdirList, fileList in os.walk(os.path.join(list_of_disk[i])):
            for fname in fileList:
                #print("正在为你查找%s" % (dirname + '\\' + fname))
                if fileName in str(fname):
                    os.system('explorer.exe %s' % dirname)
                else:
                    pass
    else:
        pass


def Use():
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v-t- ',['help','filename=','version','time'])
    for opt_name,opt_value in opts:
        if opt_name in (' '):
            print("[*] 使用时请先在命令行添加参数 -h 来获得使用帮助呦 ~")
            exit()
        if opt_name in ('-h','--help'):
            print("[*] Help info (你可真是个小机灵鬼儿~) \n  "
                  "没错下面就是使用说明啦 \n  "
                  "-v         check the version \n  "
                  "--version  check the version too ~ \n  "
                  "-f         add with filename(就是参数-f后面要加文件名啦) \n  "
                  "--filename 使用方法同上 \n  "
                  "-t 报时以及距离下班（放飞自我）时间")
            exit()
        if opt_name in ('-t','--time'):
            now_time = datetime.datetime.now()
            work_off = datetime.datetime(2019, 10, 17, 17, 30, 00)
            schdu_time = work_off + datetime.timedelta(days=1)
            differ = schdu_time - now_time
            h = differ.seconds // 60 // 60
            m = differ.seconds // 60 % 60
            print("[*] 现在是北京时间 %s ，离下班还有%s h %s min " % (now_time.strftime(('%Y-%m-%d %H:%M:%S')), h, m))
            exit()
        if opt_name in ('-v','--version'):
            print("[*] Version is 新鲜出炉 ")
            exit()
        if opt_name in ('-f','--filename'):
            global fileName
            fileName = opt_value
            #print("[*] Filename is ",fileName)
            print("[*] 即将为你精彩呈现  - %s -"% fileName)
            print("[*] 请耐心等待哦（os：30s内找得到算我输  略略略【鬼脸】）")
            print("[*] 文件名输错了找不到的话此juo本表示不背锅！")
            #这里用多线程查找每一个磁盘
            while True:
                try:
                    #input()  # 如果是 python 2.x 版本请使用 raw_input()
                    starttime = time.time()
                    print('开始查找')
                    try:
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find0).start()
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find1).start()
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find2).start()
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find3).start()
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find4).start()
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find5).start()
                        threading.Thread(target=Find0).setDaemon(True)
                        threading.Thread(target=Find6).start()
                    except KeyboardInterrupt:
                        print("结束查找")
                        break
                    while True:
                        print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
                        time.sleep(1)


                except KeyboardInterrupt:
                    print('结束')
                    endtime = time.time()
                    print('总共的时间为:', round(endtime - starttime, 2), 'secs')
                    break

            exit()

def main():

    try:
        Use()
    except getopt.GetoptError as error:
        print(error)
        print("[*]  忘记输入文件名了啊大哥")
        sys.exit(2)
    except KeyboardInterrupt as e:
        print(e)
        print("[*]  已中断查找")
    except NameError as ne:
        print(ne)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)
        print("[*]  已中断查找")
