import os
import cv2
import importPictures as imP
from pathlib import Path
import PyQt5.QtCore as core

def BPM_Save(BPM, Sensor_Name):
    #Rücklesen wie viele BPMs es gibt Aus Dateiname
    x=(os.listdir(dir_path))
    print(len(x)," Dateien im Ordner")
    #Davon Sensor
    Nr=0
    for i in range(len(x)):
        DatName=str(x[i])
        if DatName.find(Sensor_Name) !=-1:
            Start=DatName.find("V",len(Sensor_Name))
            Ende=DatName.find(".",len(Sensor_Name))
            sZahl=DatName[Start+1:Ende]
            #print(sZahl)
            Zahl=int(sZahl)
            if(Zahl>Nr):
                Nr=Zahl
                y=x[i]
    if len(x)>200:
        Print("Speicher voll")
        return -1
    else:     
        #Schreiben
        Nr=Nr+1
        Datei_path=os.sep.join([dir_path,Sensor_Name+"_V"+str(Nr)+".png"])
        cv2.imwrite(Datei_path, BPM, [cv2.IMWRITE_PNG_COMPRESSION,0])
        return 0

def BPM_Read(Sensor_Name):
    #Rücklesen wie viele BPMs es gibt Aus Dateiname
    x=os.listdir(dir_path)
    #Davon Sensor
    Nr=0
    for i in range(len(x)):
        DatName=str(x[i])
        if DatName.find(Sensor_Name) !=-1:
            Start=DatName.find("V",len(Sensor_Name))
            Ende=DatName.find(".",len(Sensor_Name))
            sZahl=DatName[Start+1:Ende]
            #print(sZahl)
            Zahl=int(sZahl)
            if(Zahl>Nr):
                Nr=Zahl
                y=x[i]
    if Nr==0:
        print("Kein Korrekturdatensatz vorhanden, muss Erstellt werden") #Error Meldungen in GUI?
        return -1
    else:
        Datei_path=os.sep.join([dir_path,Sensor_Name+"_V"+str(Nr)+".png"])
        BPM = imP.importFunction(Datei_path) #???
        return BPM[0]

global dir_path
#dir_path = '%s\\Bad_Pixel Map\\' %  os.environ['APPDATA'] 
#os.path.join(os.environ['HOME'], 'MYPROJECT')
dir_path = core.QStandardPaths.writableLocation(core.QStandardPaths.AppDataLocation)
dir_path=os.sep.join([dir_path,"Bad_Pixel Maps"])
print(dir_path)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)