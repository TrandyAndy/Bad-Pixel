import numpy as np                                                          # Für Arrays
import cv2  
from enum import Enum                                                                # Import OpenCV
from _thread import start_new_thread, allocate_lock #oder mit therading lib.


#Global         Muss man das in Python überhaupt machen?
Bildhoehe=512
Bildbreite=512
Bilderzahl=0
Farbtiefe=16 #in Bit
#BPM= array([Bildbreite][Bildhoehe]) #Bad Pixel Map
#ImageArr= np.array([[Bildbreite][Bildhoehe][Bilderzahl]])
BildCounter=0
#Tread Sachen
Global_BPM_Moving=0
Global_BPM_Multi=0
Global_BPM_Dynamik=0
Ladebalken=0 #Globaler Tread Ladebalken
LadebalkenMax=100 #auf Anz der Bilder * Detections setzen
lock=allocate_lock() #Mutex

"""

    B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])  # 3D Array
"""
#Methoden_Liste=['NARC', 'NMFC', 'NSRC'] #zur Korrektur
class Methoden(Enum): #zur Korrektur
    NARC = 2 #Mittelwert
    NMFC = 1 #Median
    NSRC = 3 #Replacement