# coding:utf-8
# remove carrot background


import cv2
import cv2.cv as cv

filename = 'carrot.png'

def open_file(filename):
    im = cv2.imread(filename)
    print("read "+ filename + " finish.")
    return im


#todo filter pic
def filter_carrot(im):
    # convert to gray pic
    after = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # convert gray pic to binary
    ret, binary = cv2.threshold(after, 120, 255, cv2.THRESH_BINARY)
    print(ret)
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im, contours, -1, (0,222,255), 2)
    cv2.imshow("img", im)
    cv2.waitKey()
    cv2.imwrite("bin.png", binary)



def random_carrot(im):
    # go though all the dot, and set pic as a matrix
    im = cv.LoadImage(filename)
    for i in range(im.height):
        for j in range(im.width):
            #print(im[i, j])
            pass



im = open_file(filename)
print(im[271, 42])
# go_through(im)
#filter_carrot(im)
random_carrot(im)

