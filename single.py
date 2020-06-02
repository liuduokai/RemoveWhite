import cv2
import os

# def GetCoordinate()
# 简单实现了去除导出图片白色边框的功能
# TODO:1.将求坐标点的功能封装成函数
#      2.考虑优化运算速度，引入多线程，同时对多行进行检测
#      3.考虑优化算法，遍历效率过低

if __name__ == '__main__':

    img = cv2.imread("2.jpg")
    sp = img.shape
    hei = sp[0]
    wid = sp[1]

    i = 0
    j = 0

    p1x = 0
    p1y = 0
    p2x = 0
    p2y = 0
    # 初始化左上角和右下角点的初始值

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # print(hei, wid)
    # print(i <= hei)
    # print(i < hei)
    # print(p1y == 0)
    while i < hei and p1y == 0:
        # print("in p1y")
        while j < wid:
            # print(gray[i, j])
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
    # print(p1x, p1y, i, j)
    # print(p1x, p1y, p2x, p2y)

    cropped = img[p1y:p2y, p1x:p2x]
    cv2.imwrite("./3.jpg", cropped)
