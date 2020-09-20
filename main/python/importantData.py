# Gute Webseiten:
# Einführung in OpenCV: https://www.geeksforgeeks.org/opencv-python-tutorial/#images
# Einfügen von RAW-Dateien: https://stackoverflow.com/questions/18682830/opencv-python-display-raw-image
# Offizielle Doku zu imwrite(): https://docs.opencv.org/4.3.0/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
# Hauptfunktionen in Python: https://docs.python.org/3/library/functions.html#round
# Eine Datei binär lesen: https://stackoverflow.com/questions/8710456/reading-a-binary-file-with-python
# Image-Container in OpenCV: https://docs.opencv.org/2.4/doc/tutorials/core/mat_the_basic_image_container/mat_the_basic_image_container.html
# Einführung in Numpy: https://www.python-kurs.eu/numpy.php
# Terminal Befehl od (Linux oder MacOS): https://www.geeksforgeeks.org/od-command-linux-example/
# Element aus Numpy Array holen: https://numpy.org/doc/1.18/reference/generated/numpy.take.html
# Pfadnamen auswerten: https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format/8384786
# Pfadnamen auswerten 2: https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python



"""
    # Funktionen aus numpy:
    F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
    C = np.array(cvalues) # Array erzeugen
    x = np.arange(0.5, 6.1, 0.8, int)   # start, stop, step, typ    
    samples, spacing = np.linspace(1, 10, 5, endpoint=False, retstep=True)   # start, stop, anzahlWerte, Endpunkt, Abstand zwischen zwei Werten auch zurückliefern?
    np.ndim(C)  # dimension des Arrays
    A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])   # 2D Array mit 3 Spalten und 3 Zeilen
    B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])  # 3D Array
    print(np.shape(x))  # Zeilen, Spalten, ... Anzahl des Arrays ausgeben
    x.shape = (9,2)     # Zeilten, Spalten Verteilung ändern
"""




# def hisImportFunctionOld(pImportPath):
#     pathWithoutExtension = os.path.splitext(pImportPath) [0]
#     print("\n\n*************************************************************")
#     print("Funktion zum Einlesen von HIS-Dateien aufgerufen")
#     print("*************************************************************\n")
#     fileName, fileExtension = os.path.splitext(os.path.basename(importPath))
#     print("Die Datei", fileName, "wird jetzt eingelesen.")
#     fd = open(pImportPath,'rb')
#     data = np.fromfile(fd,dtype=np.uint16, count=50)                        # Den Header 50 mal mit unsinged int 16 Bit einlesen (erste 100 Bytes)
#     rows = int(np.take(data, 8))                                            # Reihen bestimmen, in int konvertieren, ansonsten overflow Error bei der Funktion fromfile()
#     cols = int(np.take(data, 9))                                            # Spalten bestimmen
#     print("Ihre Datei hat", rows, "Reihen und", cols, "Spalten und besteht aus")
#     f = np.fromfile(fd, dtype=np.uint16, count=rows*cols)                   # Pixel lesen und in einem ein dimensionales Array speichern
#     im = f.reshape((rows, cols))                                            # Array in zwei dimensionales Array mit rows x cols erstellen
#     fd.close()                                                              # File schließen
#     cv2.imshow('image', im)                                                 # Array als Bild anzeigen
#     #cv2.imwrite(fileName+'.png',im, [cv2.IMWRITE_PNG_COMPRESSION,0])       # Array als PNG speichern ohne Kompression
#     cv2.imwrite(pathWithoutExtension+'_beta.png',im, [cv2.IMWRITE_PNG_COMPRESSION,0])     # Array als PNG speichern ohne Kompression
#     print("Ihre Datei wurden unter", pathWithoutExtension+".png gespeichert")
#     cv2.waitKey()                                                           # Warten bis eine Taste gedrückt wird
#     cv2.destroyAllWindows()                                                 # Alle Fenster schließen


#print("Dateiname: ", fileName)
#print("Endung: ", fileExtension)



#fd = open('/Users/julian/Desktop/Bildserie1_160kV_0uA.his','rb')

#data = np.fromfile(fd,dtype=np.uint16, count=50)                        # Den Header 50 mal mit unsinged int 16 Bit einlesen (erste 100 Bytes)
# print(data)
# rows = int(np.take(data, 8))                                            # Reihen bestimmen, in int konvertieren, ansonsten overflow Error bei der Funktion fromfile()
# cols = int(np.take(data, 9))                                            # Spalten bestimmen
#print("Es sind", rows, "Reihen und", cols, "Spalten")

#f = np.fromfile(fd, dtype=np.uint16, count=rows*cols)                   # Pixel lesen und in einem ein dimensionales Array speichern
#print(f)
# im = f.reshape((rows, cols))                                            # Array in zwei dimensionales Array mit rows x cols erstellen
#print(im)   
# cv2.imshow('image', im)                                                 # Array als Bild anzeigen
# cv2.imwrite(fileName+'.png',im, [cv2.IMWRITE_PNG_COMPRESSION,0])  # Array als PNG speichern ohne Kompression
# cv2.waitKey()                                                           # Warten bis eine Taste gedrückt wird
# cv2.destroyAllWindows()                                                 # Alle Fenster schließen
 


# #f = open('/Users/julian/Desktop/Bildserie1_160kV_0uA.his','rb')  

# # You can give path to the 
# # image as first argument 
# img = cv2.imread('lena.png',0) 
#  # /Users/julian/Desktop/hello/.vscode/lena.png
# # will show the image in a window
# cv2.imshow('image', img) 
# k = cv2.waitKey(0) & 0xFF
  
# # wait for ESC key to exit 
# if k == 27:  
#     cv2.destroyAllWindows() 
      
# # wait for 's' key to save and exit 
# elif k == ord('s'):  
#     cv2.imwrite('messigray.png',img) 
#     cv2.destroyAllWindows()