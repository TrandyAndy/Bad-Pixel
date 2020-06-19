import random as r
import config as cfg
import numpy as np

def verpixeln (D2_Bild, AnzPixel=100, lineEnable=False,Cluster=False, minAbweichung=20):
    hoehe, breite = np.shape(D2_Bild)
    r.seed(D2_Bild[1,1]+AnzPixel)
    BPM=np.zeros((hoehe,breite))
    for i in range(AnzPixel):
        x=r.randint(0,breite-1)
        y=r.randint(0,hoehe-1)
        grey=r.randint(0,2**cfg.Farbtiefe)
        if(abs(D2_Bild[x,y]-grey)>2**cfg.Farbtiefe*minAbweichung/100):
            D2_Bild[x,y]=grey
            BPM[x,y]=100
        else:
            i -=1

    if(lineEnable):
        print("Es werden Linienfehler erzeugt")
        for v in range(lineEnable):
            length=r.randint(10,int(breite/3))
            dir=r.choice(['X','Y'])
            x=r.randint(0,breite-1)
            y=r.randint(0,hoehe-1)
            if(dir=='X'):
                x=r.randint(0,breite-length)
            else:
                y=r.randint(0,breite-length)

            grey=r.randint(0,2**cfg.Farbtiefe)
            if(abs(D2_Bild[x,y]-grey)>2**cfg.Farbtiefe*minAbweichung/100):
                if(dir=='X'):
                    D2_Bild[x:x+length,y]=grey
                    BPM[x:x+length,y]=100
                else:
                    D2_Bild[x,y:y+length]=grey
                    BPM[x,y:y+length]=100
            else:
                v -=1
    if Cluster:
        a,b,c=cluster(D2_Bild,Anz=Cluster)
        BPM=BPM+b
        D2_Bild=a
    print("Bad-Pixel wurden erzeugt")
    return D2_Bild, BPM
            

def cluster (D2_Bild, Durchmesser=8, Anz=1, Dichte=1/3):
    print("Cluster wird erzeugt Anzahl ist verfälscht")
    hoehe, breite = np.shape(D2_Bild)
    r.seed(D2_Bild[1,1]+Anz+Durchmesser)
    BPM=np.zeros((hoehe,breite))
    Zaehler=0
    for i in range(Anz):
        x=r.randint(int(Durchmesser/2),breite-int(Durchmesser/2)-1)
        y=r.randint(int(Durchmesser/2),hoehe-int(Durchmesser/2)-1)
        grey=r.randint(D2_Bild[x,y],2**cfg.Farbtiefe)
        grey=r.randint(grey,2**cfg.Farbtiefe)
        grey=r.randint(grey,2**cfg.Farbtiefe)
        for v in range(int((Durchmesser**2) *Dichte)):
            x2=int(r.gauss(0,Durchmesser/3))
            y2=int(r.gauss(0,Durchmesser/3))
            D2_Bild[x+x2,y+y2]=grey
            BPM[x+x2,y+y2]=100
            Zaehler+=1
        
    return D2_Bild, BPM, Zaehler

