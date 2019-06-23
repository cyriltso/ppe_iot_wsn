#include <DHT.h>
#include <SoftwareSerial.h>

//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
SoftwareSerial XBee(2, 3);

int chk;
float temp; //Stores temperature value

void setup()
{
  XBee.begin(9600);
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
    delay(2000);
    //Read data and store it to variables temp
    temp= dht.readTemperature();
       
    //Print temp values to serial monitor
    Serial.println(temp);
    delay(2000); //Delay 2 sec.

    XBee.println(temp);
    delay(2000); //Delay 2 sec.
}
