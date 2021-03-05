# Python program to write JSON 
# to a file 



import Speichern

DATA=Speichern.Read_json() #Lesen zu Beginn #-1 Abfangen?!
print("Hi ", DATA["Firma"], "was macht der ",DATA["Sensors"][0]["Sensor_Name"])
print(Speichern.WelcheSensorenGibtEs(DATA))
Speichern.SensorAnlegen("Julian", DATA)
Speichern.SensorLoschen("Andy",DATA)
Speichern.Write_json(DATA) #Schreiben am Ende

""" 
# Data to be written 
global ReadFlag
ReadFlag=False #Start vom Programm
InitConfigData ={ 
    "Firma" : "Roematek",
    "Autor": "Julian und Andy",
    "Datum" : str(date.today()), 
    "Sensors" : [
        {
            "Sensor_Name" : "Bitte Sensor anlegen",
            "Erstell_Datum" : 19950101,
            "Anz_Bilder" : 0, 
	        "last_Fensterbreite_advWindow" : "88",
            "last_Faktor_advWindow" : "3",
            "last_Schwellwert_oben" : "99",
            "last_Schwellwert_unten" : "0.1",
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
    json_path=os.sep.join([Speichern.dir_path,"config.json"])
    with open(json_path, "w") as outfile: 
	    outfile.write(json_object) 
    return 0

def WelcheSensorenGibtEs(Data):
    Anz=len(DATA["Sensors"])
    Sensor=[]
    for i in range(Anz):
        Buf=(DATA["Sensors"][i]["Sensor_Name"])
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
	        "last_Fensterbreite_advWindow" : "88",
            "last_Faktor_advWindow" : "3",
            "last_Schwellwert_oben" : "99",
            "last_Schwellwert_unten" : "0.1",
            "last_Faktor_Dynamik" : "8",
            "last_korrekturmethode" : "NSRA"
        })
    return 0

def SensorLoschen(Name,Data):
    #Prüfen ob vorhanden:
    for i in range(len(Data["Sensors"])):
        if Name ==Data["Sensors"][i]["Sensor_Name"]:
            del Data["Sensors"][i]
            print("geloescht")
            return 0
    print("Nicht gefunden")
    return -1 """


