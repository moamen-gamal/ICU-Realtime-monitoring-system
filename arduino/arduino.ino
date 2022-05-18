#include <ArduinoJson.h>
const byte numChars = 3;
char receivedChars[numChars];  // an array to store the received data
boolean newData = false;
String sensorValues ;
String objectString = " ";
bool senosr1Active = true ;
bool senosr2Active = true ;
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  digitalWrite(LED_BUILTIN, LOW);
  
  recvFromEsp();
 
  collectSensorData();

  Serial.println(receivedChars);
  if(receivedChars== '1')
    digitalWrite(LED_BUILTIN, HIGH);
  delay(100);

}
void collectSensorData() {
  const size_t CAPACITY = JSON_OBJECT_SIZE(3);
  StaticJsonDocument<CAPACITY> doc;
  // create an object
  JsonObject object = doc.to<JsonObject>();
  object["ID"] = 0;
  int randint = 10;
  if (senosr1Active) {
    object["TEMP"] = randint;
  }
  if (senosr2Active) {
    object["LDR"] = randint;
  }
  sensorValues = " " ;
  serializeJson(doc, sensorValues);
  Serial.println(sensorValues);
}
void recvFromEsp() {
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
