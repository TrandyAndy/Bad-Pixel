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

import   config as cfg

SCHWELLWERT_SUPER_HOT=      int((2**  cfg.Farbtiefe)*0.95)  #obere Genze
SCHWELLWERT_HOT=            int((2**  cfg.Farbtiefe)*0.85)
SCHWELLWERT_ALMOST_DEAD=    int((2**  cfg.Farbtiefe)*0.01) 
SCHWELLWERT_DEAD=           int((2**  cfg.Farbtiefe)*0.001) #untere Grenze

# Hot Pixel finder:
def HotPixelFinder(Bild):
    for z in   cfg.Bildhoehe:
        for s in   cfg.Bildbreite:
            if Bild[z,s]>=SCHWELLWERT_SUPER_HOT:
                BPM[z,s]=100
            elif Bild[z,s]>=SCHWELLWERT_HOT:
                BPM[z,s]=80
    #return BMP[]

# Dead Pixel finder:
def DeadPixelFinder(Bild):
    Zaehler=0
    for z in (0,512-1):
        for s in (0,  cfg.Bildbreite-1):
            if Bild[z,s]<=SCHWELLWERT_DEAD:
                (BPM[z,s])=100
                Zaehler +=1
            elif Bild[z,s]<=SCHWELLWERT_ALMOST_DEAD:
                BPM[z,s]=80
                Zaehler +=1
    print("Tote Pixel: " , Zaehler)
    #return BMP

def MultiPicturePixelCompare(Bilder, Bilderanzahl):
    x=np.shape(Bilder)
    print(x)
    for i in (0, x):  #Check for Black
        DeadPixelFinder(Bilder[i])




def test(n):
    print(n, SCHWELLWERT_DEAD)
