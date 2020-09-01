import sys
from cx_Freeze import setup, Executable

#//CMD cd "Ordner" + python setup.py build

""" #build_exe_options={}
base = None
if sys.platform == "win32":
    base="Win32GUI"

setup(
    name = "Andys",
    version="0",
    description = "Mein erstes Programm!",
    #options = {"build_exe": build_exe_options},
    executables = [Executable("programm.py", base=base)]
) """

setup(
    name = "Bad Pixel Killer",
    version="0",
    description = "Bad Pixel Eliminator der HS-Karlsruhe",
    executables = [Executable("programm.py")]
     )

