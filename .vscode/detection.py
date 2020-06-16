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

SCHWELLWERT_SUPER_HOT=      int((2**  cfg.Farbtiefe)*0.95)  #obere Genze
SCHWELLWERT_HOT=            int((2**  cfg.Farbtiefe)*0.85)
SCHWELLWERT_ALMOST_DEAD=    int((2**  cfg.Farbtiefe)*0.01) 
SCHWELLWERT_DEAD=           int((2**  cfg.Farbtiefe)*0.001) #untere Grenze
SCHWELLWERT_WINDOWS_DEAD = 0.3
SCHWELLWERT_WINDOWS_HOT = 10
# Hot Pixel finder:
def HotPixelFinder(Bild, Nr):
    Zaehler=0
    leer, hohe, breite=np.shape(Bild)
    BPM=np.zeros((hohe,breite))
    for z in range(cfg.Bildhoehe):
        for s in range(cfg.Bildbreite):
            if Bild[Nr,z,s]>=SCHWELLWERT_SUPER_HOT:
                BPM[z,s]=100
                Zaehler +=1
            elif Bild[Nr,z,s]>=SCHWELLWERT_HOT:
                BPM[z,s]=80
                Zaehler +=1
    print("Zeile Spalte " , z, s)
    print("Hot Pixel: " , Zaehler)
    return BPM, Zaehler

# Dead Pixel finder:
def DeadPixelFinder(Bild, Nr):
    Zaehler=0
    leer, hohe, breite=np.shape(Bild) 
    BPM=np.zeros((hohe,breite))
    for z in range(hohe):
        for s in range(breite):
            if Bild[Nr,z,s]<=SCHWELLWERT_DEAD:
                BPM[z,s]=100
                Zaehler +=1
            elif Bild[Nr,z,s]<=SCHWELLWERT_ALMOST_DEAD:
                BPM[z,s]=80
                Zaehler +=1
    print("Zeile Spalte " , z, s)
    print("Tote Pixel: " , Zaehler)
    return BPM, Zaehler

def MultiPicturePixelCompare(Bilder):
    Bilderanzahl, hohe, breite=np.shape(Bilder) 
    print(Bilderanzahl," Bilder prüfen...")

    BPM_Durchschnitt=np.zeros((hohe,breite))
    BPM_Alive=np.ones((hohe,breite))
    BPM_HOT_Durchschnitt=np.zeros((hohe,breite))
    BPM_HOT_Alive=np.ones((hohe,breite))
    for i in range(Bilderanzahl):  
        print("Bild Nr. ",i)
        BPM, Anz =DeadPixelFinder(Bilder, i) #Check for Black
        BPM_HOT, Anz_HOT =HotPixelFinder(Bilder, i) #Check HOT
        #Durchschnitt
        BPM_Durchschnitt +=BPM
        BPM_HOT_Durchschnitt +=BPM_HOT
        #Alive Check
        BPM_Alive= BPM_Alive*BPM
        BPM_HOT_Alive= BPM_HOT_Alive*BPM_HOT
    BPM_Durchschnitt =BPM_Durchschnitt/Bilderanzahl
    BPM_HOT_Durchschnitt =BPM_HOT_Durchschnitt/Bilderanzahl

    #Auswertung
    Zaehler=[0,0,0,0]
    for z in range(hohe):
        for s in range(breite):
            if BPM_Alive[z,s]>=100:
                Zaehler[0] +=1
            if BPM_Durchschnitt[z,s]>=50:
                Zaehler[1] +=1
            if BPM_HOT_Alive[z,s]>=100:
                Zaehler[2] +=1
            if BPM_HOT_Durchschnitt[z,s]>=50:
                Zaehler[3] +=1
    print("Es sind noch ",Zaehler[0],"Dead Pixel übrig, und ",Zaehler[2]," HOT. (Nach Alive Check)" )
    print("Es sind noch ",Zaehler[1],"Dead Pixel übrig, und ",Zaehler[3]," HOT. (im Durchschnitt)" )

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
            erg = pBild[z,s] / durchschnittswert
            
            if(erg < SCHWELLWERT_WINDOWS_DEAD):
                print("Moving-Windows: Dead-Pixel: ", erg)
                BPM[z,s] = erg 
            elif(erg > SCHWELLWERT_WINDOWS_HOT):
                print("Moving-Windows: Hot-Pixel: ", erg)
                BPM[z,s] = erg 
    return BPM

