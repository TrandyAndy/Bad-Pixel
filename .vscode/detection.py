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

