import tkinter as tk
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("the set date is :" date)
        print(now)
        if now == set_alarm_timer:
        print("time to wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break


window = tk.Tk()

window.geometry("800x600")


window.mainloop()
