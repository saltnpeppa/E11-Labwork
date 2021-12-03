import RPi.GPIO as GPIO
import time as time
import sys
import numpy as np
import math
import statistics
import matplotlib
%matplotlib inline
import matplotlib.pylot as plt


class Final:

    timestamp = 0
    count = 0
    r = []
    

    #time.sleep(90) # REMOVE AFTER GOING BACK INSIDE

    def __init__(self, uncertainty):
        pass

    def acquire_data():

        print(sys.argv)

        if len(sys.argv) > 1:
            interval = int(sys.argv[1]) # Seconds between each measurement
        if len(sys.argv) > 2:
            num_intervals = int(sys.argv[2]) # number of intervals measured
            if len(sys.argv) > 3:
                name = str(sys.argv[3])

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN)

        def my_callback(channel):
            
            self.count += 1
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


    def parse_data(self):
        data_mean = np.mean(self.data["Counts"])
        data_std = np.std(self.data["Counts"])
        print(f"The relative uncertainty is: {data_std/data/mean}")
        # equation for uncertainty effeciency std_f = f * sqrt((std_a/A)^2 + (std_b/B)^2) Where f = uncertainty, a = CPS, b = Determined Activity
        #print(uncertainty_efficiency, "= uncertainty of the efficiency of the detector")
        # Activity equation: A = 1 / (std_e/e)^2 + (std_CPS/CPS)^2
        #print("The activity of the unknown source is:", A)
        
        #thorium_mean = 
        #thorium_std = 
        #thorium_activity = 
        #other_source_mean = 
        #other_source_std = 
        #other_source_activity = 
        
        
        
        
        
    
    
    

