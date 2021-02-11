import tkinter as tk
from tkinter import *
import datetime
import time
#import winsound
import pyaudio
import wave


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("the set date is :", date)
        print(now)
        if now == set_alarm_timer:
            print("time to wake up")
            #winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            filename = 'myfile.wav'
            # Set chunk size of 1024 samples per data frame
            chunk = 1024
            # Open the sound file
            wf = wave.open(filename, 'rb')
            # Create an interface to PortAudio
            p = pyaudio.PyAudio()
            # Open a .Stream object to write the WAV file to
            # 'output = True' indicates that the sound will be played rather than recorded
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            # Read data in chunks
            data = wf.readframes(chunk)
            # Play the sound by writing the audio data to the stream
            while data != '':
                stream.write(data)
                data = wf.readframes(chunk)

         # Close and terminate the stream
            stream.close()
            p.terminate()

            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


window = tk.Tk()
window.title("Alarm clock")
window.geometry("800x600")
time_format = Label(window, text="Enter in 24 hours format",
                    fg="red", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(window, text="Hour  Min   Sec", font=60).place(x=110)

setYourAlarm = Label(window, text="when to wake up ", fg="blue",
                     relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(window, textvariable=hour, bg="pink",
                 width=15).place(x=110, y=30)
minTime = Entry(window, textvariable=min, bg="pink",
                width=15).place(x=150, y=30)
secTime = Entry(window, textvariable=sec, bg="pink",
                width=15).place(x=200, y=30)

submit = Button(window, text="set alarm", fg="red", width=10,
                command=actual_time).place(x=110, y=70)
window.mainloop()
