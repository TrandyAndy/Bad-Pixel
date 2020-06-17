import cv2
import numpy as np

def markPixels(bpm, pBild, schwelle=100, bgr = 1):
    cv2.imwrite('PictureWithNoMarkings.png', pBild, [cv2.IMWRITE_PNG_COMPRESSION,0])
    colorPicture = cv2.cvtColor(pBild,cv2.COLOR_GRAY2RGB)
    hoehe, breite = np.shape(pBild)
    for z in range(hoehe):
        for s in range(breite):
            if(bpm[z,s] >= schwelle):
                colorPicture = drawPlus(colorPicture, z, s, hoehe, breite, bgr)
    #cv2.imshow('image', colorPicture)
    print(colorPicture)
    cv2.imwrite('PictureWithMarkings.png', colorPicture, [cv2.IMWRITE_PNG_COMPRESSION,0])
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    

def drawPlus(colorPicture, zeile, spalte,  hoehe, breite, bgr, wert = 65535,):
    colorPicture[bottom(zeile-2),spalte,bgr] = wert
    colorPicture[bottom(zeile-1),spalte,bgr] = wert
    colorPicture[zeile,bottom(spalte-2),bgr] = wert
    colorPicture[zeile,bottom(spalte-1),bgr] = wert
    colorPicture[zeile,top(spalte+1,breite),bgr] = wert
    colorPicture[zeile,top(spalte+2,breite),bgr] = wert
    colorPicture[top(zeile+1,hoehe),spalte,bgr] = wert
    colorPicture[top(zeile+2,hoehe),spalte,bgr] = wert
    return colorPicture
    

def bottom(aktuellerWert, minWert = 0):
    if(aktuellerWert < minWert):
        return minWert
    else:
        return aktuellerWert

def top(aktuellerWert, maxWert):
    if(aktuellerWert > maxWert):
        return maxWert
    else:
        return aktuellerWert