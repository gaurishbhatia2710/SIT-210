#Name : Gaurish Bhatia
#STUDENT ID : 2110994762.
#Remarks : This is the code that I have written for the implementation of the task 7.3D.


#importing all the required libraries.
import time                             
from time import sleep 

import RPi.GPIO as GPIO   

from gpiozero import DistanceSensor#importing the function for accessing the ultrasonic sensor directly.
from gpiozero import PWMLED#importing the function for accessing the LED Pulse width modulation.

GPIO.setmode(GPIO.BCM) #setting the pinout as BOARD.                 

LED_FOR_DISTANCE = PWMLED(12)#defining the LED for PWM LED.             
Ultrasonic_sensor = DistanceSensor(echo=23, trigger=24) # defining the variable for ultrasonic sensor.  

#running the loop for checking the distance and blinking the LED.
while True:    

    distance_of_object = Ultrasonic_sensor.distance * 100 #retrieving the distance values.  

    print('Distance of the object that is approaching the system = ', distance_of_object) #displaying the distance values.    
    
    # dilfferent if blocks with conditions to check the distance and changing the different values associated with the LED.
    if (distance_of_object > 30):
        LED_FOR_DISTANCE.value = 0
    
    if (distance_of_object < 30 and distance_of_object > 20):
        LED_FOR_DISTANCE.value = 0.25
    
    if (distance_of_object < 20 and distance_of_object > 10):
        LED_FOR_DISTANCE.value = 0.5

    if (distance_of_object < 10 and distance_of_object > 5):
        LED_FOR_DISTANCE.value = 0.75
    
    if (distance_of_object < 5):
        LED_FOR_DISTANCE.value =1

    sleep(1)#setting a suitable delay of 1 second.


LED_FOR_DISTANCE.off()#turning the LED OFF.
