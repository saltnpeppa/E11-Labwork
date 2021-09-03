import serial
import time
import math

port = serial.Serial("/dev/serial0", baudrate = 9600,timeout = 1.5)

text = port.read(32)

f = lambda x: x * 1.8 + 32

data = []

data1 = int.from_bytes(text[4:6], byteorder = "big")
data2 = int.from_bytes(text[6:8], byteorder = "big")
data3 = int.from_bytes(text[8:10], byteorder = "big")



runtime = 10
start_time = time.time()

while runtime > 0: # Iterate for ten seconds, adding data to the data array each time with values for temperature and current time
	curr_time = time.time() - start_time
	measurement1 = int.from_bytes(text[4:6], byteorder = "big")
	measurement2 = int.from_bytes(text[6:8], byteorder = "big")
	measurement3 = int.from_bytes(text[8:10], byteorder = "big")
	
	time.sleep(1)
	runtime -= 1
	data.append([(measurement1, math.floor(curr_time)), (measurement2, math.floor(curr_time)), (measurement3, math.floor(curr_time))])

myFile = open("air_data.txt", "w")

print(data)

for e in data: # Write data to the data file
	myFile.write(str(e[0][0]) + " ug / m3" + ", " + str(e[0][1]) + " seconds" + "\n")
