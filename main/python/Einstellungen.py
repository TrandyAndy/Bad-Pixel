# Python program to write JSON 
# to a file 


import json 
import Speichern #soll Später alles in Speichern
import os
from datetime import date

# Data to be written 
global GlobalConfigData, ReadFlag
ReadFlag=False #Start vom Programm
GlobalConfigData ={ 
    "Firma" : "Roematek",
    "Autor": "Julian und Andy",
    "Datum" : str(date.today()), 
    "Sensors" : [
        {
            "Sensor_Name" : "X-0815",
            "Erstell_Datum" : 19950101,
            "Anz_Bilder" : 0, 
	        "last_Fensterbreite_advWindow" : "88",
            "last_Faktor_advWindow" : "3",
            "last_Schwellwert_oben" : "99",
            "last_Schwellwert_oben" : "0.1",
            "last_Faktor_Dynamik" : "8",
            "last_korrekturmethode" : "NSRA"
        }
    ],
    "last_GenutzterSensor" : "choose a Sensor",
    "Flat_Field_Bilder": [
        {
            "Hell_Bild": False,
            "Dunkel_Bild": False
        }
    ]
    

} 


def Read_json():
    json_path=os.sep.join([Speichern.dir_path,"config.json"])
    #Json Suchen bzw Anlegen.
    if not os.path.exists(json_path):
        Write_json(0)#dump
        print("Json config nicht vorhanden. Erstellen...")
        return -1
    #Json Laden (Open ...)
    with open(json_path, "r") as openfile: 
	# Reading from json file 
	    json_object = json.load(openfile)
    print(json_object) 
    print(type(json_object))
    ReadFlag=True
    return json_object

def Write_json(Data): #Oder immer zu Laufzeit
    # Serializing json 
    json_object = json.dumps(Data, indent = 4,sort_keys=True) 
    json_path=os.sep.join([Speichern.dir_path,"config.json"])
    with open(json_path, "w") as outfile: 
	    outfile.write(json_object) 
    return 0

def JRead_Sensor_Name(json_object,JustDoIt=False):
    if ReadFlag==False or JustDoIt==True:
        json_objekt=Read_json()
    #Find String:
    json_object.find("Sensor_Name") 
    return Data

Write_json(GlobalConfigData)
Read_json()