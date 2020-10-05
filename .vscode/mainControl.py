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
import config as cfg
import importPictures as imP
import cv2
import telemetry
import cProfile 
import verpixler
import Speichern
from _thread import start_new_thread, allocate_lock #oder mit therading lib.

""" Pfad der Bilddateien:______________________________________________________________________________________ """
importPath = ".vscode\Serie 4 original.png"
importPath_Flat = "FFC_Bilder\Bildserie2_160kV_70uA_mittelwert.png"
importPath_Hell = "FFC_Bilder\Bildserie1_160kV_70uA_mittelwert.png" #MW Bild
importPath_Dunkel = "FFC_Bilder\Bildserie1_160kV_0uA_mittelwert.png"
importPath = "MethodentestBearbeitet.png"


""" Import der Bilddateien:______________________________________________________________________________________ """
bildDaten = imP.importFunction(importPath)
bildDaten_Flat = imP.importFunction(importPath_Flat)
bildDaten_Hell = imP.importFunction(importPath_Hell)
bildDaten_Dunkel = imP.importFunction(importPath_Dunkel)
#bildDaten=np.concatenate((bildDaten,bildDaten_Hell,bildDaten_Dunkel,bildDaten_Flat))
bildDaten[0,0,0]=12 #Unfug
#global Global_Bild
cfg.Global_Bild=bildDaten[0]
""" Aufruf der Detection Funktion:______________________________________________________________________________________ """
if True:

    #Tread erstellen:
    start_new_thread(detection.advancedMovingWindow,(cfg.Global_Bild,))
    i_Zeit=0
    while cfg.Global_Bild[0,0]==12:
        i_Zeit=i_Zeit+1
        print("Wir warten schon: ",i_Zeit)
        if i_Zeit>5000:
            break
        
    #BAD1=detection.advancedMovingWindow(bildDaten[0],Faktor=2.0,Fensterbreite=10)[0] #F=4
    #BAD1_2=detection.advancedMovingWindow(bildDaten[0],Faktor=2.5,Fensterbreite=5)[0] 
    #BAD1_3=detection.advancedMovingWindow(bildDaten_Hell[0],Faktor=4,Fensterbreite=10)[0] 
    #BAD2=detection.MultiPicturePixelCompare(bildDaten,GrenzeHot=0.995,GrenzeDead=0.1)[0] 
    #BAD3=detection.dynamicCheck(bildDaten, Faktor=1.03)[0]
    BAD=cfg.Global_Bild#detection.Mapping(BAD1,BAD2,BAD3,BAD1_2,BAD1_3)*100
    #Anzeigen
    telemetry.markPixels(BAD,bildDaten[0],bgr=0,Algorithmus="advWindow",schwelle=1)
    #telemetry.markPixels(BAD1_2,bildDaten[0],bgr=0,Algorithmus="advWindow_2",schwelle=1)
    #telemetry.markPixels(BAD1_3,bildDaten[0],bgr=0,Algorithmus="advWindow_3",schwelle=1)
    #telemetry.markPixels(BAD2,bildDaten[0],bgr=1,Algorithmus="Schwelle",schwelle=1)
    #telemetry.markPixels(BAD3,bildDaten[0],bgr=2,Algorithmus="Dynamik",schwelle=1)
    #Speichern
    Speichern.BPM_Save(BAD,"Grad_Test")
else:
    BAD=Speichern.BPM_Read("Grad_Test") #Aus Speicher laden.

""" Aufruf der Correction Funktion:______________________________________________________________________________________ """
if True:
    Datasvae=bildDaten[0]+1
    # GOOD_NB2_NARC=np.uint16(correction.nachbar2(bildDaten[0],BAD,2))
    # GOOD_NB2_NMFC=np.uint16(correction.nachbar2(bildDaten[0],BAD,1))
    # GOOD_NB2_NSRC=np.uint16(correction.nachbar2(bildDaten[0],BAD,3))
    GOOD_NB=np.uint16(correction.nachbar(bildDaten[0],BAD))
    GOOD_Grad_NARC=np.uint16(correction.Gradient(bildDaten[0],BAD,2,12))
    GOOD_Grad_NMFC=np.uint16(correction.Gradient(bildDaten[0],BAD,1))
    GOOD_Grad_NSRC=np.uint16(correction.Gradient(bildDaten[0],BAD,3))
    GOOD_Hybrid=np.uint16(correction.Hybrid(bildDaten[0], BAD,1))
    #FGOOD_Hybrid=np.uint16(correction.Hybrid(bildDaten_Flat[0], BAD,1))
    #HGOOD_Hybrid=np.uint16(correction.Hybrid(bildDaten_Hell[0], BAD,1))
    #DGOOD_Hybrid=np.uint16(correction.Hybrid(bildDaten_Dunkel[0], BAD,1))
    #GOOD_Flatfield=np.uint16(correction.Flatfield(FGOOD_Hybrid,HGOOD_Hybrid,DGOOD_Hybrid)[0])

""" Audgabe der Bilder Plots und Ergebnisse:______________________________________________________________________________________ """
telemetry.markPixels(BAD,bildDaten[0],bgr=0,Algorithmus="Hybrid",schwelle=1)
# cv2.imwrite("_korriegiert GOOD_NB2_NARC.png", GOOD_NB2_NARC, [cv2.IMWRITE_PNG_COMPRESSION,0])
# cv2.imwrite("_korriegiert GOOD_NB2_NMFC.png", GOOD_NB2_NMFC, [cv2.IMWRITE_PNG_COMPRESSION,0])
# cv2.imwrite("_korriegiert GOOD_NB2_NSRC.png", GOOD_NB2_NSRC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_NB.png", GOOD_NB, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_Grad_NARC.png", GOOD_Grad_NARC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_Grad_NMFC.png", GOOD_Grad_NMFC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_Grad_NSRC.png", GOOD_Grad_NSRC, [cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite("_korriegiert GOOD_Hybrid.png", GOOD_Hybrid, [cv2.IMWRITE_PNG_COMPRESSION,0])
#cv2.imwrite("_korriegiert Flatfield.png", GOOD_Flatfield, [cv2.IMWRITE_PNG_COMPRESSION,0])
