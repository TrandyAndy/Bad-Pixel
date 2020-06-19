import random as r
import config as cfg
import numpy as np

def verpixeln (D2_Bild, AnzPixel=100, lineEnable=False, minAbweichung=20):
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
    print("Bad-Pixel wurden erzeugt")
    return D2_Bild, BPM
            



