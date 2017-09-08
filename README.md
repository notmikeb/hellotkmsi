# hellotk msi sample

## Intro
Use cx_Freeze to compile python3 scrips
Need add necessary dlls to include files

## Steps

### how to build
Use build.bat to compile
```
>build.bat
```

### environment
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32

### requirements cx_Freeze
python -m pip install cx_Freeze --upgrade

### origin sample
a sample msi to use ekey to capture print-screen key 

https://github.com/ffreitasalves/boneca

### bug solver: KeyError: 'TCL_Library' when I use cx_Freeze
```
set TCL_LIBRARY=C:\Program Files\Python35-32\tcl\tcl8.6
set TK_LIBRARY=C:\Program Files\Python35-32\tcl\tk8.6
```

https://stackoverflow.com/questions/35533803/keyerror-tcl-library-when-i-use-cx-freeze

### pyqt sample
http://icodding.blogspot.tw/2016/03/python-cxfreeze-pyqt.html