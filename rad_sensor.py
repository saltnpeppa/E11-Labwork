import RPi.GPIO as GPIO
import time as time
import sys

timestamp = 0
count = 0
r = []

time.sleep(90) # REMOVE AFTER GOING BACK INSIDE

print(sys.argv)

if len(sys.argv) > 1:
  interval = int(sys.argv[1])
  if len(sys.argv) > 2:
    num_intervals = int(sys.argv[2])
    if len(sys.argv) > 3:
      name = str(sys.argv[3])

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def my_callback(channel):
  global count
  
  count += 1
  print("fallen")
  
  
GPIO.add_event_detect(17, GPIO.FALLING, callback = my_callback)

myFile2 = open(name + "_" + str(round(time.time()))+".csv", "w")
myFile2.write("Counts," + " Timestamp" + "\n")

while timestamp <= num_intervals * interval:
  timestamp += 1
  if timestamp % interval == 0:
    r.append([count, timestamp])
    myFile2.write(str(count) + ", " + str(timestamp) + "\n")
    count = 0
    # timestamp = 0
  
  print("looped")
  print(count)
  print(r)
  time.sleep(1)
  
  
  
  

