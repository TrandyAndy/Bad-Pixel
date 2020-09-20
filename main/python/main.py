"""
/*
 * @Author: Julian Schweizerhof und Andreas Bank
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-09-20 16:41:38
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-09-20 18:41:14
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
# lokale Bibliotheken
import importPictures as imP
import exportPictures as exP

""" Beginn der Hauptfunktion:__________________________________________________________________________________"""
if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext    # für das fbs

    """ Globale Variablen:___________________________________________________________________________________ """
    aktuellerTab = 0    # Zustand des Tabs der GUI
    anzahlBilder = 0    # Anzahl der importierten Bilder für die Zeilenanzahl der Tabelle
    sensorList = ["Bitte Ihren Sensor auswählen"]

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
    msgBox = widgets.QMessageBox()  # Die Message Box

    """ Funktionen für die GUI:___________________________________________________________________________________ """
    ############ Allgemeine Funktionen ########################################################################################
    def startClicked():
        global aktuellerTab
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



        # Import Pictures

        # Suchen

        # Korrigieren

        # Export Aufruf
        # image = imP.importFunction("/Users/julian/Desktop/simulationsbild.tif")
        # exP.exportPictures(mW.lineEditSpeicherort.text(), mW.tableWidgetBilddaten.item(0,0).text(), image[0])


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
    def mWButtonBackClicked():
        global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
        if aktuellerTab > 0:
            aktuellerTab = aktuellerTab - 1
        mW.tabWidget.setCurrentIndex(aktuellerTab)
        if aktuellerTab < 3:
            mW.pushButtonMainForward.setText("Weiter")
        if aktuellerTab <= 0:
            mW.pushButtonMainBack.setVisible(False)
        # print(aktuellerTab)   # debug      
    def mWButtonForwardClicked():
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
    def mWTabChanged():
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
        aktuellerTab = mW.tabWidget.currentIndex()
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
        # Einstellungen Korrigieren
        eKSliderNachbarFensterbreite()
        eKSliderGradientFensterbreite()
    ############ Funktionen von dem ab Sensor / BPM ########################################################################################
    def mWBPMComboBoxSensor():
        print("mWBPMComboBoxSensor")
    def mWBPMComboBoxBPM():
        print("mWBPMComboBoxBPM")
    def mWBPMButtonNeuerSensor():
        # Ordner auswählen: getExistingDirectory(), Datei auswählen: getOpenFileName(), Dateien auswählen: filename = widgets.QFileDialog.getOpenFileNames() [0]      
        # filename = widgets.QFileDialog.getOpenFileNames() [0]      
        # filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "UI-Dateien (*.ui)")
        # mW.lineEditBPM.setText(filename)
        #print("Ordnerdialog geöffnet", filename)
        if nB.exec() == widgets.QDialog.Accepted:
            global sensorList
            sensorList.append(nB.lineEditNeueBPM.text())
            #mW.comboBoxBPMSensor.clear()
            #mW.comboBoxBPMSensor.addItems(sensorList)
            mW.comboBoxBPMSensor.addItem(sensorList[-1])    # -1 letzes Elemt 
            mW.comboBoxBPMSensor.setCurrentIndex( len(sensorList) - 1) # -1 da Informatiker ab 0 zählen
            print("Läuft 3")
        print("NeueBPM geöffnet")   # debug
    def mWBPMButtonSensorLoeschen():
        aktuellerIndex = mW.comboBoxBPMSensor.currentIndex()
        print(aktuellerIndex)
        if aktuellerIndex == 0:
            pass
        else:
            del sensorList[aktuellerIndex]
            mW.comboBoxBPMSensor.removeItem(aktuellerIndex)
        pass
    def mWBPMButtonBPMLoeschen():
        pass
    def setEnabledBPM(flag):
        mW.labelBPMchoose.setEnabled(flag)
        #mW.labelBPMChoose.setText(core.QStandardPaths.writableLocation(core.QStandardPaths.AppDataLocation))
        mW.comboBoxBPMBPM.setEnabled(flag)

    setEnabledBPM(False)   

    ### Tab Bilddaten
    def mWBilddatenButtonOrdnerDurchsuchen():   # Ordner importieren
        dirname = widgets.QFileDialog.getExistingDirectory(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation))    
        if dirname != "":  # wenn nicht auf abbrechen gedrückt wird
            mW.lineEditBilddatenDurchsuchen.setText(dirname)
            print(os.listdir(dirname))
        else:
            print("Abgebbrochen")
        print("Ordnerdialog Bilddaten geöffnet", dirname)
    def mWBilddatenButtonImportieren():
        global anzahlBilder
        dirname = mW.lineEditBilddatenDurchsuchen.text()
        if os.path.exists(dirname): # wenn der Pfad überhaupt existiert
            if mW.checkBoxBilddaten.isChecked():   # Unterordner auch importieren
                print("Unterordner werden auch importiert")
            else:   # keine Unterordner importieren
                #if dirname != "": 
                files = os.listdir(dirname) # bug, wenn dirname kein bekannter Pfad ist
                print(files,type(files))
                anzahlBilderLocal = 0
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
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,3, widgets.QTableWidgetItem(  farbtiefe ) )
                    mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,4, widgets.QTableWidgetItem( str(os.path.join(dirname,imageFiles[index])) ) )# Die Pfade aller Bilder in die dritten Spalte schreiben
                    # zentrieren
                    mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(imageFiles))), 1).setTextAlignment(core.Qt.AlignCenter)
                    mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(imageFiles))), 2).setTextAlignment(core.Qt.AlignCenter)
                    mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(imageFiles))), 3).setTextAlignment(core.Qt.AlignCenter)
                #else:
                #print("Abgebbrochen")
                print("Keine Unterordner importieren")

        else:
            openMessageBox(icon=widgets.QMessageBox.Information, text="Der eingegebene Pfad ist nicht gültig",informativeText="Der Pfad: \"" + dirname + "\" ist kein gültiger Pfad. Bitte ändern Sie den eingegebenen Pfad.",windowTitle="Kein gültiger Pfad",standardButtons=widgets.QMessageBox.Ok,pFunction=msgButtonClick)
        
            
    def buttonBilddatenAddDurchsuchen():    # Bilddateien importieren
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
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,3, widgets.QTableWidgetItem(  farbtiefe ) )
            mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,4, widgets.QTableWidgetItem( str(filename[index]) ) )# Die Pfade aller Bilder in die dritten Spalte schreiben
            mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(filename))), 1).setTextAlignment(core.Qt.AlignCenter)
            mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(filename))), 2).setTextAlignment(core.Qt.AlignCenter)
            mW.tableWidgetBilddaten.item((index + (anzahlBilder - len(filename))), 3).setTextAlignment(core.Qt.AlignCenter)
        #print(os.path.basename(filename[0]))
        imP.importUIFunction(filename[0])
        if imP.checkGreyimage(filename[0]):
            print("Graubild")
        else:
            print("Farbbild")

        # print("buttonBilddatenAddDurchsuchen")    # debug
    
    def buttonBilddatenDelete():
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
        print("buttonBilddatenDelete")
        
    def buttonBilddatenDeleteAll():
        #mW.tableWidgetBilddaten.clearContents()
        #mW.tableWidgetBilddaten.removeRow()
        mW.tableWidgetBilddaten.setRowCount(0)
        #mW.tableWidgetBilddaten.setRowCount(1)
        global anzahlBilder
        anzahlBilder = 0
        print("buttonBilddatenDeleteAll")
    ### Tab Speicherort
    def buttonSpeicherortDurchsuchen():
        filename = widgets.QFileDialog.getExistingDirectory(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation))    
        mW.lineEditSpeicherort.setText(filename)
        print("buttonSpeicherortDurchsuchen")
    ### Tab Algorithmus
    def suchenEnable():
        if mW.checkBoxAlgorithmusSuchen.isChecked():
            mW.groupBoxSuchen.setEnabled(True)
            #print("Checked")
        else:
            mW.groupBoxSuchen.setEnabled(False)
            #print("not Checked")
        #print("Suchen")
    def korrigierenEnable():
        if mW.checkBoxAlgorithmusKorrigieren.isChecked():
            mW.groupBoxKorrigieren.setEnabled(True)
            #print("Checked")
        else:
            mW.groupBoxKorrigieren.setEnabled(False)
            #print("not Checked")
    def buttonAlgorithmusSuchenEinstellungen():
        if eS.exec() == widgets.QDialog.Accepted:
            print("Läuft")
        #eS.exec()
    def buttonAlgorithmusKorrigierenEinstellungen():
        if eK.exec() == widgets.QDialog.Accepted:
            print("Läuft 2")
    def mWCheckBoxAlgorithmusFFK():
        if mW.checkBoxAlgorithmusFFK.isChecked():
            if fF.exec() == widgets.QDialog.Accepted:
                print("Läuft")
    ### Flat-Field-Korrektur

    def radioButtonFlatFieldKorrekturGespeicherte():
        fF.groupBox.setEnabled(False)
        print("Radio Button FFK Dunkel")
    def radioButtonFlatFieldKorrekturNeue():
        fF.groupBox.setEnabled(True)
        print("Radio Button FFK Hell")

    ### Einstellungen Suchen
    
    ### Einstellungen Korrektur 
    eK.horizontalSliderNachbarFensterbreite.setMinimum(1)
    eK.horizontalSliderNachbarFensterbreite.setMaximum(4)
    eK.horizontalSliderNachbarFensterbreite.setTickInterval(1)
    eK.horizontalSliderGradientFensterbreite.setMinimum(1)
    eK.horizontalSliderGradientFensterbreite.setMaximum(4)
    eK.horizontalSliderGradientFensterbreite.setTickInterval(1)
    def eKSliderNachbarFensterbreite():
        value = eK.horizontalSliderNachbarFensterbreite.value()
        #eK.labelNachbarFensterbreite.setStyleSheet('color: red')
        eK.labelNachbarFensterbreite.setText(str((value*2)+1))  # 3, 5, 7, 9
        print("eKSliderNachbarFensterbreite", value)   # debug
    def eKSliderGradientFensterbreite():
        value = eK.horizontalSliderGradientFensterbreite.value()
        #eK.labelNachbarFensterbreite.setStyleSheet('color: red')
        eK.labelGradientFensterbreite.setText(str((value*2)+1))  # 3, 5, 7, 9
        print("eKSliderGradientFensterbreite", value)   # debug

     
    #### UI Aktionen #### 
    ### Allgemein
    uiSetup()
    mW.pushButtonMainBack.clicked.connect(mWButtonBackClicked)
    mW.pushButtonMainForward.clicked.connect(mWButtonForwardClicked)
    mW.tabWidget.currentChanged.connect(mWTabChanged)

    ### Tab Sensor / BPM
    mW.comboBoxBPMSensor.activated.connect(mWBPMComboBoxSensor)
    mW.comboBoxBPMBPM.activated.connect(mWBPMComboBoxBPM)
    mW.pushButtonBPMNeuerSensor.clicked.connect(mWBPMButtonNeuerSensor)
    mW.pushButtonBPMSensorLoeschen.clicked.connect(mWBPMButtonSensorLoeschen)
    mW.pushButtonBPMBPMLoeschen.clicked.connect(mWBPMButtonBPMLoeschen)

    ### Tab Bilddaten
    mW.pushButtonBilddatenOrdnerDurchsuchen.clicked.connect(mWBilddatenButtonOrdnerDurchsuchen)
    mW.pushButtonBilddatenImportieren.clicked.connect(mWBilddatenButtonImportieren)
    mW.pushButtonBilddatenAdd.clicked.connect(buttonBilddatenAddDurchsuchen)
    mW.pushButtonBilddatenDelete.clicked.connect(buttonBilddatenDelete)
    mW.pushButtonBilddatenDeleteAll.clicked.connect(buttonBilddatenDeleteAll)


    ### Tab Speicherort
    mW.pushButtonSpeicherortDurchsuchen.clicked.connect(buttonSpeicherortDurchsuchen)

    ### Tab Algorithmus
    mW.checkBoxAlgorithmusSuchen.stateChanged.connect(suchenEnable)
    mW.pushButtonAlgorithmusSuchenEinstellungen.clicked.connect(buttonAlgorithmusSuchenEinstellungen)
    mW.checkBoxAlgorithmusKorrigieren.stateChanged.connect(korrigierenEnable)
    mW.pushButtonAlgorithmusKorrigierenEinstellungen.clicked.connect(buttonAlgorithmusKorrigierenEinstellungen)
    mW.checkBoxAlgorithmusFFK.stateChanged.connect(mWCheckBoxAlgorithmusFFK)
    eS.groupBoxSchwellwert.setToolTip("Hinweise für die Einstellung der Schwellwerte: \nAchtung ein Schwellwert über 0,1 ist Lebensmüde!")
    eS.groupBoxMoving.setToolTip("Hinweise für die Einstellung des Moving-Window: \nAchtung ein Schwellwert über 0,1 ist Lebensmüde!")
    eS.groupBoxDynamic.setToolTip("Hinweise für die Einstellung des Dynamic-Check: \nAchtung ein Schwellwert über 0,1 ist Lebensmüde!")

    ### Flat-Field-Korrektur
    fF.radioButtonGespeicherteBilder.clicked.connect(radioButtonFlatFieldKorrekturGespeicherte)
    fF.radioButtonNeueBilder.clicked.connect(radioButtonFlatFieldKorrekturNeue)
    
    ### Einstellungen Suchen
    
    ### Einstellungen Korrektur
    eK.horizontalSliderNachbarFensterbreite.valueChanged.connect(eKSliderNachbarFensterbreite)
    eK.horizontalSliderGradientFensterbreite.valueChanged.connect(eKSliderGradientFensterbreite)
    
    #### QT UI anzeigen####
    mW.show()




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