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

# Nachbar
def nachbar2(Bild, BPM, Methode=1, Fester=6):  # Fenster um BadPixel
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
        return -1
    hoehe, breite = np.shape(Bild)
    Q_halbe=int(Fester/2)
    beautiful=copy.copy(Bild)
    for z in range(hoehe):
        for s in range(breite):
            if BPM[z,s] !=0:
                #Fester aufspannen.
                oben=z-Q_halbe
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
                Fenster=Bild[oben:unten,links:rechts]
                beautiful[z,s]=Methoden(Fenster,Methode)
    return beautiful

""" #NARC=0 NMFC=1 NSRC=2
SR=Simpel Replacement
MF=Median Filter
AR=Average Relacement

def neigborhood(Bild, BPM, Methode=0):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
        return -1
    hoehe, breite = np.shape(Bild)
        
    return beautiful """

# Gradient

def Gradient(Bild, BPM, Methode=1, Laenge=10):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
        return -1
    hoehe, breite = np.shape(Bild)
    Richtung=-1
    beautiful=copy.copy(Bild)
    l=int(Laenge/2)
    großBild=np.zeros((hoehe+Laenge,breite+Laenge))
    großBild[l:hoehe+l,l:breite+l]=Bild
    großBPM=np.zeros((hoehe+Laenge,breite+Laenge))
    großBPM[l:hoehe+l,l:breite+l]=BPM
    for z in range(l,hoehe):
        for s in range(l,breite):
            if BPM[z-l,s-l] !=0:
                #Gradienten legen
                vertikal=großBild[z-l:z+l,s]
                horizontal=großBild[z,s-l:s+l]
                sub=großBild[z-l:z+l,s-l:s+l]
                nordost=np.diagonal(sub)
                nordwest=np.fliplr(sub).diagonal()
                #low Gradient berechnen
                Gradient=[max(np.gradient(vertikal)),max(np.gradient(horizontal)),max(np.gradient(nordost)),max(np.gradient(nordwest))]
                Low=2**16
                for i in range(len(Gradient)):
                    if Low>Gradient[i]:
                        Low=Gradient[i]
                        Richtung=i
                #Grauwert berechen
                if Richtung==0:
                    Grau=Methoden(vertikal,Methode)
                elif Richtung==1:
                    Grau=np.mean(horizontal)
                elif Richtung==2:
                    Grau=np.mean(nordost)
                elif Richtung==3:
                    Grau=np.mean(nordwest)
                else:
                    print("Error")
                beautiful[z-l,s-l]=Grau  #Oder mit dem Korregierten Teil weiterarbeiten.
    return beautiful
                

def Methoden(Pixels, Methode):
    if Methode==1: #Methoden.NMFC:
        return np.median(Pixels)
    elif Methode==2: #NARC
        return np.mean(Pixels) #ohne den Bad??
    elif Methode==3: #NSRC
        flatPixels=(np.reshape(Pixels,-1))
        l=len(flatPixels)
        m=int(l/2-1)
        return flatPixels[m]
    else:
        return -1



#Nagao

""" def Nagao(Bild, BPM):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
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
        print("Digga schau das die Dimensionen passen!")
        return -1
    a= Bild-Dunkel_Mittel_Bild
    b= Hell_Mittel_Bild-Dunkel_Mittel_Bild
    # a=np.array([1,3,4,5,5,6,7,0,1,4,4,1])
    # b=np.array([1,2,3,4,5,6,7,0,0,8,9,0])
    Zero=np.where(b==0)
    print(Zero)
    for z in Zero:
        b[z]=1 #zu groß
    c=np.divide(a,b)
    c=(c.reshape(-1))
    for i in range(len(c)):
        if c[i]>1.2:
            print(i, c[i])
            c[i]=1
    m=np.amax(c)
    c=np.divide(c,m)
    x=c*2**16-1
    x=np.uint(x.reshape(512,512))
    return x
