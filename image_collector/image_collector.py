import cv2 as cv
import os
import shutil

dirname = '/home/khsunkh/data_prepare/yawn_prepare'
anotherimgsavedir = os.path.join(dirname, 'anther')

if os.path.exists(anotherimgsavedir) is False:
    os.makedirs(anotherimgsavedir)

namelist = os.listdir(dirname)

for imgname in namelist:

    # print(imgname)
    filename = os.path.join(dirname, imgname)

    if os.path.isdir(filename):
        continue

    img = cv.imread(filename)

    cv.imshow("show", img)
    c = cv.waitKey(0)

    if c & 0xFF == ord('f'):
        pass
    elif c & 0xFF == ord('a'):
        anotherfilename = os.path.join(anotherimgsavedir, imgname)
        shutil.move(filename, anotherfilename)
    elif c & 0xFF == ord('q'):
        break


