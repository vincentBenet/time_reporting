# import os
# import sys
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# os.system("cxfreeze -c time_reporting.py")

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "os", 
        "tkinter"
    ], "excludes": [
        ""
    ]
}

setup(
    name="Time Reporting",
    version="0.1",
    description="Application for time keeping",
    options = {"build_exe": build_exe_options},
    executables=[Executable(
        "time_reporting.py", 
        base = "Win32GUI"
    )],
)