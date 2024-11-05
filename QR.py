import qrcode
import socket
from datetime import datetime, timedelta,date
host=socket.gethostname()
Fecha= date.today()
img = qrcode.make(f"Expedido por {host}, el dia {Fecha}")
f = open("output.png", "wb")
img.save(f)
f.close()