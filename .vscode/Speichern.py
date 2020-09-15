

def BPM_Save(pBPM_Path, BPM, Sensor_Name):
    #Rücklesen wie viele BPMs es gibt Aus Dateiname
    x=os.listdir(pBPM_Path)
    #Davon Sensor
    #x=sort....
    if x>500:
        return -1
    else:
        #Höchste Nr Finden:
        Nr=0
        #Schreiben
        Nr=Nr+1
        cv2.imwrite(Sensor_Name + "_V" + Nr + ".png", BPM, [cv2.IMWRITE_PNG_COMPRESSION,0])
        return 0

def BPM_Read(pBPM_Path, Sensor_Name):
    #Rücklesen wie viele BPMs es gibt Aus Dateiname
    x=os.listdir(pBPM_Path)
    #Davon Sensor
    #x=sort....
    if x==0:
        Print("Kein Korrekturdatensatz vorhanden, muss Erstellt werden") #Error Meldungen in GUI?
        return -1
    else:
        BPM = imP.importFunction(pBPM_Path+"/"+Sensor_Name+"_V"+Nr+".png") #???
        return BPM