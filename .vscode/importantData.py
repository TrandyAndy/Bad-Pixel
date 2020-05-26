


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