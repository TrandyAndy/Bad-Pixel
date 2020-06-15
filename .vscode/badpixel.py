""" 
/*
 * @Author: Julian Schweizerhof
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-05-26 20:13:55
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-05-26 20:35:38
 * @Description: Python Programm um ein oder mehrere Bilder des Formats his zu importieren, To-Do: Datei in OpenCV Format importieren
 */
 """

import numpy as np                                                          # Für Arrays
import cv2                                                                  # Import OpenCV
                                                               # Für die Path-Manipulation
#import matplotlib.pyplot as plt

#how to import numpy und ov2.  Python updaten, pip install, pip3 install numpy, pip3 install opencv-python.

import detection
import config

detection.test(3)
detection.test(config.Bildhoehe)

#importPath = '/Users/julian/Desktop/test/Bildserie1_160kV_0uA.his' 
#importPath = "/Users/julian/Desktop/test/Bildserie1_160kV_0uA.his"
#importPath = "/Users/julian/Desktop/test/Bildserie2_160kV_70uA.his"

#importPath = "/Users/julian/Desktop/Bildserie1_160kV_0uA.his"
#importPath = "Bildserie1_160kV_0uA.his"
#bildArray = hisImportFunction(importPath,True)
#print(bildArray)

#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/2. Stand der Technik - Recherche/Beispielbilder/Daten/Aufnahmen zur Korrektur Panel Version 2/Serie4/Bildserie4_75kV_20uA.his"
importPath = "Bildserie3_160kV_0uA.his"


#ab hier Quasi die main:
detection.DeadPixelFinder(hisImportFunction(importPath))
