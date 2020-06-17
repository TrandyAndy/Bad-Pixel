import cv2
import numpy as np

def markPixels(bpm, bild):
    backtorgb = cv2.cvtColor(bild,cv2.COLOR_GRAY2RGB)
    # backtorgb[Zeile: 0, Spalte: 0, bgr: 1] = maximaler Wert: 65535
    backtorgb[99,201,2] = 65535
    backtorgb[100,201,2] = 65535
    backtorgb[101,199,2] = 65535
    backtorgb[101,200,2] = 65535
    backtorgb[101,202,2] = 65535
    backtorgb[101,203,2] = 65535
    backtorgb[102,201,2] = 65535
    backtorgb[103,201,2] = 65535
    #cv2.imshow('image', backtorgb)
    print(backtorgb)
    cv2.imwrite('redPixels.png', backtorgb, [cv2.IMWRITE_PNG_COMPRESSION,0])
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    

