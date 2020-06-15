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


 # Hot Pixel finder:

 def HotPixelFinder(Bild):
     return Bild*4
    # for z in Bildhoehe
    #     for s in Bildbreite
    #         if Bild[z,s]>=SCHWELLWERT_SUPER_HOT
    #             BPM[z,s]=100
    #         else if Bild[z,s]>=SCHWELLWERT_HOT
    #             BPM[z,s]=80



# Fibonacci-Zahlen-Modul

def fib(n):    # schreibe Fibonacci-Folge bis n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()