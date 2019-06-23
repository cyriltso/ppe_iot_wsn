import serial

from ubidots import ApiClient

print("Sending Data ...")

api = ApiClient(token ='Insert your API token here') #update token

my_temp = api.get_variable('Insert your variable token here') #update variable ID
my_hum = api.get_variable('Insert your variable token here') #update variable ID

ser = serial.Serial('/dev/cu.usbserial-DN04271B', 9600) #update with port for Arduino

while True:
    read_serial = ser.readline()
    tempReading = (float(read_serial)) #convert to float
    humReading = (float(read_serial)) #convert to float
    new_value = my_temp.save_value({'value': tempReading})
    new_value2 = my_hum.save_value({'value': humReading})
    print(read_serial) #prints serial reading to python