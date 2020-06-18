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

SCHWELLWERT_SUPER_HOT=      int((2**  cfg.Farbtiefe)*0.99)  #obere Genze
SCHWELLWERT_HOT=            int((2**  cfg.Farbtiefe)*0.95)
SCHWELLWERT_ALMOST_DEAD=    int((2**  cfg.Farbtiefe)*0.05) 
SCHWELLWERT_DEAD=           int((2**  cfg.Farbtiefe)*0.01) #untere Grenze
# Hot Pixel finder:
def HotPixelFinder(Bild, Nr):
    Zaehler=0
    leer, hohe, breite=np.shape(Bild)
    BPM=np.zeros((hohe,breite))
    for z in range(hohe):
        for s in range(breite):
            if Bild[Nr,z,s]>=SCHWELLWERT_SUPER_HOT:
                BPM[z,s]=100
                Zaehler +=1
            elif Bild[Nr,z,s]>=SCHWELLWERT_HOT:
                BPM[z,s]=80
                Zaehler +=1
    print("Hot Pixel: " , Zaehler)
    if Zaehler>hohe*breite*0.1: #Break if >10% falsch
        Zaehler=-1
        print("Überbelichtet")
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
    print("Tote Pixel: " , Zaehler)
    if Zaehler>hohe*breite*0.05: #Break if >5% falsch
        Zaehler=-1
        print("zu viele Dead Pixel")
    return BPM, Zaehler

def MultiPicturePixelCompare(Bilder):
    Bilderanzahl, hohe, breite=np.shape(Bilder) 
    print(Bilderanzahl," Bilder prüfen...")
    Bilderanzahl_Dead=Bilderanzahl
    Bilderanzahl_HOT =Bilderanzahl
    BPM_Dead_Alive =np.ones((hohe,breite))
    BPM_HOT_Alive =np.ones((hohe,breite))
    BPM_Dead_Durchschnitt=np.zeros((hohe,breite))
    BPM_HOT_Durchschnitt=np.zeros((hohe,breite))
    for i in range(Bilderanzahl):  
        print("Bild Nr. ",i)

        BPM, Anz_Dead =DeadPixelFinder(Bilder, i) #Check for Black
        if(Anz_Dead>=0):
            BPM_Dead_Durchschnitt +=BPM #Durchschnitt
            BPM_Dead_Alive= BPM_Dead_Alive*BPM #Alive Check
        else:
            Bilderanzahl_Dead -=1
        
        BPM_HOT, Anz_HOT =HotPixelFinder(Bilder, i) #Check HOT
        if(Anz_HOT>=0):
            BPM_HOT_Durchschnitt +=BPM_HOT
            BPM_HOT_Alive= BPM_HOT_Alive*BPM_HOT
        else:
            Bilderanzahl_HOT -=1
    
    BPM_Dead_Alive =(BPM_Dead_Durchschnitt>0)*100
    BPM_HOT_Alive =(BPM_HOT_Durchschnitt>0)*100
    BPM_Dead_Durchschnitt =BPM_Dead_Durchschnitt/(Bilderanzahl_Dead)
    BPM_HOT_Durchschnitt =BPM_HOT_Durchschnitt/(Bilderanzahl_HOT)
    

    #Auswertung
    Zaehler=[0,0,0,0]
    BPM_Alive=BPM_Dead_Alive
    BPM_Durchschnitt =BPM_Dead_Durchschnitt
    for z in range(hohe):
        for s in range(breite):
            if BPM_Dead_Alive[z,s]>=100:
                Zaehler[0] +=1
            if BPM_Dead_Durchschnitt[z,s]>=50:
                Zaehler[1] +=1
            if BPM_HOT_Alive[z,s]>=100:
                Zaehler[2] +=1
                BPM_Alive[z,s]=BPM_HOT_Alive[z,s]
            if BPM_HOT_Durchschnitt[z,s]>=50:
                Zaehler[3] +=1
                BPM_Durchschnitt[z,s] =BPM_HOT_Durchschnitt[z,s]
    print("Es sind noch ",Zaehler[0],"Dead Pixel übrig, und ",Zaehler[2]," HOT. (Nach Alive Check)" )
    print("Es sind noch ",Zaehler[1],"Dead Pixel übrig, und ",Zaehler[3]," HOT. (im Durchschnitt)" )
    return BPM_Durchschnitt, BPM_Alive #Auswahl

def test(n):
    print(n, SCHWELLWERT_DEAD)


def movingWindow(pBild, schwellwertDead = 0.5, schwellwertHot = 1.5):
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
            
            if(erg <= schwellwertDead):
                #print("Moving-Windows: Dead-Pixel: ", erg, "Z: ", z, "S: ", s)
                BPM[z,s] = 100 
            elif(erg >= schwellwertHot):
                print("Moving-Windows: Hot-Pixel: ", erg, "Z: ", z, "S: ", s)
                BPM[z,s] = 100 
    return BPM

def top(x,Max):
    if x>=Max:
        return Max
    else:
        return x

def bottom(x):
    if x<0:
        return 0
    else:
        return x

def advancedMovingWindow(Bilder, Nr, Fensterbreite=6, Faktor=3): #Faktor literatur sagt 3
    Anz, hoehe, breite = np.shape(Bilder)
    BPM=np.zeros((hoehe,breite))
    quadrat=int(Fensterbreite/2) #+1
    Zaehler=0
    for y in range(hoehe):
        for x in range(breite):
            supBPM=Bilder[Nr,bottom(x-quadrat):top(x+quadrat,breite),bottom(y-quadrat):top(y+quadrat,hoehe)]
            a= np.shape(supBPM)[0]+1
            b= np.shape(supBPM)[1]+1
            Elemente=a+b
            #print("Elemente",Elemente," a=",a," b=",b)
            Std=np.sqrt(np.var(supBPM))
            debug= abs(np.mean(supBPM)-Bilder[Nr,x,y])
            if Std*Faktor< abs(np.mean(supBPM)-Bilder[Nr,x,y]):
                BPM[x,y]=100
                Zaehler +=1
                #print("Std: ",Std," Abweichung= ", abs(np.mean(supBPM)-Bilder[Nr,x,y]))
    print("advWindow erkennt ",Zaehler," Fehler. Festerbreite= ",Fensterbreite)
    return BPM ,Zaehler
