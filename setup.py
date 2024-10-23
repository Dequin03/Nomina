from distutils.core import setup
import py2exe

setup(console=['#Nomina2.py'],
      options= {"py2exe":{
        "packages":["tkinter","pyodbc","uuid","base64","datetime","openpyxl","pandas","reportlab.lib","socket"]}})