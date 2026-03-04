import calendar
import random

def define_notif_day(today):
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    notif_day = random.randint(1, days_in_month)
    return notif_day