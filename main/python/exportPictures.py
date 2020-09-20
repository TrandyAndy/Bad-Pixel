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
import numpy
import cv2
import os

def exportPictures(pPath, pImagename, pImage):  # pPath: Zielverzeichnis, pImagename: Name des Bildes, pImage: Array des Bildes
    # os.path.join() für Crossplatform-Funktionalität, fügt / oder \ je nach Betriebssystem
    cv2.imwrite(os.path.join(pPath, pImagename) + "_korrigiert.png", pImage, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
    print(os.path.join(pPath, pImagename))
    #print("exportPictures") # debug
