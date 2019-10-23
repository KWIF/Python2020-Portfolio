import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h=0
m=0
s=0
t="am"

def get_alarm(*args):
    global h
    h=input("What Hour")
    global m
    m=input("What Minute")
    global s
    s=input("What Second")
    global t
    t=input("Am or Pm"),upper()
    
def current_time():
    
    totalSeconds= calendar.timegm(time.gmtime())
    currentSeconds= totalSeconds%60
    if currentSeconds < 10:
        currentSeconds = "0"+str(currentSeconds)
    
    totalMin= totalSeconds//60
    currentMin=totalMin%60
    if currentMin < 10:
        currentMin = "0"+str(currentMin)
    
    totalHours=totalMin//60
    currentHour= totalHours%24-6

    am_pm = ""
    if currentHour> 12:
        am_pm= "PM"
    if currentHour==0:
        currentHour=currentHour=12
    else:
        am_pm="AM"
        if currentHour==0:
             currentHour=currentHour=12
    a=str(h)+":"+str(m)+":"+str(s)+t

    timex=str(currentHour)+":"+str(currentMin)+":"+str(currentSeconds)+" "+am_pm
    if timex == a:
        beep()
    return timex

def quit(*args):
    root.destroy()

    
def beep():
    winsound.Beep(2000, 5000)

def show_Time():
    global h
    global m
    global s
    global t
    time=current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_Time)
    

root=Tk()

#Set Window Size
root.geometry("500x200")
root.configure(background='teal')



fnt=font.Font(family='Merriweather', size=60, weight='bold')
txt = StringVar()
#Display Title and setup the color
root.after(1000, show_Time)
lbl=ttk.Label(root, textvariable=txt,  font=fnt, foreground="Gold", background="teal")
#Center of screeb
lbl.place(relx=0.5, rely=0.5, anchor= CENTER)

#StartLoop
root.mainloop()
