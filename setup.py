import esky.bdist_esky
from esky.bdist_esky import Executable as Executable_Esky
from cx_Freeze import setup, Executable

include_files = []

import os
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = r'{}\tcl\tcl8.6'.format(PYTHON_INSTALL_DIR) 
os.environ['TK_LIBRARY'] = r'{}\tcl\tk8.6'.format(PYTHON_INSTALL_DIR)
include_files = [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ]

setup(
    name = 'helloday',
    version = '1.0.0',
    options = {
        'build_exe': {
            'packages': ['os','sys','ctypes','win32con'],
            #'excludes': ['tkinter','tcl','ttk'],
            'include_files': include_files,
            'include_msvcr': True,
        },
        'bdist_esky': {
            'freezer_module': 'cx_freeze',
        }
    },
    data_files = include_files,
    scripts = [
        Executable_Esky(
            "hellotk.py",
            gui_only = True,
            #icon = XPTO #Coloque um icone aqui se quiser ,
            ),
    ],
    executables = [Executable('hellotk.py',base='Win32GUI')]
    )