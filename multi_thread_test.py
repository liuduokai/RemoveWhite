
import os
import cv2
import threading
from multiprocessing import Process
import _thread
import datetime


# 尝试使用多进程进行优化，效果拔群，
# 尝试使用多线程存在如下问题:
# 1.若调用之后无死循环保持程序不被结束，则线程未运行就与程序一起结束
# 2.若使用死循环保持程序运行，则存在无法自动退出及效率低下的问题
# TODO：找到可用的方法，能够保持程序不被结束，当进程运行完成后及时结束进程的解决方案

# 功能实现函数，为方便多进程调用实现
def CutWhite(InputPath, OutputPath):
    # print("in it")
    img = cv2.imread(InputPath)

    sp = img.shape
    hei = sp[0]
    wid = sp[1]

    i = 0
    j = 0

    p1x = 0
    p1y = 0
    p2x = 0
    p2y = 0

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    while i < hei and p1y == 0:
        while j < wid:
            if gray[i, j] == 0:
                p1y = i
                break
            j = j + 1
        j = 0
        i = i + 1

    i = 0
    j = 0

    while j < wid and p1x == 0:
        # print("in p1x")
        while i < hei:
            # print(gray[i, j])
            if gray[i, j] == 0:
                p1x = j
                break
            i = i + 1
        i = 0
        j = j + 1

    i = hei - 1
    j = wid - 1

    while i > 0 and p2y == 0:
        while j > 0:
            if gray[i, j] == 0:
                p2y = i
                break
            j = j - 1
        j = wid - 1
        i = i - 1

    i = hei - 1
    j = wid - 1

    while j > 0 and p2x == 0:
        while i > 0:
            if gray[i, j] == 0:
                p2x = j
                break
            i = i - 1
        i = hei - 1
        j = j - 1

    p1y = p1y - 1
    p1x = p1x - 1
    p2x = p2x + 1
    p2y = p2y + 1

    # 将左上角点向左向上移动1px，将右下点向右向下移动1px，防止将图像边缘裁切

    cropped = img[p1y:p2y, p1x:p2x]
    cv2.imwrite(OutputPath, cropped)


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    path = "./input"
    files = os.listdir(path)

# 遍历文件夹中的文件
    for file in files:
        inputPath = path + '/' + file
        outputPath = "./output/" + file

        # 多线程调用代码
        # _thread.start_new_thread(CutWhite, (inputPath, outputPath,))

        # 创建新进程
        t = Process(target=CutWhite, args=(inputPath, outputPath,))
        t.start()

    # 多线程时，程序保活代码
    # while threading.activeCount():
    #     pass

    # 时间测量代码
    endTime = datetime.datetime.now()
    print("used ", end='')
    print((endTime - startTime).seconds, end='')
    print(" seconds", end='')