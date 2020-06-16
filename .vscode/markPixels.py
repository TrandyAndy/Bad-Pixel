import cv2
import numpy as np

def markPixels(bpm, bild):
    backtorgb = cv2.cvtColor(bild,cv2.COLOR_GRAY2RGB)
    backtorgb[0,0,1] = 65535
    cv2.imshow('image', backtorgb)
    print(backtorgb)
    cv2.imwrite('redPixels.png', backtorgb, [cv2.IMWRITE_PNG_COMPRESSION,0])
    cv2.waitKey()
    cv2.destroyAllWindows()
    

