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

SCHWELLWERT_SUPER_HOT=      int((2**  cfg.Farbtiefe)*0.95)  #obere Genze
SCHWELLWERT_HOT=            int((2**  cfg.Farbtiefe)*0.85)
SCHWELLWERT_ALMOST_DEAD=    int((2**  cfg.Farbtiefe)*0.01) 
SCHWELLWERT_DEAD=           int((2**  cfg.Farbtiefe)*0.001) #untere Grenze

# Hot Pixel finder:
def HotPixelFinder(Bild):
    Zaehler=0
    hohe, breite=np.shape(Bild)
    BPM=np.zeros((hohe,breite))
    for z in range(cfg.Bildhoehe):
        for s in range(cfg.Bildbreite):
            if Bild[z,s]>=SCHWELLWERT_SUPER_HOT:
                BPM[z,s]=100
                Zaehler +=1
            elif Bild[z,s]>=SCHWELLWERT_HOT:
                BPM[z,s]=80
                Zaehler +=1
    print("Zeile Spalte " , z, s)
    print("Hot Pixel: " , Zaehler)
    return BPM

# Dead Pixel finder:
def DeadPixelFinder(Bild):
    Zaehler=0
    hohe, breite=np.shape(Bild)
    BPM=np.zeros((hohe,breite))
    for z in range(cfg.Bildhoehe):
        for s in range(cfg.Bildbreite):
            if Bild[z,s]<=SCHWELLWERT_DEAD:
                BPM[z,s]=100
                Zaehler +=1
            elif Bild[z,s]<=SCHWELLWERT_ALMOST_DEAD:
                BPM[z,s]=80
                Zaehler +=1
    print("Zeile Spalte " , z, s)
    print("Tote Pixel: " , Zaehler)
    return BPM

def MultiPicturePixelCompare(Bilder, Bilderanzahl):
    x=np.shape(Bilder)
    print(x)
    for i in (0, x):  #Check for Black
        DeadPixelFinder(Bilder[i])




def test(n):
    print(n, SCHWELLWERT_DEAD)

