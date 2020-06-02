import os
import cv2
import datetime

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    path = "./input"
    files = os.listdir(path)

    for file in files:

        filePath = path + '/' + file
        outPath = "./output/" + file

        img = cv2.imread(filePath)

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
        cv2.imwrite(outPath, cropped)
        endtime = datetime.datetime.now()
    print("used ",end='')
    print((endtime - starttime).seconds, end='')
    print(" seconds", end='')
