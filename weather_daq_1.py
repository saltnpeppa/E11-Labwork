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

f = lambda x: x * 1.8 + 32

runtime = 10
start_time = time.time()

while runtime > 0:
	curr_time = time.time() - start_time
	temp = f(sensor.temperature)
	print(temp)
	time.sleep(1)
	runtime -= 1
	data.append((round(temp, 3), math.floor(curr_time)))

myFile = open("data.csv", "w")
for e in data:
	myFile.write(str(e[0]) + " F" + ", " + str(e[1]) + " seconds" + "\n")
	

