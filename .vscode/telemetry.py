import cv2
import numpy as np
import matplotlib.pyplot as plt
import cProfile
import detection
import os
from datetime import datetime


def markPixels(bpm, pBild, schwelle=100, bgr = 1, Bildname="Bildname", Algorithmus="Suchalgorithmus", Parameter="Parameter"):
    cv2.imwrite(Bildname + "_original.png", pBild, [cv2.IMWRITE_PNG_COMPRESSION,0])
    colorPicture = cv2.cvtColor(pBild,cv2.COLOR_GRAY2RGB)
    if(np.shape(pBild) !=np.shape(bpm)):        # Wann kann das passieren?
        print("Digga schau das die Dimensionen passen!")
    hoehe, breite = np.shape(pBild)
    for z in range(hoehe):
        for s in range(breite):
            if(bpm[z,s] >= schwelle):
                colorPicture = drawPlus(colorPicture, z, s, hoehe, breite, bgr)
    #cv2.imshow('image', colorPicture)
    #print(colorPicture)
    #for index in range(10):
        #cv2.imwrite(Bildname + "_" + Algorithmus + "_" + Parameter + str(index) + ".png", colorPicture, [cv2.IMWRITE_PNG_COMPRESSION,index])
    cv2.imwrite(Bildname + "_" + Algorithmus + "_" + Parameter + ".png", colorPicture, [cv2.IMWRITE_PNG_COMPRESSION,1])
    #print("Bild gespeichert ;D")
    #cv2.waitKey()
    #cv2.destroyAllWindows()

# Daten: 2-D Array (1. Spalte: eingestellter Parameter, 2. Spalte: dazugehöriger Funktionswert, z.B. Fehleranzahl)
# Bildname: String Name des gespeicherten Bildes
# Algorithmus: String Verwendeter Suchalgorithmus
# Parameter: String Modifizierter Parameter     
def plotData(Daten, Bildname="Bildname", Algorithmus="Suchalgorithmus", Parameter="Parameter"):    
    plt.plot(Daten[0], Daten[1], Daten[0], Daten[1], 'kx')
    plt.xlabel(Parameter)
    plt.ylabel('gefunde Fehler')
    plt.title(Bildname + " - " + Algorithmus + " - " + Parameter)
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.grid(True)
    aktuelleZeit = str(datetime.now())[:-7].replace(":","-") # aktuelle Zeit mit Datum und Uhrzeit
    #plt.savefig(Bildname + "_" + Algorithmus + "_" + Parameter + "_" + aktuelleZeit, bbox_inches='tight', dpi=300)
    plt.savefig(Bildname + "_" + Algorithmus + "_" + Parameter + "_" + "_lin", bbox_inches='tight', dpi=300)
    #plt.show()

def plotDataLog(Daten, Bildname="Bildname", Algorithmus="Suchalgorithmus", Parameter="Parameter"):    
    plt.plot(Daten[0], Daten[1], Daten[0], Daten[1], 'kx')
    plt.xlabel(Parameter)
    plt.ylabel('gefunde Fehler')
    plt.title(Bildname + " - " + Algorithmus + " - " + Parameter)
    plt.xscale('linear')
    plt.yscale('symlog')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.grid(True)
    aktuelleZeit = str(datetime.now())[:-7].replace(":","-") # aktuelle Zeit mit Datum und Uhrzeit
    print(aktuelleZeit)
    #plt.savefig(Bildname + "_" + Algorithmus + "_" + Parameter + "_" + aktuelleZeit + "_log", bbox_inches='tight', dpi=300)
    plt.savefig(Bildname + "_" + Algorithmus + "_" + Parameter + "_" + "_log", bbox_inches='tight', dpi=300)
    #plt.show()


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


def logDetection(pBild, bpmFehlerSchwellert = 100, startwert = 0, stopwert = 2, messpunkte = 10):
    xArray = np.linspace(start= startwert, stop= stopwert, num= messpunkte,dtype= np.float) # erstellen von der x-Achse
    yArray = np.zeros((messpunkte),dtype= np.float) # erstellen von der y-Achse
    hoehe, breite = np.shape(pBild[0])
    bpm = np.zeros((hoehe,breite))
    print("Das x-Array: ", xArray, type(xArray))
    print("Das y-Array: ", yArray, type(yArray))
    aktuelleZeit = str(datetime.now())[:-7].replace(":","-") # aktuelle Zeit mit Datum und Uhrzeit
    aktuellerPfad = "Testbilder/" + aktuelleZeit
    os.mkdir(aktuellerPfad)
    for index in range(len(xArray)):
        #bpm = detection.movingWindow(pBild,xArray[index],1000)
        bpm = detection.advancedMovingWindow(pBild,0,Faktor=xArray[index]) [0]
        print("Aktuelle Messreihe: ", index)
        #markPixels(bpm, pBild, bpmFehlerSchwellert, 1,  aktuellerPfad + "/Bildserie1_160kV_70uA", "Advanced Moving Window", "Fensterbreite_" + "{:.3f}".format(round(xArray[index],3))   )
        markPixels(bpm, pBild[0], bpmFehlerSchwellert, 1,  aktuellerPfad + "/Bildserie1_160kV_70uA", "Advanced Moving Window", "Fensterbreite_" + "{:.3f}".format(round(xArray[index],3))   )
        for z in range(hoehe):
            for s in range(breite):
                if bpm[z,s] >= bpmFehlerSchwellert:
                    yArray[index] += 1 
    dataArray = np.array([xArray, yArray],dtype= np.float)
    print(dataArray)
    #plotData(dataArray,"Bildserie1_160kV_70uA","Moving Window", "Schwellwert Dead-Pixel")
    #plotDataLog(dataArray,"Bildserie1_160kV_70uA","Moving Window", "Schwellwert Dead-Pixel")
    #aktuelleZeit = "test"
    np.savetxt(aktuellerPfad + "/messdaten.csv", dataArray, delimiter=";", fmt="%1.3f")
    plotData(dataArray, aktuellerPfad + "/Bildserie1_160kV_70uA","Advanced Moving Window", "Fensterbreite")
    plotDataLog(dataArray, aktuellerPfad + "/Bildserie1_160kV_70uA","Advanced Moving Window", "Fensterbreite_")