# Python program to write JSON 
# to a file 


import json 

# Data to be written 
data ={ 
    "Firma" : "Römatek",
	"Sensor" : "X-0815", 
	"Datum" : 20200915, 
	"Anz_Bilder" : 0, 
	"last_Fensterbreite_advWindow" : "8",
    "Flat_Field_Bilder": [
        {
            "Hell_Bild": False,
            "Dunkel_Bild": False
        }
    ],
    "Autor": "Julian und Andy"

} 

# Serializing json 
json_object = json.dumps(data, indent = 4) 

# Writing to sample.json 
with open("config.json", "w") as outfile: 
	outfile.write(json_object) 



# Python program to read JSON 
# from a file 

# Opening JSON file 
with open('config.json', 'r') as openfile: 

	# Reading from json file 
	json_object = json.load(openfile) 

print(json_object) 
print(type(json_object)) 



def Startup():
    #Json Suchen bzw Anlegen.
    #Json Laden (Open ...)
    return 0

def Exit(): #Oder immer zu Laufzeit
    #Global Json Dump
    #Json Close
    return 0