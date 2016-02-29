#! python3.4
from setuptools import setup
import os
import py2exe, sys, os

sys.argv.append('py2exe')

includes = ["sip",
            "PyQt5",
            "PyQt5.QtCore",
            "PyQt5.QtGui"]

datafiles = [("platforms", ["C:\\Python34\\Lib\\site-packages\\PyQt5\\plugins" +
                            "\\platforms\\qwindows.dll"]),
             ("", [r"c:\windows\System32\MSVCP100.dll",
                   r"c:\windows\System32\MSVCR100.dll"])]

setup(
    name='sampleapp',
    version='1.0',
    url='',
    license='',
    windows=[{"script": "startupscript.pyw"}],
    scripts=['startupscript.pyw'],
    data_files=datafiles,
    options={
        "py2exe":{
            "includes": includes,
        }
    }
)
