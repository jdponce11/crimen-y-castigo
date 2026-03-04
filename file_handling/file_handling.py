def save_notif_day(notif_date):
    with open("notif_date.txt", "w") as f:
        f.write(str(notif_date))
    return

def read_notif_day():
    with open("notif_date.txt", "r") as f:
        notif_day = f.read()
    return notif_day