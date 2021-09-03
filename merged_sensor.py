import serial
import time
import math
import csv
import board
import sys
from adafruit_bme280 import basic as adafruit_bme280
import matplotlib.pyplot as plt
import numpy as np

port = serial.Serial("/dev/serial0", baudrate = 9600,timeout = 1.5)

text = port.read(32)

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()   # uses board.SCL and board.SDA
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)

f = lambda x: x * 1.8 + 32 # Convert C to F

air_data = []
temp_data = []

interval = 10
sleep_time = 1
start_time = time.time()
current_time = start_time


print(sys.argv)
if len(sys.argv) > 1:
	interval = int(sys.argv[1])
	if len(sys.argv) > 2:
		sleep_time = int(sys.argv[2])


while current_time < (start_time + interval): # Iterate for [user input] seconds, adding data to the data array each time with values for air quality and current time
	
	measurement1 = int.from_bytes(text[4:6], byteorder = "big")
	measurement2 = int.from_bytes(text[6:8], byteorder = "big")
	measurement3 = int.from_bytes(text[8:10], byteorder = "big")
	
	temp = f(sensor.temperature)

	time.sleep(sleep_time)
	current_time = time.time()
	real_time = current_time - start_time
	
	temp_data.append((round(temp, 3), math.floor(real_time)))
	air_data.append([(measurement1, math.floor(real_time)), (measurement2, math.floor(real_time)), (measurement3, math.floor(real_time))])
	

myFile = open("merged_data.csv", "w")


for element in temp_data: # Write temperature to the data file
	myFile.write(str(element[0]) + " F" + ", " + str(element[1]) + " seconds" + "\n")
	
myFile.write("\n")
	
for element in air_data: # Write PM1 data to the data file
	myFile.write(str(element[0][0]) + " ug/m3 (PM1)" + ", " + str(element[1][0]) + " ug/m3 (PM2.5)" + ", " + str(element[2][0]) + " ug/m3 (PM10)" + ", " + str(element[0][1]) + " seconds" + "\n")
	
	
print("finished writing")
flat = np.array(temp_data).flatten().reshape(5,2)
print(flat[:,0])
print(flat[:,1])
plt.plot(flat[:,1], flat[:,0])

