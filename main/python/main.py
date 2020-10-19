"""
/*
 * @Author: Julian Schweizerhof und Andreas Bank
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-10-16 12:09:24
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-10-16 13:05:43
 * @Description: Main des Projektes, primär ermöglicht diese Datei die GUI
 */
"""

""" Import der Bibliotheken:__________________________________________________________________________________"""
# globale Bibliotheken
from fbs_runtime.application_context.PyQt5 import ApplicationContext    # für das fbs
import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic
import types
import os
import numpy as np
from _thread import start_new_thread, allocate_lock #oder mit therading lib.
import threading
import platform     # für das Öffnen des File Explores
import subprocess   # für das Öffnen des File Explores
from datetime import datetime
# lokale Bibliotheken
import importPictures as imP
import exportPictures as exP
import Speichern
import config as cfg
import detection
import correction

""" Beginn der Hauptfunktion:__________________________________________________________________________________"""
if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext    # für das fbs

    """ Globale Variablen:___________________________________________________________________________________ """
    aktuellerTab = 0    # Zustand des Tabs der GUI
    anzahlBilder = 0    # Anzahl der importierten Bilder für die Zeilenanzahl der Tabelle
    sensorList = ["Bitte Ihren Sensor auswählen"]
    bildDaten = 0       # hier werden die importierten Bilder gespeichert, 3D-Array: [anzahlBilder][Zeilen][Spalten]
    DATA = 0            # Die Daten für die Speicherung der Config Datei

    """ Laden der Gui-UI-Dateien:___________________________________________________________________________________ """
    app = widgets.QApplication(sys.argv)
    dateiMainWindow = appctxt.get_resource("badPixelMainWindow.ui")
    mW = uic.loadUi(dateiMainWindow)        # UI-Fenster MainWindow laden
    dateiNeueBPM = appctxt.get_resource("neueBPM.ui")
    nB = uic.loadUi(dateiNeueBPM)  
    dateiEinstellungSuchen = appctxt.get_resource("einstellungenSuchen.ui")
    eS = uic.loadUi(dateiEinstellungSuchen)  
    dateiEinstellungKorrigieren = appctxt.get_resource("einstellungenKorrigieren.ui")
    eK = uic.loadUi(dateiEinstellungKorrigieren)
    dateiFlatFieldKorrektur = appctxt.get_resource("flatFieldKorrektur.ui")
    fF = uic.loadUi(dateiFlatFieldKorrektur)
    dateiFortschritt = appctxt.get_resource("fortschritt.ui")
    fortschritt = uic.loadUi(dateiFortschritt)
    dateiBildFenster = appctxt.get_resource("bildFenster.ui")
    bildFenster = uic.loadUi(dateiBildFenster)
    msgBox = widgets.QMessageBox()  # Die Message Box

    """ Funktionen für die GUI:___________________________________________________________________________________ """
    ############ Allgemeine Funktionen ########################################################################################
    def startClicked():
        global aktuellerTab
        #Speichern wie bei forward
        Speichern.Write_json(DATA) #Schreiben am Ende   # Julian: eigentlich unnötig, da startClicked einem Forward Klick entspricht
        # Check BPM is valid
        # Check Bilddaten is valid
        if mW.tableWidgetBilddaten.rowCount() == 0:
            openMessageBox(icon=widgets.QMessageBox.Information, text="Keine Bilder importiert",informativeText="Bitte importieren Sie Bilder.",windowTitle="Keine Bilder importiert",standardButtons=widgets.QMessageBox.Ok,pFunction=msgButtonClick)
            aktuellerTab = 1
            mW.tabWidget.setCurrentIndex(aktuellerTab)
            return False
        for aktuelleZeile in range(mW.tableWidgetBilddaten.rowCount()):
            if mW.tableWidgetBilddaten.item(0, 1).text() != mW.tableWidgetBilddaten.item(aktuelleZeile, 1).text():
                openMessageBox(icon=widgets.QMessageBox.Information, text="Die Auflösung der importierten Bilder ist unterschiedlich",informativeText="Bitte entfernen Sie die falschen Bilder.",windowTitle="Falsche Auflösung",standardButtons=widgets.QMessageBox.Ok,pFunction=msgButtonClick)
                aktuellerTab = 1
                mW.tabWidget.setCurrentIndex(aktuellerTab)
                return False
        # Check Speicherort is valid
        if os.path.exists(mW.lineEditSpeicherort.text()) == False:
            openMessageBox(icon=widgets.QMessageBox.Information, text="Der eingegebene Pfad für den Speicherort ist nicht gültig",informativeText="Der Pfad: \"" + mW.lineEditSpeicherort.text() + "\" ist kein gültiger Pfad. Bitte ändern Sie den eingegebenen Pfad.",windowTitle="Kein gültiger Pfad",standardButtons=widgets.QMessageBox.Ok,pFunction=msgButtonClick)
            aktuellerTab = 2
            mW.tabWidget.setCurrentIndex(aktuellerTab)
            return False
        # Check Algorithmus is valid

        # Update UI
        fortschritt.textEdit.clear()    # Info Textfeld löschen
        fortschritt.buttonBox.button(widgets.QDialogButtonBox.Ok).setEnabled(False) # Okay Button disable
        # Import Pictures
        
        global bildDaten
        pathlist = []
        for index in range(anzahlBilder):   # alle Pfade aus der Tabelle in eine Liste schreiben
            pathlist.append(mW.tableWidgetBilddaten.item(index,4).text())
        if mW.checkBoxRohbilderSpeichern.isChecked():
            bildDaten = imP.importUIFunction(pathlist,pMittelwert=True, pExport=True, pExportPath= mW.lineEditSpeicherort.text())
            fortschritt.textEdit.insertPlainText("Rohbilder wurden unter: \"" + mW.lineEditSpeicherort.text() + "\" gespeichert.\n")
        else:
            bildDaten = imP.importUIFunction(pathlist,pMittelwert=True, pExport=False)
        

        


            #if( np.shape(imP.importUIFunction(mW.tableWidgetBilddaten.item(index,4).text())) [0] > 1):
            #print(np.shape(imP.importUIFunction(mW.tableWidgetBilddaten.item(index,4).text())) [0])
            #bildDaten.append( imP.importUIFunction(mW.tableWidgetBilddaten.item(index,4).text()) [0] ) #Mehre Bilder gehen nicht...
        #print(np.shape(bildDaten)) 

        #Ladebalken init
        cfg.Ladebalken=0
        Anz=int(mW.checkBoxAlgorithmusSchwellwertfilter.isChecked())+int(mW.checkBoxAlgorithmusWindow.isChecked())+int(mW.checkBoxAlgorithmusDynamic.isChecked())
        cfg.LadebalkenMax=Anz*np.shape(bildDaten)[0]
        print("Rechenschritte=",cfg.LadebalkenMax)
        # Suchen Treads
        IDs=[]
        if mW.checkBoxAlgorithmusSuchen.isChecked():
            if(mW.checkBoxAlgorithmusSchwellwertfilter.isChecked()):
                #BPM_Schwellwert=detection.MultiPicturePixelCompare(bildDaten,GrenzeHot=0.995,GrenzeDead=0.1)[0]
                T_ID_MPPC=threading.Thread(target=detection.MultiPicturePixelCompare,args=(bildDaten,float(eS.labelSchwellwertHot.text()),float(eS.labelSchwellwertDead.text())))
                IDs.append(T_ID_MPPC)
                T_ID_MPPC.start()
            if(mW.checkBoxAlgorithmusDynamic.isChecked()):
                #BPM_Dynamik=detection.dynamicCheck(bildDaten,Faktor=1.03)[0]
                T_ID_dC=threading.Thread(target=detection.dynamicCheck,args=(bildDaten,float(eS.labelDynamicSchwellwert.text())))
                IDs.append(T_ID_dC)
                T_ID_dC.start()
            if(mW.checkBoxAlgorithmusWindow.isChecked()):
                #BPM_Window=detection.advancedMovingWindow(bildDaten[0],Faktor=2.0,Fensterbreite=10)[0] 
                T_ID_aMW=threading.Thread(target=detection.advancedMovingWindow,args=(bildDaten,int(eS.labelMovingFensterbreite.text()),float(eS.labelMovingSchwellwert.text())))
                IDs.append(T_ID_aMW)
                T_ID_aMW.start()
        #====Jetzt wird gesucht!====#
        timer.start(500) # ms heruntersetzen für Performance
        fortschritt.progressBar.setValue(0)
        if fortschritt.exec() == widgets.QDialog.Rejected: #Abbrechen
            print("Gecancelt gedrückt") # hier muss dann der Prozess gestoppt werden. 
            cfg.holocaust=True #alle Treads killen
            cfg.Ladebalken=0
            timer.stop() #Prozess ist damit abgeschalten.
            print("Try to join")
            for ID in IDs:
                if ID.is_alive():
                    ID.join()
                    print(ID,"der leuft ja noch!")
            print("Treads sind alle tot")
            cfg.holocaust=False

        print("startClicked")   # debug
    def msgButtonClick():
        print("message")
        pass
    def openMessageBox(icon, text, informativeText, windowTitle, standardButtons, pFunction):
        msgBox.setIcon(icon) # msgBox.setIcon(widgets.QMessageBox.Information)
        msgBox.setText(text) # msgBox.setText("Der eingegebene Pfad für den Speicherort ist nicht gültig")
        msgBox.setInformativeText(informativeText) # msgBox.setInformativeText("Der Pfad: \"" + mW.lineEditSpeicherort.text() + "\" ist kein gültiger Pfad. Bitte ändern Sie den eingegebenen Pfad.")
        msgBox.setWindowTitle(windowTitle) #msgBox.setWindowTitle("Kein gültiger Pfad")
        msgBox.setStandardButtons(standardButtons) #msgBox.setStandardButtons(widgets.QMessageBox.Ok) # | widgets.QMessageBox.Cancel)
        msgBox.buttonClicked.connect(pFunction) # msgBox.buttonClicked.connect(msgButtonClick)
        returnValue = msgBox.exec()
        if returnValue == widgets.QMessageBox.Ok:
            print("OK clicked") # debug
        return returnValue        
    def mW_pushButtonMainBack():
        print(eS.labelMovingSchwellwert.text())
        global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
        if aktuellerTab > 0:
            aktuellerTab = aktuellerTab - 1
        mW.tabWidget.setCurrentIndex(aktuellerTab)
        if aktuellerTab < 3:
            mW.pushButtonMainForward.setText("Weiter")
        if aktuellerTab <= 0:
            mW.pushButtonMainBack.setVisible(False)
        # print(aktuellerTab)   # debug      
    def mW_pushButtonMainForward():
        global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
        if aktuellerTab >= 3:
            startClicked()
            return
        if aktuellerTab < 3:
            aktuellerTab = aktuellerTab + 1 
        mW.tabWidget.setCurrentIndex(aktuellerTab)
        if aktuellerTab >= 3:
            mW.pushButtonMainForward.setText("Start")
        if aktuellerTab > 0:
            mW.pushButtonMainBack.setVisible(True)
        # print(aktuellerTab)   # debug
        Speichern.Write_json(DATA) #Schreiben am Ende
    def mW_tabWidget():
        global aktuellerTab
        aktuellerTab = mW.tabWidget.currentIndex()
        # print(aktuellerTab)   # debug
        if aktuellerTab >= 3:
            mW.pushButtonMainForward.setText("Start")
        if aktuellerTab > 0:
            mW.pushButtonMainBack.setVisible(True)
        if aktuellerTab < 3:
            mW.pushButtonMainForward.setText("Weiter")
        if aktuellerTab <= 0:
            mW.pushButtonMainBack.setVisible(False)
    def uiSetup():  # alles was beim Laden passieren soll
        # Aktuelle Tab speichern
        global aktuellerTab
        global DATA
        aktuellerTab = mW.tabWidget.currentIndex()
        DATA=Speichern.Read_json() #Lesen zu Beginn #-1 Abfangen?!
        # Tab-Widget
        if aktuellerTab >= 3:
            mW.pushButtonMainForward.setText("Start")
        if aktuellerTab > 0:
            mW.pushButtonMainBack.setVisible(True)
        if aktuellerTab < 3:
            mW.pushButtonMainForward.setText("Weiter")
        if aktuellerTab <= 0:
            mW.pushButtonMainBack.setVisible(False)
        # Tab: Sensor/BPM
        sensorList=Speichern.WelcheSensorenGibtEs(DATA)[1]
        mW.comboBoxBPMSensor.addItems(sensorList)
        # Tab: Algorithmus - GroupBox Pixelfehler finden enablen
        if mW.checkBoxAlgorithmusSuchen.isChecked():
            mW.groupBoxSuchen.setEnabled(True)
            # print("Checked")  # debug
        else:
            mW.groupBoxSuchen.setEnabled(False)
            # print("not Checked")  # debug
        # Tab: Algorithmus - GroupBox Pixelfehler korrigieren enablen
        if mW.checkBoxAlgorithmusKorrigieren.isChecked():
            mW.groupBoxKorrigieren.setEnabled(True)
            # print("Checked")  # debug
        else:
            mW.groupBoxKorrigieren.setEnabled(False)
            # print("not Checked") # debug
        mW.checkBoxBilddaten.setVisible(False) # noch nicht implementiert
        # Einstellungen Suchen
        eS_horizontalSliderSchwellwertHot()
        eS_horizontalSliderSchwellwertDead()
        eS_horizontalSliderMovingFensterbreite()
        eS_horizontalSliderMovingSchwellwert()
        eS_horizontalSliderDynamicSchwellwert()
        # Einstellungen Korrigieren
        eK_horizontalSliderNachbarFensterbreite()
        eK_horizontalSliderGradientFensterbreite()
        # Fortschritt Fenster
        fortschritt.buttonBox.button(widgets.QDialogButtonBox.Ok).setEnabled(False) # Okay Button disable
    ############ Ende Allgemeine Funktionen ########################################################################################
    ############ Funktionen von dem ab Sensor / BPM ########################################################################################
    def mW_comboBoxBPMSensor():
        print("mW_comboBoxBPMSensor")
        DATA["last_GenutzterSensor"]=mW.comboBoxBPMSensor.currentText()
    def mW_comboBoxBPMBPM():
        print("mW_comboBoxBPMBPM")
    def mW_pushButtonBPMNeuerSensor():
        # Ordner auswählen: getExistingDirectory(), Datei auswählen: getOpenFileName(), Dateien auswählen: filename = widgets.QFileDialog.getOpenFileNames() [0]      
        # filename = widgets.QFileDialog.getOpenFileNames() [0]      
        # filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "UI-Dateien (*.ui)")
        # mW.lineEditBPM.setText(filename)
        #print("Ordnerdialog geöffnet", filename)
        if nB.exec() == widgets.QDialog.Accepted:
            global sensorList
            #sensorList.append(nB.lineEditNeueBPM.text())
            Speichern.SensorAnlegen(nB.lineEditNeueBPM.text(), DATA)
            sensorList=Speichern.WelcheSensorenGibtEs(DATA)[1]
            #mW.comboBoxBPMSensor.clear()
            #mW.comboBoxBPMSensor.addItems(sensorList)
            mW.comboBoxBPMSensor.addItem(sensorList[-1])    # -1 letzes Elemt 
            mW.comboBoxBPMSensor.setCurrentIndex( len(sensorList) - 1) # -1 da Informatiker ab 0 zählen
            print("Läuft 3")
        print("NeueBPM geöffnet")   # debug
    def mW_pushButtonBPMSensorLoeschen():
        aktuellerIndex = mW.comboBoxBPMSensor.currentIndex()
        currentText = mW.comboBoxBPMSensor.currentText()
        print(aktuellerIndex)
        if aktuellerIndex == 0:
            pass
        else:
            del sensorList[aktuellerIndex]
            mW.comboBoxBPMSensor.removeItem(aktuellerIndex)
            Speichern.SensorLoschen(currentText,DATA)
        pass
    def mW_pushButtonBPMBPMLoeschen():
        pass
    def setEnabledBPM(flag):
        mW.labelBPMchoose.setEnabled(flag)
        #mW.labelBPMChoose.setText(core.QStandardPaths.writableLocation(core.QStandardPaths.AppDataLocation))
        mW.comboBoxBPMBPM.setEnabled(flag)

    setEnabledBPM(False)   

    ### Tab Bilddaten
    def mW_pushButtonBilddatenOrdnerDurchsuchen():   # Ordner importieren
        if DATA["Import_Pfad"]==" ":
            dirname = widgets.QFileDialog.getExistingDirectory(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation))
        else:
            dirname = widgets.QFileDialog.getExistingDirectory(directory = DATA["Import_Pfad"])
        if dirname != "":  # wenn nicht auf abbrechen gedrückt wird
            mW.lineEditBilddatenDurchsuchen.setText(dirname)
            print(os.listdir(dirname))
        else:
            print("Abgebbrochen")
        print("Ordnerdialog Bilddaten geöffnet", dirname)
    def mW_pushButtonBilddatenImportieren():
        global anzahlBilder
        dirname = mW.lineEditBilddatenDurchsuchen.text()
        if os.path.exists(dirname): # wenn der Pfad überhaupt existiert
            if mW.checkBoxBilddaten.isChecked():   # Unterordner auch importieren    
                print("Unterordner werden auch importiert")
            else:   # keine Unterordner importieren
                #if dirname != "": 
                files = os.listdir(dirname) # bug, wenn dirname kein bekannter Pfad ist
                print(files,type(files))
                #anzahlBilderLocal = 0
                imageFiles = []
                for aktuellesFile in files:
                    dateiEndung = (os.path.splitext(aktuellesFile) [1]).lower() # lower für Windos
                    if dateiEndung == ".png" or dateiEndung == ".jpg" or dateiEndung == ".jpeg" or dateiEndung == ".tif" or dateiEndung == ".tiff" or dateiEndung == ".his":
                        #anzahlBilderLocal = anzahlBilderLocal + 1
                        imageFiles.append(aktuellesFile)
                anzahlBilder = anzahlBilder + len(imageFiles)
                mW.tableWidgetBilddaten.setRowCount(anzahlBilder) # Soviele Zeilen in der Tabelle aktivieren, wie es Bilder gibt.
                for index in range(len(imageFiles)):  # Alle importieren Bilder durchgehen
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,0, widgets.QTableWidgetItem(imageFiles[index]) ) # Den Dateinamen aller markierten Bilder in die erste Spalte schreiben
                    print(dirname + "/" + imageFiles[index])
                    rows, cols, anzahlHisBilder, farbtiefe = imP.getAufloesungUndAnzahlUndFarbtiefe(os.path.join(dirname,imageFiles[index]))
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,1, widgets.QTableWidgetItem( str(rows) + " x " + str(cols) ) )# Die Auflösung aller markierten Bilder in die erste Spalte schreiben
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,2, widgets.QTableWidgetItem( str( int(anzahlHisBilder)) ) )
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,3, widgets.QTableWidgetItem(  farbtiefe.name ) )
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,4, widgets.QTableWidgetItem( str(os.path.join(dirname,imageFiles[index])) ) )# Die Pfade aller Bilder in die dritten Spalte schreiben
                    # zentrieren
                    mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(imageFiles))), 1).setTextAlignment(core.Qt.AlignCenter)
                    mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(imageFiles))), 2).setTextAlignment(core.Qt.AlignCenter)
                    mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(imageFiles))), 3).setTextAlignment(core.Qt.AlignCenter)
                #else:
                #print("Abgebbrochen")
                print("Keine Unterordner importieren")
                #imP.importUIFunction(mW.tableWidgetBilddaten.item(0,4).text(),True)
                #exP.exportPictures(mW.lineEditSpeicherort.text(), mW.tableWidgetBilddaten.item(0,0).text(),GOOD)
            #Pfad Speichern
            DATA["Import_Pfad"]=dirname
        else:
            openMessageBox(icon=widgets.QMessageBox.Information, text="Der eingegebene Pfad ist nicht gültig",informativeText="Der Pfad: \"" + dirname + "\" ist kein gültiger Pfad. Bitte ändern Sie den eingegebenen Pfad.",windowTitle="Kein gültiger Pfad",standardButtons=widgets.QMessageBox.Ok,pFunction=msgButtonClick)
        
            
    def mW_pushButtonBilddatenAdd():    # Bilddateien importieren
        global anzahlBilder # globale Variable Anzahl der Bilder bekannt machen
        # file Dialog, kompatible Dateien: *.his *.png *.jpg *.jpeg *.tif *.tiff,
        # Alle Pfäde der Dateien werden in filename gespeichert
        filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "Bild-Dateien (*.his *.png *.jpg *.jpeg *.tif *.tiff)") [0]
        # print(filename) # debug
        anzahlBilder = anzahlBilder + len(filename) # Anzahl der Bilder aktualisieren
        mW.tableWidgetBilddaten.setRowCount(anzahlBilder) # Soviele Zeilen in der Tabelle aktivieren, wie es Bilder gibt.
        # print(anzahlBilder) # debug
        for index in range(len(filename)):  # Alle importieren Bilder durchgehen
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,0, widgets.QTableWidgetItem( os.path.basename(filename[index]))) # Den Dateinamen aller markierten Bilder in die erste Spalte schreiben
            rows, cols, anzahlHisBilder, farbtiefe = imP.getAufloesungUndAnzahlUndFarbtiefe(filename[index])
            # data = imP.importUIFunction(filename[index])
            # print(data, imP.np.shape(data))
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,1, widgets.QTableWidgetItem( str(rows) + " x " + str(cols) ) )# Die Auflösung aller markierten Bilder in die erste Spalte schreiben
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,2, widgets.QTableWidgetItem( str( int(anzahlHisBilder)) ) )
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,3, widgets.QTableWidgetItem(  farbtiefe.name ) )
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,4, widgets.QTableWidgetItem( str(filename[index]) ) )# Die Pfade aller Bilder in die dritten Spalte schreiben
            mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(filename))), 1).setTextAlignment(core.Qt.AlignCenter)
            mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(filename))), 2).setTextAlignment(core.Qt.AlignCenter)
            mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(filename))), 3).setTextAlignment(core.Qt.AlignCenter)
        #print(os.path.basename(filename[0]))
        #imP.importUIFunction(filename[0])
        #if imP.checkGreyimage(filename[0]):        ##### bug geht nicht bei HIS-Dateien
        #    print("Graubild")
        #else:
        #    print("Farbbild")
        #imP.importUIFunction(mW.tableWidgetBilddaten.item(0,4).text(),True)
        # print("mW_pushButtonBilddatenAdd")    # debug
    
    def mW_pushButtonBilddatenDelete():
        global anzahlBilder
        #print(mW.tableWidgetBilddaten.item(0,0).text())
        zeilen =  mW.tableWidgetBilddaten.selectedItems()
        print(zeilen)
        zeilenLoeschen = []
        alterWert = -1
        for index in zeilen:
            if alterWert != index.row():
                zeilenLoeschen.append( index.row() )
            alterWert = index.row()
            
        print(zeilenLoeschen)
        """
        for index in range(len(zeilen)):
            zeilenLoeschen.append( zeilen[index].row() )
        """
        zeilenLoeschen.sort()
        print(zeilenLoeschen)
        zeilenLoeschen.reverse()
        print(zeilenLoeschen)
        for index in range(len(zeilenLoeschen)):
            mW.tableWidgetBilddaten.removeRow(zeilenLoeschen[index]) 
        anzahlBilder = anzahlBilder - len(zeilenLoeschen)
        print(anzahlBilder)
        
        """
        print(mW.tableWidgetBilddaten.selectedIndexes())
        print(mW.tableWidgetBilddaten.selectedIndexes())
        print(mW.tableWidgetBilddaten.selectedRanges())
        #mW.tableWidgetBilddaten
        #core.QItemSelectionModel.reset()
        """
        
        """
        print(mW.tableWidgetBilddaten())

        widgets.QTableWidget

        mW.tableWidgetBilddaten.setRowCount(2)
        mW.tableWidgetBilddaten.setItem(0,0, widgets.QTableWidgetItem("Yeay"))
        mW.tableWidgetBilddaten.setItem(0,1, widgets.QTableWidgetItem("Yeay2"))
        mW.tableWidgetBilddaten.setItem(1,0, widgets.QTableWidgetItem("Yeay3"))
        mW.tableWidgetBilddaten.setItem(1,1, widgets.QTableWidgetItem("Yeay4"))
        
        mW.tableWidgetBilddaten.setItem(1,0, abc[0])
        mW.tableWidgetBilddaten.setItem(1,1, abc[1])
        """
        #mW.tableWidgetBilddaten.setItem(1,1, widgets.QTableWidgetItem("Yeay4"))
        print("mW_pushButtonBilddatenDelete")
        
    def mW_pushButtonBilddatenDeleteAll():
        #mW.tableWidgetBilddaten.clearContents()
        #mW.tableWidgetBilddaten.removeRow()
        mW.tableWidgetBilddaten.setRowCount(0)
        #mW.tableWidgetBilddaten.setRowCount(1)
        global anzahlBilder
        anzahlBilder = 0
        print("mW_pushButtonBilddatenDeleteAll")
    ### Tab Speicherort
    def mW_pushButtonSpeicherortDurchsuchen():
        if DATA["Export_Pfad"]==" ":
            filename = widgets.QFileDialog.getExistingDirectory(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation))    
        else:
            filename = widgets.QFileDialog.getExistingDirectory(directory = DATA["Export_Pfad"])    
        mW.lineEditSpeicherort.setText(filename)
        DATA["Export_Pfad"]=filename
        print("mW_pushButtonSpeicherortDurchsuchen")
    ### Tab Algorithmus
    def mW_checkBoxAlgorithmusSuchen():
        if mW.checkBoxAlgorithmusSuchen.isChecked():
            mW.groupBoxSuchen.setEnabled(True)
            #print("Checked")
        else:
            mW.groupBoxSuchen.setEnabled(False)
            #print("not Checked")
        #print("Suchen")
    def mW_checkBoxAlgorithmusKorrigieren():
        if mW.checkBoxAlgorithmusKorrigieren.isChecked():
            mW.groupBoxKorrigieren.setEnabled(True)
            #print("Checked")
        else:
            mW.groupBoxKorrigieren.setEnabled(False)
            #print("not Checked")
    def mW_pushButtonAlgorithmusSuchenEinstellungen():
        #Laden
        eS.horizontalSliderSchwellwertHot.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Schwellwert_oben"])
        eS.horizontalSliderSchwellwertDead.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Schwellwert_unten"])
        eS.horizontalSliderMovingFensterbreite.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fensterbreite_advWindow"])
        eS.horizontalSliderMovingSchwellwert.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Faktor_advWindow"])
        eS.horizontalSliderDynamicSchwellwert.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Faktor_Dynamik"])
        if eS.exec() == widgets.QDialog.Accepted:
            #Speichern
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Schwellwert_oben"]=eS.horizontalSliderSchwellwertHot.value()
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Schwellwert_unten"]=eS.horizontalSliderSchwellwertDead.value()            
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fensterbreite_advWindow"]=eS.horizontalSliderMovingFensterbreite.value()
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Faktor_advWindow"]=eS.horizontalSliderMovingSchwellwert.value()
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Faktor_Dynamik"]= eS.horizontalSliderDynamicSchwellwert.value()
        else:   # Die alten Werte wiederherstellen, da auf Abbrechnen geklickt wurde
            eS.horizontalSliderSchwellwertHot.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Schwellwert_oben"])
            eS.horizontalSliderSchwellwertDead.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Schwellwert_unten"])
            eS.horizontalSliderMovingFensterbreite.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fensterbreite_advWindow"])
            eS.horizontalSliderMovingSchwellwert.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Faktor_advWindow"])
            eS.horizontalSliderDynamicSchwellwert.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Faktor_Dynamik"])
    def mW_pushButtonAlgorithmusKorrigierenEinstellungen():
        eK.horizontalSliderNachbarFensterbreite.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fenster_Nachbar"])
        eK.horizontalSliderGradientFensterbreite.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fenster_Gradient"])
        Methode=DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_korrekturmethode"]
        eK.radioButtonMedian.setChecked(Methode==cfg.Methoden.NMFC.value)
        eK.radioButtonMittelwert.setChecked(Methode==cfg.Methoden.NARC.value)
        eK.radioButtonReplacement.setChecked(Methode==cfg.Methoden.NSRC.value)
        if eK.exec() == widgets.QDialog.Accepted:
            if eK.radioButtonMedian.isChecked():
                Methode=cfg.Methoden.NMFC
            elif eK.radioButtonMittelwert.isChecked():
                Methode=cfg.Methoden.NARC
            else:
                Methode=cfg.Methoden.NSRC
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fenster_Nachbar"]=eK.horizontalSliderNachbarFensterbreite.value()
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fenster_Gradient"]=eK.horizontalSliderGradientFensterbreite.value()
            DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_korrekturmethode"]=int(Methode.value)
        else:   # Die alten Werte wiederherstellen, da auf Abbrechnen geklickt wurde
            eK.horizontalSliderNachbarFensterbreite.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fenster_Nachbar"])
            eK.horizontalSliderGradientFensterbreite.setValue(DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_Fenster_Gradient"])
            eK.radioButtonMedian.setChecked(Methode==cfg.Methoden.NMFC)
            eK.radioButtonMittelwert.setChecked(Methode==cfg.Methoden.NARC)
            eK.radioButtonReplacement.setChecked(Methode==cfg.Methoden.NSRC)
    def mW_checkBoxAlgorithmusFFK():
        if mW.checkBoxAlgorithmusFFK.isChecked():
            if fF.exec() == widgets.QDialog.Accepted:
                print("Läuft")
    ### Flat-Field-Korrektur

    def fF_radioButtonGespeicherteBilder():
        fF.groupBox.setEnabled(False)
        print("Radio Button FFK Dunkel")
    def fF_radioButtonNeueBilder():
        fF.groupBox.setEnabled(True)
        print("Radio Button FFK Hell")

    ### Einstellungen Suchen
                                                        #Andy Vorgabe Multi: Hell: min 1 max 0,95 ival 0,01 Dunkel: min 0 max 0,05 ival 0,01
                                                        #Andy Vorgabe Moving Fenster: min 5 max 17 ival 2  Faktor: min 2 max 3,5 ival 0,1
                                                        #Andy Vorgabe Dynamic Empfindlichkeit: min 1.03 max 2 ival 0.01
    eS.horizontalSliderSchwellwertHot.setMinimum(0) 
    eS.horizontalSliderSchwellwertHot.setMaximum(5)
    eS.horizontalSliderSchwellwertHot.setTickInterval(1)
    def eS_horizontalSliderSchwellwertHot():
        value = eS.horizontalSliderSchwellwertHot.value()
        eS.labelSchwellwertHot.setText( str(round( value*(-0.01)+1,2) ) )

    eS.horizontalSliderSchwellwertDead.setMinimum(0) 
    eS.horizontalSliderSchwellwertDead.setMaximum(5)
    eS.horizontalSliderSchwellwertDead.setTickInterval(1)
    def eS_horizontalSliderSchwellwertDead():
        value = eS.horizontalSliderSchwellwertDead.value()
        eS.labelSchwellwertDead.setText( str(round(value*0.01,2) ) ) 

    eS.horizontalSliderMovingFensterbreite.setMinimum(0) 
    eS.horizontalSliderMovingFensterbreite.setMaximum(6)
    eS.horizontalSliderMovingFensterbreite.setTickInterval(1)
    def eS_horizontalSliderMovingFensterbreite():
        value = eS.horizontalSliderMovingFensterbreite.value()
        eS.labelMovingFensterbreite.setText( str(value*2 + 5) )

    eS.horizontalSliderMovingSchwellwert.setMinimum(0) 
    eS.horizontalSliderMovingSchwellwert.setMaximum(15)
    eS.horizontalSliderMovingSchwellwert.setTickInterval(1)
    def eS_horizontalSliderMovingSchwellwert():
        value = eS.horizontalSliderMovingSchwellwert.value()
        eS.labelMovingSchwellwert.setText( str( round(value*0.1 + 2, 2 ) ) )

    eS.horizontalSliderDynamicSchwellwert.setMinimum(0) 
    eS.horizontalSliderDynamicSchwellwert.setMaximum(97)
    eS.horizontalSliderDynamicSchwellwert.setTickInterval(1)
    def eS_horizontalSliderDynamicSchwellwert():
        value = eS.horizontalSliderDynamicSchwellwert.value()
        eS.labelDynamicSchwellwert.setText( str( round(value*0.01 + 1.03,2)  ) )     

    def eS_pushButtonVorschau():
        pixmap = gui.QPixmap("Bild.png")
        bildFenster.label.setPixmap(pixmap)
        bildFenster.label.setScaledContents(True)
        bildFenster.label.resize(pixmap.width(), pixmap.height())
        bildFenster.exec()
    ### Einstellungen Korrektur 
    eK.horizontalSliderNachbarFensterbreite.setMinimum(0) #Andy Vorgabe: min 3 max 21 ival 2 
    eK.horizontalSliderNachbarFensterbreite.setMaximum(9)
    eK.horizontalSliderNachbarFensterbreite.setTickInterval(2)
    def eK_horizontalSliderNachbarFensterbreite():
        value = eK.horizontalSliderNachbarFensterbreite.value()
        eK.labelNachbarFensterbreite.setText(str((value*2)+3))  # 3, 5, 7, 9 ... 21
        #if value > 9:
        #    eK.labelNachbarFensterbreite.setStyleSheet('color: red')
        #print("eK_horizontalSliderNachbarFensterbreite", value)   # debug
    eK.horizontalSliderGradientFensterbreite.setMinimum(0) #Andy Vorgabe: min 4 max 24 ival 2 
    eK.horizontalSliderGradientFensterbreite.setMaximum(10) #länge des Gradienten
    eK.horizontalSliderGradientFensterbreite.setTickInterval(2)
    def eK_horizontalSliderGradientFensterbreite():
        value = eK.horizontalSliderGradientFensterbreite.value()
        eK.labelGradientFensterbreite.setText(str((value*2)+4))  # 4, 6, 8 ... 22
        #if value > 10:
        #    eK.labelGradientFensterbreite.setStyleSheet('color: red')
        #else:
        #    eK.labelGradientFensterbreite.setStyleSheet('color: black')
        #print("eK_horizontalSliderGradientFensterbreite", value)   # debug

    def eK_pushButtonVorschau():
        pixmap = gui.QPixmap("Bild.png")
        bildFenster.label.setPixmap(pixmap)
        bildFenster.label.setScaledContents(True)
        bildFenster.label.resize(pixmap.width(), pixmap.height())
        bildFenster.exec()
    ### Fortschritt Fenster
    def fortschritt_pushButtonOeffnen():
        path = mW.lineEditSpeicherort.text()
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
        #print("Speicherort im File Explorer öffnen")   # debug

    """ GUI-Elemente mit Funktionen verbinden:___________________________________________________________________________________ """   
    #### UI Aktionen #### 
    ### Allgemein
    uiSetup()
    mW.pushButtonMainBack.clicked.connect(mW_pushButtonMainBack)
    mW.pushButtonMainForward.clicked.connect(mW_pushButtonMainForward)
    mW.tabWidget.currentChanged.connect(mW_tabWidget)

    ### Tab Sensor / BPM
    mW.comboBoxBPMSensor.activated.connect(mW_comboBoxBPMSensor)
    mW.comboBoxBPMBPM.activated.connect(mW_comboBoxBPMBPM)
    mW.pushButtonBPMNeuerSensor.clicked.connect(mW_pushButtonBPMNeuerSensor)
    mW.pushButtonBPMSensorLoeschen.clicked.connect(mW_pushButtonBPMSensorLoeschen)
    mW.pushButtonBPMBPMLoeschen.clicked.connect(mW_pushButtonBPMBPMLoeschen)

    ### Tab Bilddaten
    mW.pushButtonBilddatenOrdnerDurchsuchen.clicked.connect(mW_pushButtonBilddatenOrdnerDurchsuchen)
    mW.pushButtonBilddatenImportieren.clicked.connect(mW_pushButtonBilddatenImportieren)
    mW.pushButtonBilddatenAdd.clicked.connect(mW_pushButtonBilddatenAdd)
    mW.pushButtonBilddatenDelete.clicked.connect(mW_pushButtonBilddatenDelete)
    mW.pushButtonBilddatenDeleteAll.clicked.connect(mW_pushButtonBilddatenDeleteAll)

    ### Tab Speicherort
    mW.pushButtonSpeicherortDurchsuchen.clicked.connect(mW_pushButtonSpeicherortDurchsuchen)

    ### Tab Algorithmus
    mW.checkBoxAlgorithmusSuchen.stateChanged.connect(mW_checkBoxAlgorithmusSuchen)
    mW.pushButtonAlgorithmusSuchenEinstellungen.clicked.connect(mW_pushButtonAlgorithmusSuchenEinstellungen)
    mW.checkBoxAlgorithmusKorrigieren.stateChanged.connect(mW_checkBoxAlgorithmusKorrigieren)
    mW.pushButtonAlgorithmusKorrigierenEinstellungen.clicked.connect(mW_pushButtonAlgorithmusKorrigierenEinstellungen)
    mW.checkBoxAlgorithmusFFK.stateChanged.connect(mW_checkBoxAlgorithmusFFK)

    ### Flat-Field-Korrektur
    fF.radioButtonGespeicherteBilder.clicked.connect(fF_radioButtonGespeicherteBilder)
    fF.radioButtonNeueBilder.clicked.connect(fF_radioButtonNeueBilder)
    
    ### Einstellungen Suchen
    eS.horizontalSliderSchwellwertHot.valueChanged.connect(eS_horizontalSliderSchwellwertHot)
    eS.horizontalSliderSchwellwertDead.valueChanged.connect(eS_horizontalSliderSchwellwertDead)
    eS.horizontalSliderMovingFensterbreite.valueChanged.connect(eS_horizontalSliderMovingFensterbreite)
    eS.horizontalSliderMovingSchwellwert.valueChanged.connect(eS_horizontalSliderMovingSchwellwert)
    eS.horizontalSliderDynamicSchwellwert.valueChanged.connect(eS_horizontalSliderDynamicSchwellwert)
    eS.pushButtonVorschau.clicked.connect(eS_pushButtonVorschau)

    eS.groupBoxSchwellwert.setToolTip("Hinweise für die Einstellung der Schwellwerte: \nAchtung ein Schwellwert über 0,1 ist Lebensmüde!")
    eS.groupBoxMoving.setToolTip("Hinweise für die Einstellung des Moving-Window: \nAchtung ein Schwellwert über 0,1 ist Lebensmüde!")
    eS.groupBoxDynamic.setToolTip("Hinweise für die Einstellung des Dynamic-Check: \nAchtung ein Schwellwert über 0,1 ist Lebensmüde!")

    ### Einstellungen Korrektur
    eK.horizontalSliderNachbarFensterbreite.valueChanged.connect(eK_horizontalSliderNachbarFensterbreite)
    eK.horizontalSliderGradientFensterbreite.valueChanged.connect(eK_horizontalSliderGradientFensterbreite)
    eK.pushButtonVorschau.clicked.connect(eK_pushButtonVorschau)

    ### Fortschritt Fenster
    fortschritt.pushButtonOeffnen.clicked.connect(fortschritt_pushButtonOeffnen)

    #### QT UI anzeigen####
    mW.show()

    def Prozess(): #Hauptprozess nach Start
        if cfg.LadebalkenMax != 0:
            fortschritt.progressBar.setValue(int(cfg.Ladebalken/cfg.LadebalkenMax*100))
        else:
            fortschritt.progressBar.setValue(100)
        print("ladebalken = ",cfg.Ladebalken)
        # if i_Zeit>3000:
        #     print("Timeout Detection 404")  
        #     break

        #Abfrage Fertig_________
        FertigFlag=False
        cfg.lock.acquire()
        if cfg.Ladebalken==cfg.LadebalkenMax:
            print("Done")
            FertigFlag=True
        cfg.lock.release()

        if FertigFlag:
            fortschritt.textEdit.insertPlainText("Pixelfehler-Suche ist abgeschlossen.")
            timer.stop()
            #Zusammenfassen + Speichern oder Laden
            if mW.checkBoxAlgorithmusSuchen.isChecked():
                BAD_Ges=detection.Mapping(cfg.Global_BPM_Moving,cfg.Global_BPM_Multi,cfg.Global_BPM_Dynamik)*100 #Digital*100
                #BPM Speichern
                Speichern.BPM_Save(BAD_Ges*150,mW.comboBoxBPMSensor.currentText()) #BPM Speichern    #Nur wenn alles gut war!  und wenn Pixel gesucht wurden.
            else: #laden
                BAD_Ges=Speichern.BPM_Read(mW.comboBoxBPMSensor.currentText())
            
            # Korrigieren
            global bildDaten
            aktuelleZeit = str(datetime.now())[:-7].replace(":","-")    # aktuelle Zeit speichern
            if mW.checkBoxAlgorithmusKorrigieren.isChecked():
                Methode=DATA["Sensors"][int(mW.comboBoxBPMSensor.currentIndex())]["last_korrekturmethode"]
                ergCorrection = 0
                for i in range(np.shape(bildDaten)[0]):
                    if mW.radioButtonAlgorithmusNachbar.isChecked():
                        GOOD=np.uint16(correction.nachbar2(bildDaten[i],BAD_Ges,Methode,int(eK.labelNachbarFensterbreite.text())))
                    elif mW.radioButtonAlgorithmusGradient.isChecked():
                        GOOD=np.uint16(correction.Gradient(bildDaten[i],BAD_Ges,Methode,int(eK.labelGradientFensterbreite.text())))
                    #if mW.radioButtonAlgorithmusNagao():
                    # Export Aufruf______________________________________________________________
                    if np.shape(GOOD) == ():   # wenn GOOD eine -1 (Integer) ist
                        openMessageBox(icon=widgets.QMessageBox.Information, text="Die Auflösung der Bad-Pixel-Map und des Bildes sind unterschiedlich",informativeText="Bitte verwenden Sie andere Bilder.",windowTitle="Unterschiedliche Auflösungen",standardButtons=widgets.QMessageBox.Ok,pFunction=msgButtonClick)
                        fortschritt.textEdit.insertPlainText("Fehler beim Korrigieren.\n")
                    else:
                        exP.exportPictures(pPath= mW.lineEditSpeicherort.text(), pImagename= mW.tableWidgetBilddaten.item(0,0).text(), pImage= GOOD, pZeit= aktuelleZeit)
    
            fortschritt.textEdit.insertPlainText("Korrektur ist abgeschlossen.\n")       
            fortschritt.textEdit.insertPlainText("Fertig.\n")
            fortschritt.buttonBox.button(widgets.QDialogButtonBox.Ok).setEnabled(True) # Okay Button able
            # image = imP.importFunction("/Users/julian/Desktop/simulationsbild.tif")
    timer = core.QTimer()
    timer.timeout.connect(Prozess)
    

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()        # für das fbs
    sys.exit(exit_code)


""" Experimente: ___________________________________________________________________________________________
    sensorList = ["Bitte Ihren Sensor auswählen"]
    sensorList.append("CT1")
    sensorList.append("CT2")
    bpmList = ["Bitte die BPM auswählen"]
    bpmList.append("BPM vom 27.02.20")
    bpmList.append("BPM vom 28.02.20")
    mW.comboBoxBPMSensor.addItems(sensorList)
    mW.comboBoxBPMChoose.addItems(bpmList)
Experimente Ende """