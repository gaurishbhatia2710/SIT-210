/*
Name : Gaurish Bhatia
Student ID : 2110994762
Task 4.2 HD
Remarks : this is the code for the task 4.2HD, which will create a web page using HTML and blink the LED.

*/

#include <SPI.h>
#include <WiFiNINA.h>
#include "arduino_secrets.h"// sensitive data such as ssid and password
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;        // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                // your network key index number (needed only for WEP)

int led1 =  7;// red led at pin 7
int led2 =  8;// blue led at pin 8
int led3 =  6;// green Led at pin 9

// initialising the states as off.
String led1_state = "off";
String led2_state = "off";
String led3_state = "off";

int status = WL_IDLE_STATUS;
WiFiServer server(80);

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.println("Access Point Web Server");

  pinMode(led1, OUTPUT);      // set the LED pin mode
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // by default the local IP address will be 192.168.4.1
  // you can override it with the following:
  WiFi.config(IPAddress(10, 0, 0, 1));

  // print the network name (SSID);
  Serial.print("Creating access point named: ");
  Serial.println(ssid);

  // Create open network. Change this line if you want to create an WEP network:
  status = WiFi.beginAP(ssid, pass);
  if (status != WL_AP_LISTENING) {
    Serial.println("Creating access point failed");
    // don't continue
    while (true);
  }

  // wait 10 seconds for connection:
  delay(10000);

  // start the web server on port 80
  server.begin();

  // you're connected now, so print out the status
  printWiFiStatus();
}


void loop() {
  // compare the previous status to the current status
  if (status != WiFi.status()) {
    // it has changed update the variable
    status = WiFi.status();

    if (status == WL_AP_CONNECTED) {
      // a device has connected to the AP
      Serial.println("Device connected to AP");
    } else {
      // a device has disconnected from the AP, and we are back in listening mode
      Serial.println("Device disconnected from AP");
    }
  }

  WiFiClient client = server.available();   // listen for incoming clients

  if (client) {                             // if you get a client,
    Serial.println("new client");           // print a message out the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected
      delayMicroseconds(10);                // This is required for the Arduino Nano RP2040 Connect - otherwise it will loop so fast that SPI will never be served.
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out to the serial monitor
        if (c == '\n') {                    // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            // following is the html code for web page.
            client.println("<!DOCTYPE html><html>");
            client.println("<head><style>.button{border: none; color: white;padding: 16px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px; margin: 4px 2px;transition-duration: 0.4s;cursor: pointer;}");
            client.println(".button1 { background-color: white; color: black;  border: 2px solid #4CAF50;}");
            client.println(".button1:hover { background-color: #4CAF50;color: white;}");
            client.println(".button3 {background-color: white;color: black;border: 2px solid #008cba;}");
            client.println(".button3:hover {background-color: #008cba;color: white;}");
            
            client.println(".button2 {background-color: white;color: black;border: 2px solid #f44336;}");
            client.println(".button2:hover {background-color: #f44336;color: white;}");
            
            client.println("</style>");
            client.println("<title>Traffic Control System</title>");
            client.println("</head>");
            client.println("<body style=\"text-align: center; font - size: large\">");
            client.println("<h1 style=\"background-color: #01d5ff\">Welcome To light Control System</h1>");
            client.println("<h2>select to turn on/off the light :</h2>");



            




            client.println("<p><a href=\"/8H\"><button class=\"button button3\">Blue Light </button></a></p>");// button for turning on
            client.print("Click <a href=\"/8L\">here</a> turn the blue LED off");// link for turning off.



            client.println("<p><a href=\"/6H\"><button class=\"button button1\">Green Light </button></a></p>");
            client.print("Click <a href=\"/6L\">here</a> turn the green LED off");

            client.println("<p><a href=\"/7H\"><button class=\"button button2\">Red Light </button></a></p>");
            client.print("Click <a href=\"/7L\">here</a> turn the Red LED off");





            client.println("</body>");
            client.println("</html>");







            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:
            break;
          }
          else {      // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        }
        else if (c != '\r') {    // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }

        // Check to see if the client request was "GET /H" or "GET /L":
        light_status(currentLine);

      }
    }
    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }
}

void light_status(String sample)
{
  if (sample.endsWith("GET /7H")) {
    digitalWrite(led1, HIGH);               // GET /H turns the LED on
    led1_state = "on";
  }
  else if (sample.endsWith("GET /7L")) {
    digitalWrite(led1, LOW);                // GET /L turns the LED off
    led1_state = "off";
  }
  else  if (sample.endsWith("GET /8H")) {
    digitalWrite(led2, HIGH);               // GET /H turns the LED on
    led2_state = "on";
  }
  else if (sample.endsWith("GET /8L")) {
    digitalWrite(led2, LOW);                // GET /L turns the LED off
    led2_state = "off";
  }
  else if (sample.endsWith("GET /6H")) {
    digitalWrite(led3, HIGH);               // GET /H turns the LED on
    led3_state = "on";
  }
  else if (sample.endsWith("GET /6L")) {
    digitalWrite(led3, LOW);                // GET /L turns the LED off
    led3_state = "off";
  }
}

void printWiFiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print where to go in a browser:
  Serial.print("To see this page in action, open a browser to http://");
  Serial.println(ip);

}
