import cv2
import numpy as np
import matplotlib.pyplot as plt
import cProfile 

def markPixels(bpm, pBild, schwelle=100, bgr = 1):
    cv2.imwrite('PictureWithNoMarkings.png', pBild, [cv2.IMWRITE_PNG_COMPRESSION,0])
    colorPicture = cv2.cvtColor(pBild,cv2.COLOR_GRAY2RGB)
    if(np.shape(pBild) !=np.shape(bpm)):
        print("Digga schau das die Dimensionen passen!")
    hoehe, breite = np.shape(pBild)
    for z in range(hoehe):
        for s in range(breite):
            if(bpm[z,s] >= schwelle):
                colorPicture = drawPlus(colorPicture, z, s, hoehe, breite, bgr)
    #cv2.imshow('image', colorPicture)
    #print(colorPicture)
    cv2.imwrite('PictureWithMarkings.png', colorPicture, [cv2.IMWRITE_PNG_COMPRESSION,0])
    print("Bild gespeichert ;D")
    #cv2.waitKey()
    #cv2.destroyAllWindows()

# Daten: 2-D Array (1. Spalte: eingestellter Parameter, 2. Spalte: dazugehöriger Funktionswert, z.B. Fehleranzahl)
# Bildname: String Name des gespeicherten Bildes
# Algorithmus: String Verwendeter Suchalgorithmus
# Parameter: String Modifizierter Parameter     
def plotData(Daten, Bildname="Bildname", Algorithmus="Suchalgorithmus", Parameter="Parameter"):    
    plt.plot(Daten[0], Daten[1], Daten[0], Daten[1], 'kx')
    plt.xlabel('parametrisierte Werte')
    plt.ylabel('gefunde Fehler')
    plt.title(Bildname + " - " + Algorithmus + " - " + Parameter)
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.grid(True)
    plt.savefig(Bildname, bbox_inches='tight', dpi=300)
    plt.show()
    


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
    if(aktuellerWert > maxWert-1):
        return maxWert-1
    else:
        return aktuellerWert

def timeTest(pythonFile = "detection", funktionsAufruf = "movingWindow(bildDaten[0])" ):
    cProfile.run(pythonFile + "." + funktionsAufruf)