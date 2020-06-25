 
"""
/*
 * @Author: Julian Schweizerhof
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-05-26 20:13:55
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-06-21 01:32:30
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
import cProfile 
import verpixler


#detection.test(3)
#detection.test(config.Bildhoehe)
#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Daten/Aufnahmen zur Korrektur Panel/Serie 1/Bildserie1_160kV_0uA.his"
#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Daten/Aufnahmen zur Korrektur Panel/Serie 1/Bildserie1_160kV_70uA.his"
importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Daten/Aufnahmen zur Korrektur Panel Version 2/Serie2/Bildserie2_160kV_70uA_mittelwert.png"
#importPath = "Bildserie4_75kV_20uA.his"
#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Daten/Aufnahmen zur Korrektur Panel Version 2/Serie4/Bildserie4_75kV_20uA.his"
#
# 
#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Daten/Aufnahmen zur Korrektur Panel Version 2/Serie2/Bildserie2_160kV_70uA.his"



#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Daten/Aufnahmen zur Korrektur Panel Version 2/Serie2/Bildserie2_160kV_70uA_mittelwert.png"


#importPath = "SimBilder/Dunkelbild_Verpixelt.png"
#importPath = "SimBilder/HellBild_Verpixelt.png"
#importPath = "SimBilder/Simbild_Verpixelt.png"
#importPathBPM0 = "BMP_0.png"

#importPath = "Bildserie1_160kV_70uA.his"
#importPath =  "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/7. Evaluation und Tests/Messdaten Analyse/Simulationsbilder/dark_image_10_percent_rauschen.png"
#importPath = "simulationsbild.tif"
#bildDaten = imP.importFunction(importPath,True)
#bildDaten = imP.importFunction(importPath, True)

#bildDaten = imP.hisImportFunction(importPath)

bildDaten = imP.importFunction(importPath)
#BPM0 = imP.importFunction(importPathBPM0)

#Beispiel
#anzahlBilder, anzahlZeilen, anzahlReihen = np.shape(bildDaten)
#print("Anzahl der Bilder: ", anzahlBilder, "Anzahl der Zeilen: ",anzahlZeilen, "Anzahl der Spalten: ",anzahlReihen)
#Beispiel Ende

#9 Pixel Testbild
testImage=np.array([ [[0, 65535], [121, 65535]],
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
#cProfile.run('detection.advancedMovingWindow(bildDaten,0)')

#cProfile.run("detection.movingWindow(bildDaten[0])")
#telemetry.timeTest("telemetry","plotData(testArray)")
#telemetry.logDetection(bildDaten[0],startwert= 0,stopwert=1,messpunkte=5)
#telemetry.logDetection(bildDaten, startwert=1, stopwert=10, messpunkte=3) #7
###telemetry.logDetection(bildDaten[0],startwert= 0.5,stopwert=1,messpunkte=101)
#telemetry.timeTest("telemetry","logDetection2(bildDaten[0],startwert= 0,stopwert=1,messpunkte=50)")

#print(timerObject.timeit(10))
#u=np.uint16(correction.nachbar(bildDaten[0],k))
#anzahlZeilen, anzahlReihen = np.shape(u)
#print("Anzahl der Zeilen: ",anzahlZeilen, "Anzahl der Spalten: ",anzahlReihen)

# c,j=verpixler.verpixeln(bildDaten[0],190,7,8)
# cv2.imwrite('PictureWithPixels.png', c , [cv2.IMWRITE_PNG_COMPRESSION,0])
# cv2.imwrite('PictureBPM.png', j , [cv2.IMWRITE_PNG_COMPRESSION,0])

#cv2.imwrite('PictureWithCorrection.png', u , [cv2.IMWRITE_PNG_COMPRESSION,0])
#telemetry.markPixels(detection.advancedMovingWindow(bildDaten, 0,6)[0],bildDaten[0])
#telemetry.markPixels(detection.movingWindow(bildDaten[0]),bildDaten[0])
#telemetry.plotData()

#print("{:.3f}".format(5))
#print("{:.3f}".format(round(10,3)))
#str(round(xArray[index],3))





#Bild erszeugen:
# importPath = "Bildserie1_160kV_70uA.his"
# bildDaten = imP.hisImportFunction(importPath,False)
# Bilder=bildDaten[0:4]
# importPath = "Bildserie1_160kV_0uA.his"
# bildDaten = imP.hisImportFunction(importPath,False)
# Bilder[1]=bildDaten[0]
# importPath = "Bildserie2_160kV_70uA.his"
# bildDaten = imP.hisImportFunction(importPath,False)
# Bilder[2]=bildDaten[0]
# importPath = "Bildserie4_75kV_20uA.his"
# bildDaten = imP.hisImportFunction(importPath,False)
# Bilder[3]=bildDaten[0]
# u=detection.dynamicCheck(Bilder,1.1)[0]
# telemetry.markPixels(u,Bilder[0])
#cv2.imwrite('PictureWithMarks.png', u2 , [cv2.IMWRITE_PNG_COMPRESSION,0])
"""
Bild, BPM0=verpixler.verpixeln(bildDaten[0],190,7,8)
BPM1=detection.movingWindow(bildDaten[0])
BPM2=detection.advancedMovingWindow(bildDaten[0],10,5)[0]
verpixler.auswertung(BPM1,BPM0)
"""
"""
A,B,X,Anzahl=verpixler.Julian(bildDaten[0],bildDaten[1])
cv2.imshow('Hell',A)
cv2.imshow('Dunkel',B)
cv2.waitKey()
cv2.destroyAllWindows()
"""

#telemetry.logDetection(bildDaten[0],startwert= 0,stopwert=0.999,messpunkte=50)
#telemetry.logDetectionOld(bildDaten[0],startwert=0,stopwert=0.5,messpunkte=6)
"""
print(bildDaten[0,436,472])

print(np.size(bildDaten))

meanImage = np.zeros([512,512],dtype=np.uint32)
print(meanImage)
print(np.size(bildDaten))
print(np.shape(meanImage))
print(np.shape(bildDaten)[0])

for index in range(np.shape(bildDaten)[0]):
    meanImage = meanImage + bildDaten[index]
meanImage = meanImage / np.shape(bildDaten)[0]
ergMeanImage = np.array(meanImage, dtype=np.uint16)
print(ergMeanImage)

"""
# meanImage = meanImage + bildDaten[0] + bildDaten[1]

# meanImage = np.add(bildDaten[0], bildDaten[1])
# print(meanImage)
# print(type(meanImage))

telemetry.logDetectionOld(bildDaten[0],startwert= 0,stopwert=1,messpunkte=11)
#telemetry.logDetection(bildDaten[0],startwert= 0,stopwert=1,messpunkte=2)

#telemetry.logDetection(bildDaten,bpmFehlerSchwellert= 50, startwert= 0.00, stopwert= 0.12, messpunkte=7, BPM0=BPM0[0])
