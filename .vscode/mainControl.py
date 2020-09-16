"""
/*
 * @Author: Julian Schweizerhof und Andreas Bank
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
import Speichern

""" Pfad der Bilddateien:______________________________________________________________________________________ """
importPath = ".vscode\Serie 4 original.png"
importPath = "MethodentestBearbeitet.png"


""" Import der Bilddateien:______________________________________________________________________________________ """
bildDaten = imP.importFunction(importPath)


""" Aufruf der Detection Funktion:______________________________________________________________________________________ """
if True:
    BAD=detection.advancedMovingWindow(bildDaten[0],Faktor=2.5,Fensterbreite=5)[0] #F=4
    #Speichern
#     Speichern.BPM_Save(r"C:\Users\u2887166\Documents\GitHub\Bad-Pixel\BPM_Speicher",BAD,"X-Ray1")
# else:
#     BAD=BPM_Read(0,"Peter") #Aus Speicher laden.

""" Aufruf der Correction Funktion:______________________________________________________________________________________ """
if True:
    GOOD_NB2_NARC=np.uint16(correction.nachbar2(bildDaten[0],BAD,1))
    GOOD_NB2_NMFC=np.uint16(correction.nachbar2(bildDaten[0],BAD,2))
    GOOD_NB2_NSRC=np.uint16(correction.nachbar2(bildDaten[0],BAD,3))
    GOOD_NB_NARC=np.uint16(correction.nachbar(bildDaten[0],BAD))
    GOOD_Grad_NARC=np.uint16(correction.Gradient(bildDaten[0],BAD,1))

""" Audgabe der Bilder Plots und Ergebnisse:______________________________________________________________________________________ """
telemetry.markPixels(BAD,bildDaten[0])
cv2.imwrite("_korriegiert GOOD_NB2_NARC.png", GOOD_NB2_NARC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_NB2_NMFC.png", GOOD_NB2_NMFC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_NB2_NSRC.png", GOOD_NB2_NSRC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_NB_NARC.png", GOOD_NB_NARC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_Grad_NARC.png", GOOD_Grad_NARC, [cv2.IMWRITE_PNG_COMPRESSION,0])