from Adafruit_BME280 import *
import time
import math
import csv

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
data = []

f = lambda x: x * 1.8 + 32

runtime = 10
start_time = time.time()

while runtime > 0:
	curr_time = time.time() - start_time
	temp = f(sensor.read_temperature())
	print(temp)
	time.sleep(1)
	runtime -= 1
	data.append((round(temp, 3), math.floor(curr_time)))

myFile = open("data.csv", "w")
for e in data:
	myFile.write(str(e[0]) + " F" + ", " + str(e[1]) + " seconds" + "\n")
	
myFile.write(9)
