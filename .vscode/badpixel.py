 
"""
/*
 * @Author: Julian Schweizerhof
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-05-26 20:13:55
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-06-15 18:03:53
 * @Description: 
 */
 """


         
#import matplotlib.pyplot as plt
import numpy as np
#how to import numpy und ov2.  Python updaten, pip install, pip3 install numpy, pip3 install opencv-python.

import detection
import correction
import config
import importPictures as imP
import cv2
import telemetry

def pure_python_version(zahl):
    print(zahlig)
    X = np.arange(zahl)
    Y = np.arange(zahl)
    return X + Y


#detection.test(3)
#detection.test(config.Bildhoehe)


#importPath = "Bildserie4_75kV_20uA.his"
importPath = "Bildserie1_160kV_70uA.his"
bildDaten = imP.hisImportFunction(importPath,False)

#Beispiel
#anzahlBilder, anzahlZeilen, anzahlReihen = np.shape(bildDaten)
#print("Anzahl der Bilder: ", anzahlBilder, "Anzahl der Zeilen: ",anzahlZeilen, "Anzahl der Spalten: ",anzahlReihen)
#Beispiel Ende

#9 Pixel Testbild
TestImage=np.array([ [[0, 65535], [121, 65535]],
               [[35535, 35535], [0, 65535]],
               [[311, 65535], [321, 65535]] ])  # 3D Array


#ab hier Quasi die main:
#k=detection.MultiPicturePixelCompare(bildDaten[0:2])[0]
#anzahlZeilen, anzahlReihen = np.shape(k)
#print("Anzahl der Zeilen: ",anzahlZeilen, "Anzahl der Spalten: ",anzahlReihen)
#telemetry.markPixels( k, bildDaten[0], 50) 


#mP.markPixels( detection.MultiPicturePixelCompare(bildDaten[0:9])[0], bildDaten[0], 50) 
#mP.markPixels(detection.advancedMovingWindow(bildDaten, 0,6)[0],bildDaten[0])
#mP.markPixels(detection.movingWindow(bildDaten[0]),bildDaten[0])
#image = correction.nachbar(bildDaten[0],k)
#cv2.imwrite('PictureWithCorrection2.png', image, [cv2.IMWRITE_PNG_COMPRESSION,0])
#telemetry.markPixels(detection.advancedMovingWindow(bildDaten, 0,6)[0],bildDaten[0])
#telemetry.markPixels(detection.movingWindow(bildDaten[0]),bildDaten[0])
testArray = np.array([ [0, 10, 20], 
               [1, -7.8, 7],
               [2, -1, -10]
               ])   # 2D Array mit 3 Spalten und 3 Zeilen  # 2D Array mit 3 Spalten und 3 Zeilen
#telemetry.plotData(testArray)
#erg = cProfile.run('pure_python_version(zahlig)')
#cProfile.run("detection.movingWindow(bildDaten[0])")
telemetry.timeTest("telemetry","plotData(testArray)")


#print(timerObject.timeit(10))
#u=np.uint16(correction.nachbar(bildDaten[0],k))
#anzahlZeilen, anzahlReihen = np.shape(u)
#print("Anzahl der Zeilen: ",anzahlZeilen, "Anzahl der Spalten: ",anzahlReihen)

#cv2.imwrite('PictureWithCorrection.png', u , [cv2.IMWRITE_PNG_COMPRESSION,0])
#telemetry.markPixels(detection.advancedMovingWindow(bildDaten, 0,6)[0],bildDaten[0])
#telemetry.markPixels(detection.movingWindow(bildDaten[0]),bildDaten[0])
#telemetry.plotData()
