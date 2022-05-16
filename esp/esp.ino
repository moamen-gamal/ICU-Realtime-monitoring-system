
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#define NAME "STUDBME1"
#define PASS "BME1Stud"
const byte numChars = 39;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;
bool connected = false;

String payload;  
int httpCode;
HTTPClient http;  //Declare an object of class HTTPClient

String URL ="http://172.28.128.189:5000/sendData";


void setup() {
  Serial.begin(9600);
  WiFi.begin(NAME, PASS);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(100);
  }
  Serial.println("Connected");
  
}

void loop() {
  
 recvFromArduino();
 WiFiClient wifi;
 
 http.begin(wifi,URL); //Specify request destination
 http.addHeader("Content-Type", "application/json");
 int httpResponseCode = http.POST(receivedChars);
 String pay = http.getString();
 Serial.write(pay);
 http.end();   //Close connection
 delay(500);
}

void recvFromArduino() {
  static byte ndx = 0;
  char endMarker = '\n';
  char rc;

  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();
  
    if (rc != endMarker) {
      receivedChars[ndx] = rc;
      ndx++;
      if (ndx >= numChars) {
        ndx = numChars - 1;
      }
    }
    else {
      receivedChars[ndx] = '\0'; // terminate the string
      ndx = 0;
      newData = true;
    }
  }
}
