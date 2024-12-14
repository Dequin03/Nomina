Para empaquetar en un ejecutable se requiere pyinstaller:
 pyinstaller --onefile --windowed  --add-data "Formato.xlsx;." --add-data "Formato - copia.xlsx;." --add-data "Formatollenado.xlsx;." Login.py
 --add data se usa para añadir al empaquetado los formatos Excel necesarios para los reportes
 
