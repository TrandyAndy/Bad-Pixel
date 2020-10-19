"""
/*
 * @Author: Julian Schweizerhof
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-09-18 15:07:37
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-09-18 14:42:32
 * @Description: Python Programm um ein Array als Bild speichern zu können
 */
 """
import numpy as np
import cv2
import os
from datetime import datetime

def exportPictures(pPath, pImagename, pImage, pZeit):  # pPath: Zielverzeichnis, pImagename: Name des Bildes, pImage: Array des Bildes
    # os.path.join() für Crossplatform-Funktionalität, fügt / oder \ je nach Betriebssystem
    
    aktuelleZeit = str(pZeit)
    dirName = os.path.join(pPath, "Korregierte Bilder vom " + aktuelleZeit)
    if os.path.exists(dirName):
        pass
    else:
        os.mkdir(dirName)
    fileName = pImagename +  "_korrigiert.png"
    #print("Image beim Exportieren: ", pImage, "Typ ist", type(pImage), "Shape ist: ", np.shape(pImage))
    
    cv2.imwrite(os.path.join(dirName, fileName), pImage, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
    print(os.path.join(pPath, pImagename))
    #print("exportPictures") # debug
