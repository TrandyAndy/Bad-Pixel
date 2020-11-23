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
import copy



# Direkte Nachbarn:

def nachbar(Bild, BPM):  #Mittelwert der beiden Nachbarn
    if(np.shape(Bild) != np.shape(BPM)):
        print("Dimensionen passen nicht!")
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

# Nachbar
def nachbar2(Bild, BPM, Methode=cfg.Methoden.NMFC, Fester=4):  # Fenster um BadPixel
    if(np.shape(Bild) != np.shape(BPM)):            #Bildgröße Prüfen
        print("Dimensionen passen nicht!")
        return -1
    hoehe, breite = np.shape(Bild)                  #Bildgröße Speichern
    Q_halbe=int(Fester/2)               
    beautiful=copy.copy(Bild)
    for z in range(hoehe):                          #Schleife durch alle Bildpunkte
        for s in range(breite):
            if BPM[z,s] !=0:                                
                oben=z-Q_halbe                      #Fester aufspannen.
                if oben<0:
                    oben=0
                unten=z+Q_halbe
                if unten>hoehe:
                    unten=hoehe
                links=s
                links-=Q_halbe if (s>Q_halbe) else 0
                rechts=s+Q_halbe
                if rechts>breite:
                    rechts=breite
                Fenster=Bild[oben:unten,links:rechts]   #Fenster herrauskopieren
                beautiful[z,s]=Methoden(Fenster,Methode)#An gewünschte Korrekturmethode übergeben.
    return beautiful

""" #NARC=0 NMFC=1 NSRC=2
SR=Simpel Replacement
MF=Median Filter
AR=Average Relacement

def neigborhood(Bild, BPM, Methode=0):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Dimensionen passen nicht!")
        return -1
    hoehe, breite = np.shape(Bild)
        
    return beautiful """

# Gradient

def Gradient(Bild, BPM, Methode=cfg.Methoden.NMFC, Laenge=10):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Dimensionen passen nicht!")
        return -1
    hoehe, breite = np.shape(Bild)
    Richtung=-1
    beautiful=copy.copy(Bild)
    l=int(Laenge/2)
    for z in range(hoehe):
        for s in range(breite):
            if BPM[z,s] !=0:
                #Gradienten legen
                vertikal=beautiful[bottom(z-l):top(z+l,hoehe),s]
                horizontal=beautiful[z,bottom(s-l):top(s+l,breite)]
                sub=beautiful[bottom(z-l):top(z+l+1,hoehe),bottom(s-l):top(s+l+1,breite)]
                if sub.size <(l*2+1)**2:
                    nordost=[-2**16,+2**16]
                    nordwest=nordost
                else:             
                    nordost=np.diagonal(sub) #Falsch benannt
                    nordwest=np.fliplr(sub).diagonal() #trifft nicht Pixel
                #low Gradient berechnen
                Gradient=[max(np.gradient(vertikal)),max(np.gradient(horizontal)),max(np.gradient(nordost)),max(np.gradient(nordwest))]
                Low=2**16
                for i in range(len(Gradient)):
                    if Low>Gradient[i]:
                        Low=Gradient[i]
                        Richtung=i
                #Grauwert berechnen
                if Richtung==0:
                    Grau=Methoden(vertikal,Methode)
                elif Richtung==1:
                    Grau=Methoden(horizontal,Methode)
                elif Richtung==2:
                    Grau=Methoden(nordost,Methode)
                elif Richtung==3:
                    Grau=Methoden(nordwest,Methode)
                else:
                    print("Error")
                beautiful[z,s]=Grau  #Oder mit dem Korregierten Teil weiterarbeiten.
    return beautiful
                

def Methoden(Pixels, Methode):
    if Methode==cfg.Methoden.NMFC.value:   #NMFC
        return np.median(Pixels)
    elif Methode==cfg.Methoden.NARC.value: #NARC
        return np.mean(Pixels) #ohne den Bad-Pixel ist es Schwer
    elif Methode==cfg.Methoden.NSRC.value: #NSRC
        flatPixels=(np.reshape(Pixels,-1))
        l=len(flatPixels)
        m=int(l/2-1) # Rand Probleme
        return flatPixels[m]
    else:
        return -1

def top(x,Max):
    if x>=Max:
        return Max
    else:
        return x

def bottom(x,Min=0):
    if x<Min:
        return Min
    else:
        return x

#Nagao

""" def Nagao(Bild, BPM):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Dimensionen passen nicht!")
        return -1
    hoehe, breite = np.shape(Bild)
    Q_Fenster=2
    NagaoSub_a=([1,1,1,1,1]
                [0,1,1,1,0]
                [0,0,0,0,0]
                [0,0,0,0,0]
                [0,0,0,0,0])
    NagaoSub_a2=np.rot(NagaoSub_a)
    NagaoSub_b=([0,0,0,0,0]
                [0,0,0,0,0]
                [0,0,0,1,1]
                [0,0,1,1,1]
                [0,0,1,1,1])
    NagaoSub_c=([0,0,0,0,0]
                [0,1,1,1,0]
                [0,1,0,1,0]
                [0,1,1,1,0]
                [0,0,0,0,0])
    
    großBild=Bild
    v_rand=np.ones([:(Q_Fenster*breite)]).reshape(Q_Fenster,breite)
    h_rand=np-ones([:(Q_Fenster*(heohe+Q_Fenster))]).reshape((heohe+Q_Fenster),Q_Fenster)
    np.vstack([großBild,v_rand])
    np.hstack([großBild,h_rand])
    beautiful=Bild
    for z in range(hoehe):
        for s in range(breite):
            if BPM[z,s] !=0:
                #Fenster aufspannen
                #...
                
                Fenster*a """

def Flatfield(Bild, Hell_Mittel_Bild, Dunkel_Mittel_Bild):
    #Rechenvorschrift. Dunkel/(Hell-Dunkel)
    #Wiki: New=(Input-Dark)/(Flat_Field-Dark) Dark=ohne X-Ray; Flat_Field=ohne Bauteil
    # Gain und Dunkelstrom
    if(np.shape(Bild) != np.shape(Hell_Mittel_Bild) or np.shape(Bild) != np.shape(Dunkel_Mittel_Bild)):
        print("Dimensionen passen nicht!")
        return -1
    hoehe, breite = np.shape(Bild)
    a= Bild-Dunkel_Mittel_Bild
    b= Hell_Mittel_Bild-Dunkel_Mittel_Bild
    # a=np.array([1,3,4,5,5,6,7,0,1,4,4,1])
    # b=np.array([1,2,3,4,5,6,7,0,0,8,9,0])
    b=np.where(b!=0,b,1)
    c=np.divide(a,b)
    c=(c.reshape(-1))
    Fehler=0
    for i in range(len(c)):
        if c[i]>1.2: # passiet nur im Fehlerfall 2 falsche bilder
            print(i, c[i]," Falsches Bild gewählt")
            cfg.errorCode=-4
            Fehler=Fehler+1
            c[i]=0.2
    m=np.amax(c)
    if m==0:
        print("Alle Bilder gleich! So kann man kein FCC machen.")
        m=1
        cfg.errorCode=-4
    c=np.divide(c,m)
    beautiful=c*2**16-1
    beautiful=np.uint16(beautiful.reshape(hoehe,breite))#int 16 geht das???
    return beautiful, Fehler

def Hybrid(Bild, BPM,Methode=1): #zusätzlich Einstellungen?
    beautiful=Gradient(Bild, BPM, Methode)
    beautiful=nachbar2(beautiful, BPM, Methode)
    return beautiful