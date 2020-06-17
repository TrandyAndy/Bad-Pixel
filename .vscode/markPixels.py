import cv2
import numpy as np

def markPixels(bpm, pBild, schwelle=100):
    colorPicture = cv2.cvtColor(pBild,cv2.COLOR_GRAY2RGB)
    hoehe, breite = np.shape(pBild)
    for z in range(hoehe):
        for s in range(breite):
            if(bpm[z,s] >= schwelle):
                colorPicture = drawPlus(colorPicture, z, s)
    #cv2.imshow('image', colorPicture)
    print(colorPicture)
    cv2.imwrite('greenPixels.png', colorPicture, [cv2.IMWRITE_PNG_COMPRESSION,0])
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    

def drawPlus(colorPicture, zeile, spalte, bgr = 1, wert = 65535):
    colorPicture[zeile-2,spalte,bgr] = wert
    colorPicture[zeile-1,spalte,bgr] = wert
    colorPicture[zeile,spalte-2,bgr] = wert
    colorPicture[zeile,spalte-1,bgr] = wert
    colorPicture[zeile,spalte+1,bgr] = wert
    colorPicture[zeile,spalte+2,bgr] = wert
    colorPicture[zeile+1,spalte,bgr] = wert
    colorPicture[zeile+2,spalte,bgr] = wert
    return colorPicture
    

