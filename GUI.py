"""
/*
 * @Author: Julian Schweizerhof
 * @Email: diegruppetg@gmail.com
 * @Date: 2020-06-15 17:48:37
 * @Last Modified by: JLS666
 * @Last Modified time: 2020-09-14 12:56:03
 * @Description: Grafische Oberfläche
 */
 """

import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic
import types
import os
import numpy as np

# Unterprogramme
import importPictures as imP

#from Mainwindow import MainWindow



#### globale Variablen ####
aktuellerTab = 0    # Zustand des Tabs der GUI
anzahlBilder = 0    # Anzahl der importierten Bilder für die Zeilenanzahl der Tabelle


#### UI Vorraussetzungen ####
app = widgets.QApplication(sys.argv)
mW = uic.loadUi("badPixelMainWindow.ui")        # UI-Fenster MainWindow laden
eS = uic.loadUi("einstellungenSuchen.ui")
eK = uic.loadUi("einstellungenKorrigieren.ui")
def msgButtonClick():
    print("message")

msgBox = widgets.QMessageBox()  # Die Message Box


#### UI Aktionen Funktionen #### 
### Allgemein
def startClicked():
    print("startClicked")   # debug
    
def mainBackClicked():
    global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
    if aktuellerTab > 0:
        aktuellerTab = aktuellerTab - 1
    mW.tabWidget.setCurrentIndex(aktuellerTab)
    if aktuellerTab < 3:
        mW.pushButtonMainForward.setText("Weiter")
    if aktuellerTab <= 0:
        mW.pushButtonMainBack.setVisible(False)
    # print(aktuellerTab)   # debug
def mainForwardClicked():
    global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
    if aktuellerTab < 3:
        aktuellerTab = aktuellerTab + 1 
    mW.tabWidget.setCurrentIndex(aktuellerTab)
    if aktuellerTab >= 3:
        mW.pushButtonMainForward.setText("Start")
        startClicked()
    if aktuellerTab > 0:
        mW.pushButtonMainBack.setVisible(True)
    # print(aktuellerTab)   # debug
def tabChanged():
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
def uiSetup():
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
### Tab Sensor / BPM
def dateiOeffnen():
    # Ordner auswählen: getExistingDirectory(), Datei auswählen: getOpenFileName(), Dateien auswählen: filename = widgets.QFileDialog.getOpenFileNames() [0]      
    # filename = widgets.QFileDialog.getOpenFileNames() [0]      
    filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "UI-Dateien (*.ui)")
    # mW.lineEditBPM.setText(filename)
    print("Ordnerdialog geöffnet", filename)
    

### Tab Bilddaten
def buttonBilddatenDurchsuchen():   # Ordner importieren
    dirname = widgets.QFileDialog.getExistingDirectory(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation))    
    if dirname != "":  # wenn nicht auf abbrechen gedrückt wird
        mW.lineEditBilddatenDurchsuchen.setText(dirname)
        print(os.listdir(dirname))
    else:
        print("Abgebbrochen")
    print("Ordnerdialog Bilddaten geöffnet", dirname)
def buttonBilddatenImportieren():
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
                dateiEndung = os.path.splitext(aktuellesFile) [1]
                if dateiEndung == ".png" or dateiEndung == ".jpg" or dateiEndung == ".jpeg" or dateiEndung == ".tif" or dateiEndung == ".tiff" or dateiEndung == ".his":
                    #anzahlBilderLocal = anzahlBilderLocal + 1
                    imageFiles.append(aktuellesFile)
            anzahlBilder = anzahlBilder + len(imageFiles)
            mW.tableWidgetBilddaten.setRowCount(anzahlBilder) # Soviele Zeilen in der Tabelle aktivieren, wie es Bilder gibt.
            for index in range(len(imageFiles)):  # Alle importieren Bilder durchgehen
                mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,0, widgets.QTableWidgetItem(imageFiles[index])) # Den Dateinamen aller markierten Bilder in die erste Spalte schreiben
                print(dirname + "/" + imageFiles[index])
                rows, cols, anzahlHisBilder = imP.getAufloesungUndAnzahl(dirname + "/" + imageFiles[index])
                mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,1, widgets.QTableWidgetItem( str(rows) + " x " + str(cols) ) )# Die Auflösung aller markierten Bilder in die erste Spalte schreiben
                mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,2, widgets.QTableWidgetItem( str( int(anzahlHisBilder)) ) )
                mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(imageFiles))) ,3, widgets.QTableWidgetItem( str(dirname + "/" + imageFiles[index]) ) )# Die Pfade aller Bilder in die dritten Spalte schreiben
            #else:
            #print("Abgebbrochen")
            print("Keine Unterordner importieren")

    else:
        msgBox.setIcon(widgets.QMessageBox.Information)
        msgBox.setText("Der eingegebene Pfad ist nicht gültig")
        msgBox.setInformativeText("Der Pfad: \"" + dirname + "\" ist kein gültiger Pfad. Bitte ändern Sie den eingegebenen Pfad.")
        msgBox.setWindowTitle("Kein gültiger Pfad")
        msgBox.setStandardButtons(widgets.QMessageBox.Ok) # | widgets.QMessageBox.Cancel)
        msgBox.buttonClicked.connect(msgButtonClick)
        returnValue = msgBox.exec()
        print(returnValue)
        if returnValue == widgets.QMessageBox.Ok:
            print('OK clicked')
    
        
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
        rows, cols, anzahlHisBilder = imP.getAufloesungUndAnzahl(filename[index])
        # data = imP.importUIFunction(filename[index])
        # print(data, imP.np.shape(data))
        mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,1, widgets.QTableWidgetItem( str(rows) + " x " + str(cols) ) )# Die Auflösung aller markierten Bilder in die erste Spalte schreiben
        mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,2, widgets.QTableWidgetItem( str( int(anzahlHisBilder)) ) )
        mW.tableWidgetBilddaten.setItem( (index + (anzahlBilder - len(filename))) ,3, widgets.QTableWidgetItem( str(filename[index]) ) )# Die Pfade aller Bilder in die dritten Spalte schreiben
    #print(os.path.basename(filename[0]))
    
    #imP.importUIFunction(filename)

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
#### UI Aktionen #### 
### Allgemein
uiSetup()
mW.pushButtonMainBack.clicked.connect(mainBackClicked)
mW.pushButtonMainForward.clicked.connect(mainForwardClicked)
mW.tabWidget.currentChanged.connect(tabChanged)

### Tab Sensor / BPM
mW.pushButtonBPM.clicked.connect(dateiOeffnen)

### Tab Bilddaten
mW.pushButtonBilddatenDurchsuchen.clicked.connect(buttonBilddatenDurchsuchen)
mW.pushButtonBilddatenImportieren.clicked.connect(buttonBilddatenImportieren)
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


#### QT UI anzeigen####
mW.show()
sys.exit(app.exec_()) 

