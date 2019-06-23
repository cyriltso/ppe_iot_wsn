# IoT & Big Data project : Wireless Sensor Network

## Introduction

The goal of the project was to collect temperature and humidity data from specific sensors in order to wirelessly transfer them to a computer (i.e without connecting the microprocessor to the machine), then to store this data to an IoT Cloud Platform in order to be able to follow the evolution of these data over time (with plots and charts for example).

## Hardware tools

-  Arduino UNO
-  Raspberry Pi
-  Ultrasonic Sensor : HC-SR04
-  Temperature + Humidity Sensors all in one : DHT11
-  Xbees modules (radio connection)

## Software tools

-  Python, C++ as programming languages
-  PyCharm (Python IDE)
-  Arduino Software 
-  XCTU (setting up the Xbees)
-  Ubidots (IoT Cloud Platform)

## Steps to follow to reproduce the project

1. Plug the sensors on the Arduino
2. Set up the connectivity on the Xbees (as transmittor and receiver) with XCTU
3. Use the Arduino script (in C++) to collect the data from the sensors
4. Use the Python script to store the data locally (in CSV file) and in the cloud with Ubidots (with API key provided by the website)
