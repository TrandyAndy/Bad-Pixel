 
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
import config
import importPictures as imP


#detection.test(3)
#detection.test(config.Bildhoehe)


#importPath = "/Users/julian/Google Drive/Studium/Master/1. Semester/Mechatronische Systeme/Mecha. Systeme/F&E Bad-Pixel/2. Stand der Technik - Recherche/Beispielbilder/Daten/Aufnahmen zur Korrektur Panel Version 2/Serie4/Bildserie4_75kV_20uA.his"
importPath = "Bildserie1_160kV_0uA.his"
bildDaten = imP.hisImportFunction(importPath,False)

#Beispiel
anzahlBilder, anzahlZeilen, anzahlReihen = np.shape(bildDaten)
print("Anzahl der Bilder: ", anzahlBilder, "Anzahl der Zeilen: ",anzahlZeilen, "Anzahl der Spalten: ",anzahlReihen)
#Beispiel Ende

#9 Pixel Testbild
TestImage=np.array([ [[111, 65535], [121, 65535]],
               [[35535, 35535], [221, 65535]],
               [[311, 65535], [321, 65535]] ])  # 3D Array

detection.movingWindow(bildDaten[0])
#ab hier Quasi die main:
detection.MultiPicturePixelCompare(bildDaten)
#detection.MultiPicturePixelCompare(TestImage)
