# Name : Gaurish Bhatia
#STUDENT ID : 2110994762
#task 5.3D Morsecode
#Remarks : This is the code that I have written for the task 5.3D.

#importing all the required libraries.
import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
import time
from time import sleep
from gpiozero import LED
 
#setting the mode to use the GPIO pins on the board.
GPIO.setmode(GPIO.BOARD)   

led = 12 #setting the LED as 15th GPIO pin.

GPIO.setup(led,GPIO.OUT)

win = Tk()#initialising the GUI.    
win.title("Blink Morse") #giving the title.   
winFont = tkinter.font.Font(family = 'Century' , size = 14, weight = "bold")# defining a font by using the inbuilt font.

#funcctions for time delay to be used further.
def dash():
    time.sleep(0.75)

def dot():
    time.sleep(0.25)

def delay():
    time.sleep(0.75)

#initialising the dictionary of morsecode.
morse_dictionary = {
      'A': '.-', 
      'B': '-...', 
      'C': '-.-.', 
      'D': '-..', 
      'E': '.', 
      'F': '..-.', 
      'G': '--.', 
      'H': '....', 
      'I': '..', 
      'J': '.---', 
      'K': '-.-', 
      'L': '.-..', 
      'M': '--', 
      'N': '-.', 
      'O': '---', 
      'P': '.--.', 
      'Q': '--.-', 
      'R': '.-.', 
      'S': '...', 
      'T': '-', 
      'U': '..-', 
      'V': '...-', 
      'W': '.--', 
      'X': '-..-', 
      'Y': '-.--', 
      'Z': '--..', 
      '1': '.----', 
      '2': '..---', 
      '3': '...--', 
      '4': '....-', 
      '5': '.....', 
      '6': '-....', 
      '7': '--...', 
      '8': '---..', 
      '9': '----.', 
      '0': '-----',
      ' ': ' ',
          }

#defining a function for printing the morseocode and blinking the LED.
def blinker():
    input_text = Input_box.get()
    
    converted_string = ""
    for c in input_text:
        converted_string += morse_dictionary[c.upper()]
        converted_string += " "

    morse_text = converted_string
    print(morse_text)
    
    for sample in morse_text:
            for sample_letter in sample:
                GPIO.output(led,True)
                if sample_letter == "-":
                    dash()
                elif sample_letter == ".":
                    dot()
                elif sample_letter == " ":
                    delay()
                    delay()

                GPIO.output(led,False)
                delay()
    GPIO.output(led,False)


#function for closing the GUI and clearing up the memory.
def exit():
    GPIO.output(led,False)
    win.destroy()

#defining the input box for taking the input in form of letters.
Input_box = Entry(win,font=winFont, width=30)
Input_box.grid(row=0,column=1)

#defining the submit button.
Submit_button = Button(win,text='Convert', font=winFont, command=blinker, bg='blue', height=1, width=13)
Submit_button.grid(row=1,column=1)

#defining a button for exit.
exit_button = Button(win, text = 'Exit', font  = winFont, command = exit, bg = 'blue', width = 24)
exit_button.grid(row=2,column=1)

#clearing up the memory if GUI is closed directly.
win.protocol("WM_DELETE_WINDOW", exit)

#looping the GUI till it is closed.
win.mainloop()



