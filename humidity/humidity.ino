//Libraries
#include <DHT.h> 
#include <SoftwareSerial.h>

//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
SoftwareSerial XBee(2, 3);

int chk;
float hum; //Stores humidity value

void setup()
{
  XBee.begin(9600); //setting the baud rate
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
    delay(2000);
    //Read data and store it to variables hum
    hum = dht.readHumidity();
       
    //Print temp and humidity values to serial monitor
    Serial.println(hum);
    delay(2000); //Delay 2 sec.

    XBee.println(hum);
    delay(2000); //Delay 2 sec.   
}
