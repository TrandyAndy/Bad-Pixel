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

def nachbar2(Bild, BPM, Methode=0):  #Mittelwert der beiden Nachbarn
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
        return -1
    hoehe, breite = np.shape(Bild)
    Q_halbe=3
    beautiful=Bild
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
                if (links=s-Q_halbe)<0: #geht das?
                #if links<0:        
                    links=0
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

def Gradient(Bild, BPM, Methode=0, Laenge=10):
    if(np.shape(Bild) != np.shape(BPM)):
        print("Digga schau das die Dimensionen passen!")
        return -1
    hoehe, breite = np.shape(Bild)
    Richtung=-1
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
                Bild[z-l,s-l]=Grau  #Oder mit dem Korregierten Teil weiterarbeiten.
    return Bild
                

def Methoden(Pixels, Methode)
    if Methode==NMFC:
        return np.mean(Pixels)
    else if Methode==NARC:
        return np.average(Pixels) #ohne den Bad??
    else if Methode==NSRC:
        flatPixels=(Pixels.reshape(-1))
        l=range(flatPixels)
        return flatPixels[l/2-1]
    else:
        return -1



#Nagao

#def Nagao():
