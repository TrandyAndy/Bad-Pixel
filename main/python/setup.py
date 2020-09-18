import sys
from cx_Freeze import setup, Executable

#//CMD cd "Ordner" + python setup.py build
#oder win: python setup.py bdist_msi


build_exe_options={
        "includes": ["badPixelMainWindow.ui"]
    
}
include_package_data=True

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base="Win32GUI"


setup(
    name = "Bad_Pixel_Killer",
    version="0",
    description = "Bad Pixel Eliminator der HS-Karlsruhe",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py")]
     )

