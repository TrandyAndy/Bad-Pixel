""" 
/*
 * @Author: Andreas Bank
 * @Email: diegruppetg@gmail.com
 * @Date: 15.06.2020
 * @Last Modified by: Andy
 * @Last Modified time: 
 * @Description: Die Suchalgorithmen für bad Pixel
 */
 """

import config as cfg
import numpy as np
import math


# Direkte Nachbarn:

def nachbar(Bild, BPM):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
        return -1
    hoehe, breite = np.shape(Bild)
    flatImage=np.uint(Bild.reshape(-1))
    flatBPM=(BPM.reshape(-1))
    for i in range(hoehe*breite-1):
        if i%breite and flatBPM[i]:
            flatImage[i]=(flatImage[i-1]+flatImage[i+1])/2 #Mittelwert einsetzen
            #print(i)
        else:
            #print("Hi")
            pass  #Ränder machen wir net
    beautiful=np.uint(flatImage.reshape(hoehe, breite))
    return beautiful


#nagumo

#def nagumo():
