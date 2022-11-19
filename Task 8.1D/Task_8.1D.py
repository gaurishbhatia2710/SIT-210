#Name : Gaurish Bhatia
#Student ID: 2110994762
#Remarks: This is the code that I have written for task 8.1D.


#importing the required libraries to control the ambient light sensor.
import smbus 
import time

#setting up the variables for the address and mode for the I2C device.
I2C_DEVICE = 0x23 
one_time_high_res= 0x20

#initialising the variable for device bus.
device_bus = smbus.SMBus(1)



#function to retrieve light values and returning the main value of light intensity.
def retrieve_Light_value(addr=I2C_DEVICE):
    value_of_light = device_bus.read_i2c_block_data(addr, one_time_high_res)
    sample_result = ((value_of_light[1] + (256 * value_of_light[0])) / 1.2)
    return sample_result

#looping infinitely with a delay of 1 second in checking and displaying the brightness.
while True:
    light_value = retrieve_Light_value()
 

    if (light_value < 35):
        print("Too Dark Environment")
        time.sleep(1)
    elif (light_value < 95 and light_value >= 35):
        print("Dark Environment")
        time.sleep(1)
    elif (light_value < 150 and light_value >= 95):
        print("Medium")
        time.sleep(1)
    elif (light_value < 500 and light_value >= 150):
        print("Bright")
        time.sleep(1)
    else:
        print("Too Bright")
        time.sleep(1)

