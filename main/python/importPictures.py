"""
/*
 * @Author: Julian Schweizerhof
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-06-15 17:48:37
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-09-14 12:56:47
 * @Description: Python Programm um ein oder mehrere Bilder des Formats his zu importieren, To-Do: Datei in OpenCV Format importieren
 */
 """
import os                                                                   # Für die Path-Manipulation
import numpy as np                                                          # Für Arrays
import cv2                                                                  # Import OpenCV


def getNumberImages(pImportPath, rows, cols):                               # Funktion: Die Anzahl der Bilder in der Datei bestimmten, Rückgabewert: Anzahl Bilder
    file = open(pImportPath,'rb')                                           # File erneut öffnen, da ansonsten der "Cursor" falsch liegt
    data = np.fromfile(file,dtype=np.uint16)                                # komplettes File einlesen
    numberImages = (np.size(data) - 50) / (rows*cols)                       # Die Anzahl der Bilder bestimmen: die Größe des uint16 Arrays bestimmen, dann minus 50 Elemten (der Header der Datei) und dann geteilt durch die Pixel-Anzahl eines Bildes
    file.close()                                                            # File schließen
    return numberImages                                                    # Die Anzahl der Bilder zurückgeben

def hisImportFunction2(pImportPath, pExport = False):                        # Funktion: Bilder im HIS-Format importieren, Übergabewert: Path zum Bild
    pathWithoutExtension = os.path.splitext(pImportPath) [0]                # Pfad ohne Dateiendung erzeugen, .his wird entfernt
    print("\n\n*************************************************************")
    print("Funktion zum Einlesen von HIS-Dateien aufgerufen")
    print("*************************************************************\n")
    fileName, fileExtension = os.path.splitext(os.path.basename(pImportPath))# Dateinamen und Dateiendung extrahieren    
    print("Die Datei", fileName, "wird jetzt eingelesen.")
    fd = open(pImportPath,'rb')                                             # Das Bild öffnen im "rb"-Modus: read binary
    data = np.fromfile(fd,dtype=np.uint16, count=50)                        # Den Header 50 mal mit unsinged int 16 Bit einlesen (erste 100 Bytes)
    rows = int(np.take(data, 8))                                            # Reihen bestimmen, in int konvertieren, ansonsten overflow Error bei der Funktion fromfile()
    cols = int(np.take(data, 9))                                            # Spalten bestimmen
    numberImages = int(getNumberImages(pImportPath, rows, cols))            # Anzahl der Bilder in der Datei bestimmen
    print("Ihre Datei hat", rows, "Reihen und", cols, "Spalten und besteht aus", numberImages, "Bild(ern)")

    for index in range(numberImages):                                       # Alle Bilder anzeigen und speichern
        f = np.fromfile(fd, dtype=np.uint16, count=rows*cols)               # Pixel lesen und in einem ein dimensionales Array speichern
        im = f.reshape((rows, cols)) 
                                              # Array in zwei dimensionales Array mit rows x cols erstellen
        #np.savetxt("foo.csv", im, delimiter=";")

        #for testValue in np.nditer(f):
        #    if testValue >= 60000:
        #        print("Sehr schwarz hier!")
        #plt.plot(im)
        #plt.show()
        if pExport == True:
            cv2.imshow('image', im)                                             # Array als Bild anzeigen
            cv2.imwrite(pathWithoutExtension+"_"+str(index)+'_beta.png',im, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
            print("Ihre Datei wurden unter", pathWithoutExtension+"_"+str(index)+".png gespeichert")
            cv2.waitKey()                                                       # Warten bis eine Taste gedrückt wird      
    if pExport == True:
        cv2.destroyAllWindows()                                                 # Alle Fenster schließen    
    fd.close()                                                              # File schließen
    return im


def hisImportFunction(pImportPath, pExport = False, pMittelwert = False):                        # Funktion: Bilder im HIS-Format importieren, Übergabewert: Path zum Bild
    pathWithoutExtension = os.path.splitext(pImportPath) [0]                # Pfad ohne Dateiendung erzeugen, .his wird entfernt
    print("\n\n*************************************************************")
    print("Funktion zum Einlesen von HIS-Dateien aufgerufen")
    print("*************************************************************\n")
    fileName, fileExtension = os.path.splitext(os.path.basename(pImportPath))# Dateinamen und Dateiendung extrahieren    
    print("Die Datei", fileName, "wird jetzt eingelesen.")
    fd = open(pImportPath,'rb')                                             # Das Bild öffnen im "rb"-Modus: read binary
    data = np.fromfile(fd,dtype=np.uint16, count=50)                        # Den Header 50 mal mit unsinged int 16 Bit einlesen (erste 100 Bytes)
    rows = int(np.take(data, 8))                                            # Reihen bestimmen, in int konvertieren, ansonsten overflow Error bei der Funktion fromfile()
    cols = int(np.take(data, 9))                                            # Spalten bestimmen
    numberImages = int(getNumberImages(pImportPath, rows, cols))            # Anzahl der Bilder in der Datei bestimmen
    print("Ihre Datei hat", rows, "Reihen und", cols, "Spalten und besteht aus", numberImages, "Bild(ern)")
    bildDaten = np.zeros((numberImages, rows, cols),dtype=np.uint16)                        # leeres 3D-Array der Bilddaten: 1. Nr. des Bildes, 2. Bildhöhe, 3. Bildbreite
    for index in range(numberImages):                                       # Alle Bilder anzeigen und speichern
        f = np.fromfile(fd, dtype=np.uint16, count=rows*cols)               # Pixel lesen und in einem ein dimensionales Array speichern
        im = f.reshape((rows, cols))                                        # Array in zwei dimensionales Array mit rows x cols erstellen
        bildDaten[index] = im                                               # Aktuelles Bild speichern
       #test 
        #backtorgb = cv2.cvtColor(im,cv2.COLOR_GRAY2RGB)
        #cv2.imshow('image2', backtorgb)
        #cv2.imwrite('asdfasf.png', backtorgb, [cv2.IMWRITE_PNG_COMPRESSION,0])
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        #Ende test
        if pExport == True:
            
            cv2.imshow('image', im)                                             # Array als Bild anzeigen
            cv2.imwrite(pathWithoutExtension+"_"+str(index)+'_beta.png',im, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
            print("Ihre Datei wurden unter", pathWithoutExtension+"_"+str(index)+".png gespeichert")
            cv2.waitKey()                                                       # Warten bis eine Taste gedrückt wird              
    if pExport == True:
        cv2.destroyAllWindows()                                                 # Alle Fenster schließen    
    
    if pMittelwert == True:
        meanImage = np.zeros([rows,cols],dtype=np.uint32)
        #print(meanImage)
        #print(np.size(bildDaten))
        #print(np.shape(meanImage))
        #print(np.shape(bildDaten)[0])
        for index in range(np.shape(bildDaten)[0]):     # Anzahl der Bilddateien
            meanImage = meanImage + bildDaten[index]
        meanImage = meanImage / np.shape(bildDaten)[0]
        ergMeanImage = np.array(meanImage, dtype=np.uint16)
        #print(ergMeanImage)

        
        cv2.imshow("Mittelwert",ergMeanImage)
        cv2.imwrite(pathWithoutExtension+ "_mittelwert.png",ergMeanImage, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
        print("Ihre Datei wurden unter", pathWithoutExtension + "_mittelwert.png gespeichert")
        cv2.waitKey()                                                       # Warten bis eine Taste gedrückt wird              
    fd.close()                                                              # File schließen
    return bildDaten

def importFunction(pImportPath, pExport = False): #vill noch ne fehlermeldung Wenn der Path kein Link enthält!?
    bild = cv2.imread(pImportPath, flags= -1)
    bildDaten = np.zeros( (1, np.shape(bild)[0], np.shape(bild)[1]), dtype=np.uint16)
    bildDaten[0] = bild
    #cv2.imshow('image', bildDaten[0])
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    if pExport == True:
        cv2.imshow('image', bild)                                             # Array als Bild anzeigen
        cv2.imwrite(os.path.splitext(os.path.basename(pImportPath)) [0] + "importiertesBild.png",bild, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
        cv2.waitKey()
        cv2.destroyAllWindows()      
    return bildDaten

def importUIFunction(pImportPath, pExport = False): # Rückgabe Bild-Array und Auflösung Breite und Höhe
    dateiEndung = os.path.splitext(os.path.basename(pImportPath)) [1]
    if dateiEndung == ".his": # Eine his-Datei
        bildDaten = importFunction(pImportPath)
    elif dateiEndung == ".png" or dateiEndung == ".jpg" or dateiEndung == ".jpeg" or dateiEndung == ".tif" or dateiEndung == ".tiff":
        bildDaten = importFunction(pImportPath)
    return bildDaten

def getAufloesungUndAnzahl(pImportPath):
    dateiEndung = os.path.splitext(os.path.basename(pImportPath)) [1]
    if dateiEndung == ".his": # Eine his-Datei
        fd = open(pImportPath,'rb')                                             # Das Bild öffnen im "rb"-Modus: read binary
        data = np.fromfile(fd,dtype=np.uint16, count=50)                        # Den Header 50 mal mit unsinged int 16 Bit einlesen (erste 100 Bytes)
        rows = int(np.take(data, 8))                                            # Reihen bestimmen, in int konvertieren, ansonsten overflow Error bei der Funktion fromfile()
        cols = int(np.take(data, 9))                                            # Spalten bestimmen
        fd.close()        
        anzahl = getNumberImages(pImportPath, rows, cols)                                                      # File schließen
    elif dateiEndung == ".png" or dateiEndung == ".jpg" or dateiEndung == ".jpeg" or dateiEndung == ".tif" or dateiEndung == ".tiff":
        bild = cv2.imread(pImportPath, flags= -1)
        rows = np.shape(bild)[0]
        cols = np.shape(bild)[1]
        anzahl = 1
    return rows, cols, anzahl
 
