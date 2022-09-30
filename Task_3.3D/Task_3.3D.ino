
/*
  NAME : GAURISH BHATIA
  STUDENT ID : 2110994762
  SIT 210, TASK 3.3D
  REMARKS : THIS IS THE CODE FILE FOR THE TASK 3.3D.

*/

// The required libraries for the MQTT and the Wifi.
#include <ArduinoMqttClient.h>
#if defined(ARDUINO_SAMD_MKRWIFI1010) || defined(ARDUINO_SAMD_NANO_33_IOT) || defined(ARDUINO_AVR_UNO_WIFI_REV2)
#include <WiFiNINA.h>
#elif defined(ARDUINO_SAMD_MKR1000)
#include <WiFi101.h>
#elif defined(ARDUINO_ESP8266_ESP12)
#include <ESP8266WiFi.h>
#endif

#define echoUltra 11 //The echo pin of the HC-SR04 as the digital pin 11
#define triggerUltra 12// The trigger pin of the HC-SR04 as the digital pin 12
#define LEDblink 7// The digital pin 7 as the pin for blinking of the LED.

long duration;// for the duration of the sound wave travel.
int distance;// for measuring the distance.

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = "";        // your network SSID (name)
char pass[] = "";    // your network password (use for WPA, or use as key for WEP)

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "broker.mqttdashboard.com";// The broker used for the MQTT.
int        port     = 1883;// Port to which we will be publishing messages
const char topic[]  = "Sit210/Wave";// Topic to which we need to publish the message.


//set interval for sending messages (milliseconds)
const long interval = 8000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {
  pinMode(LEDblink, OUTPUT);

  pinMode(triggerUltra, OUTPUT); // Setting the trigger pin as an OUTPUT
  pinMode(echoUltra, INPUT); // Setting the echoPin as an INPUT
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();
}

void loop() {
  // call poll() regularly to allow the library to send MQTT keep alive which
  // avoids being disconnected by the broker
  mqttClient.poll();

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time a message was sent
    previousMillis = currentMillis;

    // Clears the trigger pin condition
    digitalWrite(triggerUltra, LOW);// srtting the trigger pin as low.
    delayMicroseconds(2);
    // Setting the trigger pin as HIGH for 10 microseconds.
    digitalWrite(triggerUltra, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerUltra, LOW);// sets the trigger pin as low.

    // Reading the echo pin.
    duration = pulseIn(echoUltra, HIGH);

    // Calculating the distance
    distance = duration * 0.034 / 2;




    if (distance <= 10)
    {

      ledBlink3();// calling the function to blink the LED.


      // printing on the serial monitor.
      Serial.print("Sending message to topic: ");
      Serial.println(topic);
      Serial.print("DISTANCE :");
      Serial.println(distance);

      //Sending the message on the MQTT client.
      mqttClient.beginMessage(topic);
      mqttClient.print("DISTANCE :");
      mqttClient.println(distance);
      mqttClient.endMessage();

      Serial.println();// suitable breaking in between.

    }







  }
}










void ledBlink3()// function to blink the LED 3 times.
{
  digitalWrite(LEDblink, HIGH);// stteing the LED as high.
  delay(300);// delay in between.

  digitalWrite(LEDblink, LOW);// stting the LED as low.
  delay(300);

  // now repeating the above steps for two more times to blink the LED 3 times.
  digitalWrite(LEDblink, HIGH);
  delay(300);
  digitalWrite(LEDblink, LOW);
  delay(300);


  digitalWrite(LEDblink, HIGH);
  delay(300);
  digitalWrite(LEDblink, LOW);
  delay(300);


}
