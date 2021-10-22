import Rpi.GPIO as GPIO
import time as time

timestamp = 0
count = 0
r = []


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def my_callback(channel):
  global count
  
  count += 1
  print("fallen")
  
  
GPIO.add_event_detect(17, GPIO.FALLING, callback = my_callback)

while True:
  timestamp += 1
  if timestamp == 10:
    r.append([count, timestamp])
    count = 0
    timestamp = 0
  
  print("looped")
  print(count)
  print(r)
  time.sleep(1)
