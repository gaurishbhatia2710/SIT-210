#Name : Gaurish Bhatia
#Student ID: 2110994762.
#Remarks : this is the code for the periodic table part.

import json
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import sys
import pyrebase
import time
import datetime
from threading import Thread
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED_1 = 19
LED_2 = 7
LED_3 = 24
LED_4 = 5

GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)
GPIO.setup(LED_4, GPIO.OUT)

# -----------------------
config = {
    "apiKey": "AIzaSyAT15wRlIPqeAtBnYldxOhuj-C2ICgoLEY",
    "authDomain": "myproject-64613.firebaseapp.com",
    "databaseURL": "https://myproject-64613-default-rtdb.firebaseio.com",
    "storageBucket": "http://myproject-64613.appspot.com"
}
firebase = pyrebase.initialize_app(config)
database = firebase.database()
Ele = int(database.child("connect").child("value").get().val())
# ------------------------------------------------------------------------------


def timmer():
    sec = 0*3600+0*60+10
    while sec > 0:
        timer = datetime.timedelta(seconds=sec)
        time.sleep(1)
        sec = sec-1
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    Ele = int(database.child("connect").child("value").get().val())
    print(Ele)


def start1():
    while (True):
        timmer()


new_thread = Thread(target=start1)


def start(value):
    new_thread.start()

    input = value

    if value == '6':
        GPIO.setup(LED_1, GPIO.HIGH)
        GPIO.setup(LED_2, GPIO.LOW)
        GPIO.setup(LED_3, GPIO.LOW)
        GPIO.setup(LED_4, GPIO.LOW)
        GPIO.setup(LED_5, GPIO.LOW)
        GPIO.setup(LED_6, GPIO.LOW)
        GPIO.setup(LED_7, GPIO.LOW)
        GPIO.setup(LED_8, GPIO.LOW)
        GPIO.setup(LED_9, GPIO.LOW)
        GPIO.setup(LED_10, GPIO.LOW)

    elif value == '1':
        GPIO.setup(LED_1, GPIO.LOW)
        GPIO.setup(LED_2, GPIO.HIGH)
        GPIO.setup(LED_3, GPIO.LOW)
        GPIO.setup(LED_4, GPIO.LOW)
        GPIO.setup(LED_5, GPIO.LOW)
        GPIO.setup(LED_6, GPIO.LOW)
        GPIO.setup(LED_7, GPIO.LOW)
        GPIO.setup(LED_8, GPIO.LOW)
        GPIO.setup(LED_9, GPIO.LOW)
        GPIO.setup(LED_10, GPIO.LOW)

    elif value == '25':
        GPIO.setup(LED_1, GPIO.LOW)
        GPIO.setup(LED_2, GPIO.LOW)
        GPIO.setup(LED_3, GPIO.HIGH)
        GPIO.setup(LED_4, GPIO.LOW)
        GPIO.setup(LED_5, GPIO.LOW)
        GPIO.setup(LED_6, GPIO.LOW)
        GPIO.setup(LED_7, GPIO.LOW)
        GPIO.setup(LED_8, GPIO.LOW)
        GPIO.setup(LED_9, GPIO.LOW)
        GPIO.setup(LED_10, GPIO.LOW)

    elif value == '30':
        GPIO.setup(LED_1, GPIO.LOW)
        GPIO.setup(LED_2, GPIO.LOW)
        GPIO.setup(LED_3, GPIO.LOW)
        GPIO.setup(LED_4, GPIO.HIGH)
        GPIO.setup(LED_5, GPIO.LOW)
        GPIO.setup(LED_6, GPIO.LOW)
        GPIO.setup(LED_7, GPIO.LOW)
        GPIO.setup(LED_8, GPIO.LOW)
        GPIO.setup(LED_9, GPIO.LOW)
        GPIO.setup(LED_10, GPIO.LOW)

    else:
        GPIO.setup(LED_1, GPIO.LOW)
        GPIO.setup(LED_2, GPIO.LOW)
        GPIO.setup(LED_3, GPIO.LOW)
        GPIO.setup(LED_4, GPIO.LOW)
        GPIO.setup(LED_5, GPIO.LOW)
        GPIO.setup(LED_6, GPIO.LOW)
        GPIO.setup(LED_7, GPIO.LOW)
        GPIO.setup(LED_8, GPIO.LOW)
        GPIO.setup(LED_9, GPIO.LOW)
        GPIO.setup(LED_10, GPIO.LOW)

    def run(input):
        Dict = {'hydrogen': 1, 'helium': 2}
        type_of = type(input)
        if (type_of == str):
            element = Dict[input.lower()]
            find_element = element
        elif (type_of == int):
            find_element = input
        else:
            print("invalid operation")
            sys.exit()

        global number
        if (find_element >= 1) and (find_element <= 118):
            number = find_element
        else:
            print("Can't perform the function")
            sys.exit()

    run(input)

    f = open('a_main.json')
    data = json.load(f)
    global root

    root = Tk()

    root.title('Application')

    # root.iconbitmap()

    root.geometry("1270x730")
    root.minsize(1270, 730)
    root.maxsize(1270, 730)
    canvas = tk.Canvas(root, height=700, width=700, bg='black').pack()

    frame = tk.Frame(root, bg='white')
    frame.place(width=650, height=650, x=310, y=25)

    Label(frame, text="Periodic Table", font=(
        "Arial", 30), bg='white').pack(pady=10)

    label = Label(text="Hello, Tkinter", fg="black",
                  bg="white", width=10, height=10)

    frame1 = Frame(root)
    frame1.pack()
    frame1.place(anchor='center', x=850, y=210)
    pic = data['elements'][(number)-1]['pic']
    print(pic)
    img = ImageTk.PhotoImage(Image.open(pic))
    label = Label(frame1, image=img)
    label.pack()

    label1 = tk.Label(master=frame, text="Atomic Number = ",
                      bg='white', font=("Arial", 15))
    label1.place(x=8, y=80)
    label1 = tk.Label(master=frame, text=(
        data['elements'][(number)-1]['id']), bg='white', font=("Arial", 15))
    label1.place(x=170, y=80)

    label1 = tk.Label(master=frame, text="Name = ",
                      bg='white', font=("Arial", 15))
    label1.place(x=8, y=110)
    label1 = tk.Label(master=frame, text=(
        data['elements'][(number)-1]['name']), bg='white', font=("Arial", 15))
    label1.place(x=85, y=110)

    label1 = tk.Label(master=frame, text="Phase = ",
                      bg='white', font=("Arial", 15))
    label1.place(x=8, y=140)
    label1 = tk.Label(master=frame, text=(
        data['elements'][(number)-1]['phase']), bg='white', font=("Arial", 15))
    label1.place(x=85, y=140)

    label1 = tk.Label(master=frame, text="Appearance = ",
                      bg='white', font=("Arial", 15))
    label1.place(x=8, y=170)
    label1 = tk.Label(master=frame, text=(
        data['elements'][(number)-1]['appearance']), bg='white', font=("Arial", 15))
    label1.place(x=138, y=170)

    label1 = tk.Label(master=frame, text="Atomic Mass = ",
                      bg='white', font=("Arial", 15))
    label1.place(x=8, y=200)
    label1 = tk.Label(master=frame, text=(
        data['elements'][(number)-1]['atomic_mass']), bg='white', font=("Arial", 15))
    label1.place(x=150, y=200)

    label1 = tk.Label(master=frame, text="Boiling Point = ",
                      bg='white', font=("Arial", 15))
    label1.place(x=8, y=230)
    label1 = tk.Label(master=frame, text=(
        data['elements'][(number)-1]['boil']), bg='white', font=("Arial", 15))
    label1.place(x=145, y=230)


