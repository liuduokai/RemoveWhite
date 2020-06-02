import cv2


if __name__ == '__main__':

    img = cv2.imread("1.jpg")
    path = "./input/"
    i = 0
    while i < 1000:
        filepath = path + str(i)
        filepath = filepath+".jpg"
        cv2.imwrite(filepath, img)
        i = i+1