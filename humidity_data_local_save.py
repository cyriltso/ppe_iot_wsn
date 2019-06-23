#Program that allows to save locally the humidity data, here in a csv file

import serial #library that allows to read the data stream from the arduino

serial_port = '/dev/cu.usbmodem1421'; #name of the serial port (its name vary depending on the location of the usb port)
baud_rate = 9600; #we chose to set the baud rate here to 9600
write_to_file_path = "Humidity logs.csv"; #the name and the type of file in which we want to write the data in
output_file = open(write_to_file_path, "w+"); #writing the data
print("Humidity (in %) :")
ser = serial.Serial(serial_port, baud_rate) #reading the data stream
while True: #to allow a permanent stream and not a limited stream
    line = ser.readline(); #reading the data line by line
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    print(line); #print the data
    output_file.write(line); #write the data coming in the file