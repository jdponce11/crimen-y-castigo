from scheduler.scheduler import *
from file_handling.file_handling import *
from datetime import date

today = date.today()

# El primer día del mes, define qué día se va a notificar
if today.day == 1:
    notif_day = define_notif_day(today)
    save_notif_day(notif_day)

# Luego revisa si hoy es el día
notif_day = int(read_notif_day())
if notif_day == today.day:
    notify = True
else: 
    notify = False

# Devuelve true o false si se necesita notificar hoy, o no