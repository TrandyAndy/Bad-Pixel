 
"""
/*
 * @Author: Julian Schweizerhof Andreas Bank
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-07_27
 * @Last Modified by: 
 * @Last Modified time: 2020-06-21 01:32:30
 * @Description: main
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
importPath = "PictureWithNoMarkings.png"

""" Import der Bilddateien:______________________________________________________________________________________ """
bildDaten = imP.importFunction(importPath)

""" Aufruf der Detection Funktion:______________________________________________________________________________________ """
if True:
    BAD=detection.advancedMovingWindow(bildDaten[1],Faktor=4)[0]

""" Aufruf der Correction Funktion:______________________________________________________________________________________ """
if True:
    GOOD=np.uint16(correction.nachbar(bildDaten[0],BAD))

""" Audgabe der Bilder Plots und Ergebnisse:______________________________________________________________________________________ """
telemetry.markPixels(BAD,bildDaten[0])