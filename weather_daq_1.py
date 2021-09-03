#from Adafruit_BME280 import *
#import time
import math
import csv
import board
import time
from adafruit_bme280 import basic as adafruit_bme280

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()   # uses board.SCL and board.SDA
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)

data = []

f = lambda x: x * 1.8 + 32 # Convert C to F

runtime = 10
start_time = time.time()

while runtime > 0: # Iterate for ten seconds, adding data to the data array each time with values for temperature and current time
	curr_time = time.time() - start_time
	temp = f(sensor.temperature)
	print(temp)
	time.sleep(1)
	runtime -= 1
	data.append((round(temp, 3), math.floor(curr_time)))

myFile = open("data.txt", "w")
for e in data: # Write data to the data file
	myFile.write(str(e[0]) + " F" + ", " + str(e[1]) + " seconds" + "\n")
	
myFile.close()

myFile = open("data.txt", "r+")
	
for i in range(10):
	print(myFile.readline())
