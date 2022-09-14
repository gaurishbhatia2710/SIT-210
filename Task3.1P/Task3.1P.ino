/*
  NAME : GAURISH BHATIA
  STUDENT ID: 2110994762
  TASK 3.1P
  REMARKS : THIS IS THE CODE THAT I HAVE IMPLEMENTED  FOR THE TASK 3.1P.



*/



/*
  Sketch generated by the Arduino IoT Cloud Thing "Untitled"
  https://create.arduino.cc/cloud/things/8fbeb1bb-9398-4030-aacb-bac19b96afbc

  Arduino IoT Cloud Variables description

  The following variables are automatically generated and updated when changes are made to the Thing

  bool lED;

  Variables which are marked as READ/WRITE in the Cloud Thing will also have functions
  which are called when their values are changed from the Dashboard.
  These functions are generated with the Thing and added at the end of this sketch.
*/

#include "thingProperties.h"
#include <DHT.h>// including the libraries  for using the DHT sensor.
#include <DHT_U.h>

#define DHTPIN 11     // defining the pin we will be connecting the sensor onto the board.
#define DHTTYPE DHT11   // defining the type of the sensor.
DHT dht(DHTPIN, DHTTYPE);// declaring the DHT sensor with the type and the pin.

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);// starting the serial communication with 9600 baud rate.
  pinMode(LED_BUILTIN, OUTPUT); // declaring the interface for the built in LED.
  dht.begin();// beginning the communication with the DHT sensor.
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500);

  // Defined in thingProperties.h
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  /*
     The following function allows you to obtain more information
     related to the state of network and IoT Cloud connection and errors
     the higher number the more granular information you’ll get.
     The default is 0 (only errors).
     Maximum is 4
  */
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
  temp = dht.readTemperature();

  delay(1000);



}



/*
  Since LED is READ_WRITE variable, onLEDChange() is
  executed every time a new value is received from IoT Cloud.
*/
void onLEDChange()  {
  // Add your code here to act upon LED change
  digitalWrite(LED_BUILTIN, lED);
}