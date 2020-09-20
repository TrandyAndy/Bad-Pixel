"""
/*
 * @Author: Julian Schweizerhof und Andreas Bank
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-09
 * @Last Modified by: 
 * @Last Modified time: 
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

""" Pfad der Bilddateien:______________________________________________________________________________________ """
importPath = "FFC_Bilder\Bildserie2_160kV_70uA_mittelwert.png"
importPath_Hell = "FFC_Bilder\Bildserie1_160kV_70uA_mittelwert.png" #MW Bild
importPath_Dunkel = "FFC_Bilder\Bildserie1_160kV_0uA_mittelwert.png"


""" Import der Bilddateien:______________________________________________________________________________________ """
bildDaten = imP.importFunction(importPath)
bildDaten_Hell = imP.importFunction(importPath_Hell)
bildDaten_Dunkel = imP.importFunction(importPath_Dunkel)


""" Aufruf der Detection Funktion:______________________________________________________________________________________ """
if False:
    BAD=detection.advancedMovingWindow(bildDaten[0],Faktor=3)[0] #F=4

""" Aufruf der Correction Funktion:______________________________________________________________________________________ """
if True:
    GOOD=np.uint16(correction.Flatfield(bildDaten[0],bildDaten_Hell[0],bildDaten_Dunkel[0])[0])

""" Audgabe der Bilder Plots und Ergebnisse:______________________________________________________________________________________ """

cv2.imwrite("_korriegiert Flatfield.png", GOOD, [cv2.IMWRITE_PNG_COMPRESSION,0])
