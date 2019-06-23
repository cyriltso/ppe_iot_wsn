#!/usr/bin/python

# Open a file
fo = open("Temperature Xbee logs.csv", "r+")
print ("Name of the file: ", fo.name)

i = 1

for line in fo.readlines():
    if i % 2 != 0 :
        print(line)
    elif i % 2 == 0 :
        print(line)
    i += 1;


# Close opend file
fo.close()

