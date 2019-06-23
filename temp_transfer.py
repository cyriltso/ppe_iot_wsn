#Program to send the data of the Temperature read to Ubidots Cloud
#Works in the same way than the Humidity one so comments are the same

import serial
from ubidots import ApiClient

print("Sending Data to the Cloud ...")

api  = ApiClient(token = 'A1E-4XbpDAYDVUDPiYaC3I3F6ukMHIrP3r') #update token

my_temp = api.get_variable('5af8656ec03f971772067df5') #update Temperature ID

ser = serial.Serial('/dev/ttyUSB3', 9600) #update with port with Arduino

while True:
	read_serial = ser.readline()
	tempReading = read_serial.decode("utf-8") #read the temperature value
	new_value = my_temp.save_value({'value': tempReading})
	print(read_serial) #prints serial reading to python
