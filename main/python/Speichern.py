import os
import cv2
import importPictures as imP
from pathlib import Path
import PyQt5.QtCore as core
import json 
from datetime import date
import config as cfg

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
                #y=x[i]
    if len(x)>200:
        print("Speicher voll")
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
                #y=x[i]
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

# Python program to write JSON 
# to a file 




# Data to be written 
global ReadFlag
ReadFlag=False #Start vom Programm
InitConfigData ={ 
    "Firma" : "Roematek",
    "Autor": "Julian und Andy",
    "Datum" : str(date.today()), 
    "Sensors" : [
        {
            "Sensor_Name" : "X-0815",
            "Erstell_Datum" : 19950101,
            "Anz_Bilder" : 0, 
            "Anz_PixelFehler" : 0, 
	        "last_Fensterbreite_advWindow" : 88,
            "last_Faktor_advWindow" : 3,
            "last_Schwellwert_oben" : 99,
            "last_Schwellwert_unten" : 1,
            "last_Faktor_Dynamik" : 8,
            "last_korrekturmethode" : 3,#int(cfg.Methoden.NSRC),
            "last_Fenster_Nachbar" : 5,
            "last_Fenster_Gradient" : 5,
            "Flat_Field_vorhanden" : False
        }
    ],
    "last_GenutzterSensor" : "erzeuge einen Sensor",
    "Import_Pfad" : " ",
    "Export_Pfad" : " ",
       

} 


def Read_json():
    json_path=os.sep.join([dir_path,"config.json"])
    #Json Suchen bzw Anlegen.
    if not os.path.exists(json_path):
        Write_json(InitConfigData)#dump
        print("Json config nicht vorhanden. Erstellen...")
        #return -1
    #Json Laden (Open ...)
    with open(json_path, "r") as openfile: 
	# Reading from json file 
	    json_object = json.load(openfile)
    # print(json_object) 
    # print(type(json_object))
    ReadFlag=True
    return json_object

def Write_json(Data): #Oder immer zu Laufzeit
    # Serializing json 
    json_object = json.dumps(Data, indent = 4,sort_keys=True) 
    json_path=os.sep.join([dir_path,"config.json"])
    with open(json_path, "w") as outfile: 
	    outfile.write(json_object) 
    return 0

def WelcheSensorenGibtEs(Data):
    Anz=len(Data["Sensors"])
    Sensor=[]
    for i in range(Anz):
        Buf=(Data["Sensors"][i]["Sensor_Name"])
        Sensor.append(Buf)
    return Anz, Sensor

def SensorAnlegen(Name,Data):
    #Prüfen ob vorhanden:
    for i in range(len(Data["Sensors"])):
        if Name ==Data["Sensors"][i]["Sensor_Name"]:
            print("Augen Auf beim Sensor Kauf")
            return -1
    Data["Sensors"].append({
            "Sensor_Name" : str(Name),
            "Erstell_Datum" : str(date.today()),
            "Anz_Bilder" : 0, 
            "Anz_PixelFehler" : 0, 
	        "last_Fensterbreite_advWindow" : 88,
            "last_Faktor_advWindow" : 3,
            "last_Schwellwert_oben" : 99,
            "last_Schwellwert_unten" : 1,
            "last_Faktor_Dynamik" : 8,
            "last_korrekturmethode" : 3,#int(cfg.Methoden.NSRC),
            "last_Fenster_Nachbar" : 5,
            "last_Fenster_Gradient" : 5,
            "Flat_Field_vorhanden" : False
        })
    return 0

def SensorLoschen(Name,Data):
    #Prüfen ob vorhanden:
    for i in range(len(Data["Sensors"])):
        if Name ==Data["Sensors"][i]["Sensor_Name"]:
            del Data["Sensors"][i]
            print("gelöscht")
            return 0
    print("Nicht gefunden")
    return -1


