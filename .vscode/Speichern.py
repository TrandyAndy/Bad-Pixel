import os
import cv2
import importPictures as imP

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
        cv2.imwrite(dir_path + "/" + Sensor_Name + "_V" + str(Nr) + ".png", BPM, [cv2.IMWRITE_PNG_COMPRESSION,0])
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
        Print("Kein Korrekturdatensatz vorhanden, muss Erstellt werden") #Error Meldungen in GUI?
        return -1
    else:
        BPM = imP.importFunction(dir_path+"//"+Sensor_Name+"_V"+str(Nr)+".png") #???
        return BPM[0]

global dir_path
dir_path = '%s\\Bad_Pixel Map\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)