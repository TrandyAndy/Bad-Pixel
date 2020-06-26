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

def nachbar(Bild, BPM, Methode=0):  #Mittelwert der beiden Nachbarn
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


""" #NARC=0 NMFC=1 NSRC=2
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
    for z in range(l,hoehe-l):
        for s in range(l,breite-l):
            if BPM[z,s] !=0:
                #Gradienten legen
                vertikal=Bild[z-l:z+l,s]
                horizontal=Bild[z,s-l:s+l]
                sub=Bild[z-l:z+l,s-l:s+l]
                nordost=np.diagonal(sub)
                nordwest=np.fliplr(sub).diagonal()
                #low Gradient berechnen
                Gradient=[max(np.gradient(vertikal)),max(np.gradient(horizontal)),max(np.gradient(nordost)),max(np.gradient(nordwest)),2**16]
                for i in range(len(Gradient)-1):
                    if Gradient[i]<Gradient[i+1]:
                        Richtung=i
                #Grauwert berechen
                if Richtung==0:
                    Grau=np.mean(vertikal)
                elif Richtung==1:
                    Grau=np.mean(horizontal)
                elif Richtung==2:
                    Grau=np.mean(nordost)
                elif Richtung==3:
                    Grau=np.mean(nordwest)
                else:
                    print("Error")
            
                Bild[z,s]=Grau
    return Bild
                





#Nagao

#def Nagao():
