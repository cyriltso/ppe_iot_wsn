#Program to send the data of the Humidity read to Ubidots Cloud

#Librairies
import serial #allows to read the data coming from the Arduino
from ubidots import ApiClient #allows to transfer the data to Ubidots Cloud

print("Sending Data to the Cloud ...")

api  = ApiClient(token = 'A1E-4XbpDAYDVUDPiYaC3I3F6ukMHIrP3r') #updating the API token

my_hum = api.get_variable('5af86576c03f97171dc84bb4') #updating the Humidity ID

ser = serial.Serial('/dev/ttyUSB3', 9600) #update with port with Arduino

while True:
	read_serial = ser.readline() #read the data income line by line
	humReading = read_serial.decode("utf-8") #convert from binary to string
	new_value2 = my_hum.save_value({'value': humReading}) #save the value to the cloud
	print(read_serial) #prints serial reading to python
