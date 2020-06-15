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

#include <badpixel.py>
import config

SCHWELLWERT_SUPER_HOT=      int((2**config.Farbtiefe)*0.95) #Obere Genze
SCHWELLWERT_HOT=            int((2**config.Farbtiefe)*0.85)
SCHWELLWERT_ALMOST_DEAD=    int((2**config.Farbtiefe)*0.01) 
SCHWELLWERT_DEAD=           int((2**config.Farbtiefe)*0.001) #untere Grenze

# Hot Pixel finder:
def HotPixelFinder(Bild):
    for z in config.Bildhoehe:
        for s in config.Bildbreite:
            if Bild[z,s]>=SCHWELLWERT_SUPER_HOT:
                BPM[z,s]=100
            elif Bild[z,s]>=SCHWELLWERT_HOT:
                BPM[z,s]=80

# Dead Pixel finder:
def DeadPixelFinder(Bild):
    for z in config.Bildhoehe:
        for s in config.Bildbreite:
            if Bild[z,s]<=SCHWELLWERT_DEAD:
                BPM[z,s]=100
            elif Bild[z,s]<=SCHWELLWERT_ALMOST_DEAD:
                BPM[z,s]=80




def test(n):
    print(n, SCHWELLWERT_DEAD)

