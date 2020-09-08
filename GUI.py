import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic
import types

# Unterprogramme
#import importPictures as imP

import os   
#from Mainwindow import MainWindow
abc = list()
abc.append(widgets.QTableWidgetItem("ABC Text"))
abc.append(widgets.QTableWidgetItem("ABC Text2"))
abc.append(widgets.QTableWidgetItem("ABC Text3"))
abc.append(widgets.QTableWidgetItem("ABC Text4"))
print("Type ist: ", type(abc))


#### globale Variablen ####
aktuellerTab = 0


#### UI Vorraussetzungen ####
app = widgets.QApplication(sys.argv)
mW = uic.loadUi("badPixelMainWindow.ui")        # UI-Fenster MainWindow laden

#### UI Aktionen Funktionen #### 

### Allgemein
def mainBackClicked():
    global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
    if aktuellerTab > 0:
        aktuellerTab = aktuellerTab - 1
    mW.tabWidget.setCurrentIndex(aktuellerTab)
    if aktuellerTab < 3:
        mW.pushButtonMainForward.setText("Weiter")
    if aktuellerTab <= 0:
        mW.pushButtonMainBack.setVisible(False)
    # print(aktuellerTab)
def mainForwardClicked():
    global aktuellerTab     # ohne diese Zeile kommt darunter eine Fehlermeldung
    if aktuellerTab < 3:
        aktuellerTab = aktuellerTab + 1 
    mW.tabWidget.setCurrentIndex(aktuellerTab)
    if aktuellerTab >= 3:
        mW.pushButtonMainForward.setText("Start")
    if aktuellerTab > 0:
        mW.pushButtonMainBack.setVisible(True)
    # print(aktuellerTab)
def tabChanged():
    global aktuellerTab
    aktuellerTab = mW.tabWidget.currentIndex()
    print(aktuellerTab)
    if aktuellerTab >= 3:
        mW.pushButtonMainForward.setText("Start")
    if aktuellerTab > 0:
        mW.pushButtonMainBack.setVisible(True)
    if aktuellerTab < 3:
        mW.pushButtonMainForward.setText("Weiter")
    if aktuellerTab <= 0:
        mW.pushButtonMainBack.setVisible(False)
def uiSetup():
    # Tab: Algorithmus - GroupBox Pixelfehler finden enablen
    if mW.checkBoxAlgorithmusSuchen.isChecked():
        mW.groupBoxSuchen.setEnabled(True)
        print("Checked")
    else:
        mW.groupBoxSuchen.setEnabled(False)
        print("not Checked")
    # Tab: Algorithmus - GroupBox Pixelfehler korrigieren enablen
    if mW.checkBoxAlgorithmusKorrigieren.isChecked():
        mW.groupBoxKorrigieren.setEnabled(True)
        print("Checked")
    else:
        mW.groupBoxKorrigieren.setEnabled(False)
        print("not Checked")
    # Aktuelle Tab speichern
    global aktuellerTab
    aktuellerTab = mW.tabWidget.currentIndex()

### Tab Sensor / BPM
def dateiOeffnen():
    # Ordner auswählen: getExistingDirectory(), Datei auswählen: getOpenFileName(), Dateien auswählen: filename = widgets.QFileDialog.getOpenFileNames() [0]      
    #filename = widgets.QFileDialog.getOpenFileNames() [0]      
    filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "UI-Dateien (*.ui)")
    #mW.lineEditBPM.setText(filename)
    print("Ordnerdialog geöffnet", filename)
    

### Tab Bilddaten
def buttonBilddatenDurchsuchen():
    # Ordner auswählen: getExistingDirectory(), Datei auswählen: getOpenFileName(), Dateien auswählen: filename = widgets.QFileDialog.getOpenFileNames() [0]      
    filename = widgets.QFileDialog.getExistingDirectory(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation))    
    #filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "UI-Dateien (*.ui)") 
    #mW.lineEditBPM.setText(filename)
    print("Ordnerdialog Bilddaten geöffnet", filename)
    mW.lineEditBildatenDurchsuchen.setText(filename)
def buttonBilddatenAddDurchsuchen():
    filename = widgets.QFileDialog.getOpenFileNames(directory = core.QStandardPaths.writableLocation(core.QStandardPaths.DocumentsLocation), filter = "Bild-Dateien (*.png *.jpg *.jpeg *.tif *.tiff)") [0]
    print(filename)
    print(os.path.basename(filename[0]))
    mW.tableWidgetBilddaten.setItem(0,0, widgets.QTableWidgetItem( os.path.basename(filename[0]) ))
    
    imP.importUIFunction(filename)

    print("buttonBilddatenAddDurchsuchen")
    
def buttonBilddatenDelete():
    print(mW.tableWidgetBilddaten.selectedIndexes())
    print(mW.tableWidgetBilddaten.selectedIndexes())
    print(mW.tableWidgetBilddaten.selectedRanges())
    #mW.tableWidgetBilddaten
    #core.QItemSelectionModel.reset()
    
    
    """
    print(mW.tableWidgetBilddaten())

    widgets.QTableWidget

    mW.tableWidgetBilddaten.setRowCount(2)
    mW.tableWidgetBilddaten.setItem(0,0, widgets.QTableWidgetItem("Yeay"))
    mW.tableWidgetBilddaten.setItem(0,1, widgets.QTableWidgetItem("Yeay2"))
    mW.tableWidgetBilddaten.setItem(1,0, widgets.QTableWidgetItem("Yeay3"))
    mW.tableWidgetBilddaten.setItem(1,1, widgets.QTableWidgetItem("Yeay4"))
    """
    mW.tableWidgetBilddaten.setItem(1,0, abc[0])
    mW.tableWidgetBilddaten.setItem(1,1, abc[1])

    #mW.tableWidgetBilddaten.setItem(1,1, widgets.QTableWidgetItem("Yeay4"))
    print("buttonBilddatenDelete")
    
def buttonBilddatenDeleteAll():
    #mW.tableWidgetBilddaten.clearContents()
    #mW.tableWidgetBilddaten.removeRow()
    mW.tableWidgetBilddaten.setRowCount(0)
    mW.tableWidgetBilddaten.setRowCount(1)
    print("buttonBilddatenDeleteAll")
### Tab Speicherort
def buttonSpeicherortDurchsuchen():
    
    
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

#### UI Aktionen #### 
### Allgemein
uiSetup()
mW.pushButtonMainBack.clicked.connect(mainBackClicked)
mW.pushButtonMainForward.clicked.connect(mainForwardClicked)
mW.tabWidget.currentChanged.connect(tabChanged)

### Tab Sensor / BPM
mW.pushButtonBPM.clicked.connect(dateiOeffnen)

### Tab Bilddaten
mW.pushButtonBildatenDurchsuchen.clicked.connect(buttonBilddatenDurchsuchen)
mW.pushButtonBilddatenAdd.clicked.connect(buttonBilddatenAddDurchsuchen)
mW.pushButtonBilddatenDelete.clicked.connect(buttonBilddatenDelete)
mW.pushButtonBilddatenDeleteAll.clicked.connect(buttonBilddatenDeleteAll)


### Tab Speicherort
mW.pushButtonSpeicherortDurchsuchen.clicked.connect(buttonSpeicherortDurchsuchen)
### Tab Algorithmus
mW.checkBoxAlgorithmusSuchen.stateChanged.connect(suchenEnable)
mW.checkBoxAlgorithmusKorrigieren.stateChanged.connect(korrigierenEnable)


#### QT UI anzeigen####
mW.show()
sys.exit(app.exec_()) 