label1 = tk.Label(master=frame, text="Category = ",
                  bg='white', font=("Arial", 15))
label1.place(x=8, y=260)
label1 = tk.Label(master=frame, text=(
    data['elements'][(number)-1]['category']), bg='white', font=("Arial", 15))
label1.place(x=115, y=260)

label1 = tk.Label(master=frame, text="Density = ",
                  bg='white', font=("Arial", 15))
label1.place(x=8, y=290)
label1 = tk.Label(master=frame, text=(
    data['elements'][(number)-1]['density']), bg='white', font=("Arial", 15))
label1.place(x=90, y=290)

label1 = tk.Label(master=frame, text="Molar Heat = ",
                  bg='white', font=("Arial", 15))
label1.place(x=8, y=320)
label1 = tk.Label(master=frame, text=(
    data['elements'][(number)-1]['molar_heat']), bg='white', font=("Arial", 15))
label1.place(x=135, y=320)

label1 = tk.Label(
    master=frame, text="Electronic Configuration = ", bg='white', font=("Arial", 15))
label1.place(x=8, y=350)
label1 = tk.Label(master=frame, text=(data['elements'][(
    number)-1]['electron_configuration_semantic']), bg='white', font=("Arial", 15))
label1.place(x=230, y=350)

global string
string = (data['elements'][(number)-1]['summary'])

btn = Button(frame, text="Sound", command=sound).pack(side='top')

root.mainloop()


def sound():
    global text_speech
    text_speech = pyttsx3.init()
    rate = text_speech.getProperty('rate')
    text_speech.setProperty('rate', 145)
    voices = text_speech.getProperty('voices')
    text_speech.setProperty('voice', voices[1].id)
    text_speech.say(string)
    text_speech.runAndWait()
    text_speech.stop()


def Stop():
    text_speech.stop()
    root.destroy


start(Ele)
