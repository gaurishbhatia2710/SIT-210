#Name : Gaurish Bhatia
#Stuent ID : 2110994762
#Remarks: This is the code that I have written for the task 5.2C

# including all the required libraries for making a GUI.
from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)# using the BCM interface for accessing the GPIO pins

red=LED(14)# defining the RED LED as 14 GPIO pin.
green=LED(10)#defining the green LED as GPIO pin 10.
blue=LED(12)#defining the blue LED as GPIO pin 12.


win=Tk()# initialising the GUI.
win.title("GUI FOR PI BY GAURISH")#giving the heading of the GUI.

Fontt=tkinter.font.Font(family='arial', size=15, weight="bold")#defining a single font type for all the buttons on the GUI.

def redToggle():#function for toggling the RED LED button
    if red.is_lit:
        red.off()# turning the red LED off.
        red_led_button["text"]="TURN RED LED ON"
    else:
        red.on()#turning the red LED on and turning all the other LEDs as off.
        green.off()
        blue.off()
        red_led_button["text"]="TURN RED LED OFF"

# similarly defining the functions for the other two buttons.
def greenToggle():
    if green.is_lit:
        green.off()
        green_led_button["text"]="TURN GREEN LED ON"
    else:
        green.on()
        blue.off()
        red.off()
        green_led_button["text"]="TURN GREEN LED OFF"

def blueToggle():
    if blue.is_lit:
        blue.off()
        blue_led_button["text"]="TURN BLUE LED ON"
    else:
        blue.on()
        green.off()
        red.off()
        blue_led_button["text"]="TURN BLUE LED OFF"
        

        
#function defined to free up the memory and closing the window.
def close_window():
    RPi.GPIO.cleanup()
    win.destroy()
        

#initialising and creating the buttons.
red_led_button=Button(win,text='TURN RED LED ON',font=Fontt,command=redToggle,bg='red', height=2, width=30)
red_led_button.grid(row=0,column=1)

green_led_button=Button(win,text='TURN GREEN LED ON',font=Fontt,command=greenToggle,bg='green',height=2,width=30)
green_led_button.grid(row=0,column=2)

blue_led_button=Button(win,text='TURN BLUE LED ON',font=Fontt,command=blueToggle,bg='blue',height=2,width=30)
blue_led_button.grid(row=0,column=3)

closeButton=Button(win, text='CLOSE GUI',font=Fontt,command=close_window,bg='bisque',height=2,width=10)
closeButton.grid(row=1,column=2)

#calling the close window function and free up the memory.
win.protocol("WM_DELETE_WINDOW",close_window)

# calling the loop function for displaying the GUi forever till it is closed.
win.mainloop()



