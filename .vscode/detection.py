""" 
/*
 * @Author: Andreas Bank
 * @Email: diegruppetg@gmail.com
 * @Date: 15.06.2020
 * @Last Modified by: Andy
 * @Last Modified time: 19.09.20
 * @Description: Die Suchalgorithmen für bad Pixel
 * @Version V2: Digital BPM, Schneller
 */
 """

import config as cfg
import numpy as np
import math

global Lichtschutz
Lichtschutz = 0.05 #10%

# Hot Pixel finder:
def HotPixelFinder(D2_Bild, Schwelle=0.99):
    Zaehler=0
    hohe, breite=np.shape(D2_Bild)
    BPM=np.zeros((hohe,breite))
    for z in range(hohe):
        for s in range(breite):
            if D2_Bild[z,s]>=Schwelle:
                BPM[z,s]=1 #Digital
                Zaehler +=1
    print("Hot Pixel: " , Zaehler)
    if Zaehler>hohe*breite*Lichtschutz: #Überbelichtungsschutz Break if >10% falsch
        Zaehler=-1
        print("Überbelichtet")
    return BPM, Zaehler

# Dead Pixel finder:
def DeadPixelFinder(D2_Bild, Schwelle=0.01):
    Zaehler=0
    hohe, breite=np.shape(D2_Bild) 
    BPM=np.zeros((hohe,breite))
    for z in range(hohe):
        for s in range(breite):
            if D2_Bild[z,s]<=Schwelle:
                BPM[z,s]=1 #Digital
                Zaehler +=1
    print("Tote Pixel: " , Zaehler)
    if Zaehler>hohe*breite*Lichtschutz: #Break if >5% falsch
        Zaehler=-1
        print("zu viele Dead Pixel")
    return BPM, Zaehler

def MultiPicturePixelCompare(D3_Bilder,GrenzeHot=0.99,GrenzeDead=0.01):
    Bilderanzahl, hohe, breite=np.shape(D3_Bilder) 
    print(Bilderanzahl," Bilder prüfen...")
    BPM_D=np.zeros((Bilderanzahl,hohe,breite))
    BPM_H=np.zeros((Bilderanzahl,hohe,breite))
    Ungueltig=np.zeros((hohe,breite))
    UberLicht=0
    UnterLicht=0
    for i in range(Bilderanzahl):  
        print("Bild Nr. ",i)
        
        BPM_Dead, Anz_Dead =DeadPixelFinder(D3_Bilder[i],GrenzeDead) #Check for Black
        if(Anz_Dead<0):
            BPM_Dead=Ungueltig
            UnterLicht=UnterLicht+1
        BPM_D=BPM_D+BPM_Dead
        BPM_HOT, Anz_HOT =HotPixelFinder(D3_Bilder[i],GrenzeHot) #Check HOT
        if(Anz_Hot<0):
            BPM_Hot=Ungueltig
            UberLicht=UberLicht+1
        BPM_H=BPM_H+BPM_Hot
        #BPM[i]=BPM_Dead or BPM_HOT
        
    #Auswertung
    print(UberLicht," Bilder Überbelichtet, ",UnterLicht," Bilder zu Dunkel")
    BPM_D=(BPM_D-int(0.3*(Bilderanzahl-UnterLicht)))>0 #Digit + mehr als 30%
    BPM_H=(BPM_H-int(0.3*(Bilderanzahl-UberLicht)))>0
    BPM=BPM_D or BPM_H
    Fehler=len(np.nonzero(BPM))
    print("Multi Picture findet ",Fehler)
    return BPM, Fehler
    

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

def advancedMovingWindow(D2_Bild, Fensterbreite=6, Faktor=3): #Faktor literatur sagt 3  (BildSerie2 70µA ist Faktor 2,5-3,5)
    hoehe, breite = np.shape(D2_Bild)
    #print(hoehe,breite)
    BPM=np.zeros((hoehe,breite))
    quadrat=int(Fensterbreite/2) #+1
    Zaehler=0
    for y in range(breite):
        for x in range(hoehe):
            supBPM=D2_Bild[bottom(x-quadrat):top(x+quadrat,breite),bottom(y-quadrat):top(y+quadrat,hoehe)]
            #a= np.shape(supBPM)[0]+1
            #b= np.shape(supBPM)[1]+1
            #Elemente=a+b
            #print("Elemente",Elemente," a=",a," b=",b)
            Std=np.sqrt(np.var(supBPM))
            #debug= abs(np.mean(supBPM)-D2_Bild[x,y])
            if Std*Faktor< abs(np.mean(supBPM)-D2_Bild[x,y]):
                BPM[x,y]=1 #Digital
                Zaehler +=1
                #print("Std: ",Std," Abweichung= ", abs(np.mean(supBPM)-Bilder[Nr,x,y]))
    print("advWindow erkennt ",Zaehler," Fehler. Festerbreite= ",Fensterbreite)
    return BPM ,Zaehler

def dynamicCheck(D3_Bilder, Faktor=1.5): #Bilder müssen verschiene sein (Helle und Dunkle!) , Faktor ist Schwellwert für Erkennung. 1.03-1.2
    Anz, hoehe, breite = np.shape(D3_Bilder)
    BPM=np.zeros((hoehe,breite))
    Zaehler=0
    #Hell Dunken erstellen
    Hellste=np.ones((hoehe,breite))
    Dunkelste=np.ones((hoehe,breite))*2**cfg.Farbtiefe
    for Nr in range(Anz):
        for s in range(hoehe):
            for z in range(breite):
                if Hellste[s,z]<D3_Bilder[Nr,s,z]:
                    Hellste[s,z]=D3_Bilder[Nr,s,z]
                if Dunkelste[s,z]>D3_Bilder[Nr,s,z]:
                    Dunkelste[s,z]=D3_Bilder[Nr,s,z]
    #Mittlere Dynamik
    Dynamik=(Hellste-Dunkelste)/Hellste
    DynamikNorm=np.mean(Dynamik)
    print("Dynamik Norm = ", DynamikNorm)
    for s in range(hoehe):
        for z in range(breite):
            if Dynamik[s,z]<DynamikNorm/Faktor:
                BPM[s,z]=int((DynamikNorm-Dynamik[s,z])/DynamikNorm*100)
                BPM[s,z]=1 #Digital 
                Zaehler+=1
    print(Zaehler," Fehler gefunden (DynamikCheck).")
    return BPM, Zaehler

