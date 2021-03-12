# Bad-Pixel-Korrektur-Programm

Ein plattformunabhängiges Python-Programm mit GUI, welches Bildfehler (Bad-Pixel, Cluster sowie Linienfehler) aus graustufen Bilder bestimmen und korrigieren kann. 

## Getting Started

### Verwendete Bibliotheken
* **NumPy** - [Link](https://github.com/numpy/numpy) (Für die Berechnungen von Matrizen)
* **OpenCV für Python** - [Link](https://pypi.org/project/opencv-python-headless/) (Für den Import, Export und Anzeigen von Bildern)
* **PyQt 5** - [Link](https://pypi.org/project/PyQt5/) (für die grafische Benutzeroberfläche)
* **matplotlib** - [Link](https://matplotlib.org) (Für das Anzeigen von Diagrammen)
* **Fman Build System** - [Link](https://build-system.fman.io) (Für die Erstellung des plattformübergreifenden Installers und der Exe)

### Mit folgenden Befehlen können alle notwendigen Bibliotheken installiert werden
pip install fbs PyQt5==5.9.2

pip install numpy

pip install matplotlib

pip install natsort

Für Windows:
pip install opencv-python 

Für macOS:
pip install opencv-python-headless


### Erstellen einer ausführbaren Datei und eines Installers (platformunabhängig)
Für das Erstellen einer ausführbaren Datei und eines Installers wird das fman-build-system verwendet. Ein einführendes Tutorial ist unter folgender Adresse zu finden: https://github.com/mherrmann/fbs-tutorial
Den Hinweis mit der zu verwendeten Python Version ernst nehmen! 

#### Probleme unter Windows lösen
Die Erstellung der EXE mit dem Befehl "fbs freeze" führt unter Windows zu Fehlern. Folgende Sachen müssen noch getätigt werden, damit es funktioniert:
* Sicherstellen das die Python Version 3.5 oder 3.6 verwendet wird.
* Installation von pypiwin32 mit "pip install pypiwin32"
* Für Windows 10 64 Bit: Fehlende DLL "msvcr100.dll" installieren z.B. von https://www.chip.de/downloads/msvcr100.dll_143094992.html Die Datei unter C:\Windows\System32 einfügen.
* Für Windows 10 32 Bit: Fehlende DLL "msvcr110.dll" installieren z.B. von https://www.chip.de/downloads/msvcr110.dll_143095169.html Die Datei unter C:\Windows\System32 einfügen.
* Für Windows 10 32 Bit: Fehlende DLL "msvcp110.dll" installieren z.B. von https://praxistipps.chip.de/msvcp110-dll-fehlt-was-tun_13586 Die Datei unter C:\Windows\System32 einfügen.
    * https://de.dll-files.com/api-ms-win-crt-multibyte-l1-1-0.dll.html


### GUI bearbeiten
Anstatt das umfangreiche QT Studio zu downloaden, kann auch unter folgender Adresse eine abgespeckte Version runtergeladen werden: https://build-system.fman.io/qt-designer-download

### Lebenstipps
Anscheinend mag der Mac keine prints mit Umlauten, er stürtzt dann einfach ab. (nur in der ausführbaren Datei)

## Versionen

0.1 &nbsp;&nbsp;&nbsp;&nbsp;Erste Version.

## Autoren

* **Julian S.** - [JLS666](https://github.com/JLS666)
* **Andreas B.** - [TrandyAndy](https://github.com/TrandyAndy)

See also the list of [contributors](https://github.com/TrandyAndy/Cor-Count/graphs/contributors) who participated in this project.

