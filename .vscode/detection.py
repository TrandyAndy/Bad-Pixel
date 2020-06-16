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
SCHWELLWERT_WINDOWS_DEAD = 0.6
SCHWELLWERT_WINDOWS_HOT = 1.6
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





def movingWindow(pBild):
    hoehe, breite = np.shape(pBild)
    BPM=np.zeros((hoehe,breite))
    for z in range(hoehe):
        for s in range(breite):
            #print("z : ", z, "s: ",s)
            durchschnittswert = 0.0
            if(z == 0 and s == 0):               # Wenn Ecke links oben
                durchschnittswert += pBild[z, s+1]
                durchschnittswert += pBild[z+1, s]
                durchschnittswert += pBild[z+1, s+1]
                durchschnittswert = durchschnittswert / 3
            elif(z == 0 and s == breite-1):        # Wenn Ecke rechts oben
                durchschnittswert += pBild[z, s-1]
                durchschnittswert += pBild[z+1, s-1]
                durchschnittswert += pBild[z+1, s]
                durchschnittswert = durchschnittswert / 3
            elif(z == hoehe-1 and s == 0):         # Wenn Ecke links unten
                durchschnittswert += pBild[z-1, s]
                durchschnittswert += pBild[z-1, s+1]
                durchschnittswert += pBild[z, s+1]
                durchschnittswert = durchschnittswert / 3
            elif(z == hoehe-1 and s == breite-1):    # Wenn Ecke rechts unten
                durchschnittswert += pBild[z-1, s-1]
                durchschnittswert += pBild[z-1, s]
                durchschnittswert += pBild[z, s-1]
                durchschnittswert = durchschnittswert / 3
            elif(z == 0):                       # Wenn am oberen Ende
                durchschnittswert += pBild[z, s-1]
                durchschnittswert += pBild[z, s+1]
                durchschnittswert += pBild[z+1, s-1]
                durchschnittswert += pBild[z+1, s]
                durchschnittswert += pBild[z+1, s+1]
                durchschnittswert = durchschnittswert / 5
            elif(s == 0):                       # Wenn am linken Ende   
                durchschnittswert += pBild[z-1, s]
                durchschnittswert += pBild[z-1, s+1]
                durchschnittswert += pBild[z, s+1]
                durchschnittswert += pBild[z+1, s]
                durchschnittswert += pBild[z+1, s+1]
                durchschnittswert = durchschnittswert / 5
            elif(s == breite-1):                  # Wenn am rechten Ende
                durchschnittswert += pBild[z-1, s-1]
                durchschnittswert += pBild[z-1, s]
                durchschnittswert += pBild[z, s-1]
                durchschnittswert += pBild[z+1, s-1]
                durchschnittswert += pBild[z+1, s]
                durchschnittswert = durchschnittswert / 5
            elif(z == hoehe-1):                   # Wenn am unteren Ende 
                durchschnittswert += pBild[z-1, s-1]
                durchschnittswert += pBild[z-1, s]
                durchschnittswert += pBild[z-1, s+1]
                durchschnittswert += pBild[z, s-1]
                durchschnittswert += pBild[z, s+1]
                durchschnittswert = durchschnittswert / 5
            else:                               # Ansonsten
                durchschnittswert += pBild[z-1, s-1]
                durchschnittswert += pBild[z-1, s]
                durchschnittswert += pBild[z-1, s+1]
                durchschnittswert += pBild[z, s-1]
                durchschnittswert += pBild[z, s+1]
                durchschnittswert += pBild[z+1, s-1]
                durchschnittswert += pBild[z+1, s]
                durchschnittswert += pBild[z+1, s+1]
                durchschnittswert = durchschnittswert / 8
            
            BPM[z,s] = pBild[z,s] / durchschnittswert
            if(BPM[z,s] < SCHWELLWERT_WINDOWS_DEAD):
                print("Der aktuelle Wert ist: ", BPM[z,s])
            else if(BPM[z,s] > SCHWELLWERT_WINDOWS_HOT)
    return BPM

