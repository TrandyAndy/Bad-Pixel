import numpy as np                                                          # Für Arrays
import cv2                                                                  # Import OpenCV



#Global         Muss man das in Python überhaupt machen?
Bildhoehe=512
Bildbreite=512
Bilderzahl=0
Farbtiefe=16 #in Bit
#BPM= array([Bildbreite][Bildhoehe]) #Bad Pixel Map
#ImageArr= array([Bildbreite][Bildhoehe][Bilderzahl])
BildCounter=0

"""

    B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])  # 3D Array
"""
