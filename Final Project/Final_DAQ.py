import RPi.GPIO as GPIO
import time as time
import sys
import numpy as np
import math
import statistics
import matplotlib
# %matplotlib inline
import matplotlib.pylot as plt

class Final:

    def __init__(self, efficiency, data, count=0, timestamp=0):
        """This method initializes a class instance.

        Args:
            efficiency (double): Efficiency coefficient of our detector
            timestamp (integer): Sets a relative timestamp of 0 for our data acquisition method
            count (integer): Stores the number of detections we get with our system
            data (array): Stores our data with two columns: counts and timestamp
        """        
        self.efficiency = efficiency
        self.timestamp = timestamp
        self.count = count
        self.data = data

    def acquire_data(self, interval, num_intervals, name):
        """This method acquires data from our system and returns an array of our counts and timestamps.

        Args:
            interval (integer): This is the interval of seconds for which our system will measure counts
            num_intervals (integer): This is the number of time intervals our system will measure for
            name (string): This is the name of the file our system will store the data in

        Returns:
            array: Array of counts and timestamps
        """           

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN)


        def my_callback(channel):
            """This functions increments our count variable by 1 every time a detection is registered with our sensor.

            Args:
                channel (GPIO Channel): Channel that our RPi communicates with (GPIO)
            """            
            self.count += 1
            print("fallen")
            
        
        GPIO.add_event_detect(17, GPIO.FALLING, callback = my_callback)

        myFile2 = open(name + "_" + str(round(time.time()))+".csv", "w")
        myFile2.write("Counts," + " Timestamp" + "\n")

        while self.timestamp <= num_intervals * interval:

            self.timestamp += 1

            if self.timestamp % interval == 0:
                self.data.append([self.count, self.timestamp])
                myFile2.write(str(self.count) + ", " + str(self.timestamp) + "\n")

                count = 0

            self.timestamp = 0
        
            print("looped", count, self.data)
 
            time.sleep(1)

        return self.data


    def parse_data(self):
        Eu_152_activity = 213345.9
        e = Eu_152_activity / np.mean(Europium_152_Data_2021-11-19_D3S.csv)  #need to ask sid how to open this file
        
        unknown_activities
        
        data_mean = np.mean(self.data["Counts"])
        unknown_activity = data_mean / e
        unknown_activity_uncertainty = 
        
        #data_std = np.std(self.data["Counts"])
        
        
        #data_uncertainty = np.sqrt(data_mean)
        # equation for uncertainty effeciency std_f = f * sqrt((std_a/A)^2 + (std_b/B)^2) Where f = uncertainty, a = CPS, b = Determined Activity
        #print(uncertainty_efficiency, "= uncertainty of the efficiency of the detector")
      
        #Activity = CPS/e use this formula
        # get uncertainties for A
        #creat range for values and the compare to our unknown values and choose closest to the mean
        #print("The activity of the unknown source is:", A)
        
        #thorium_mean = 
        #thorium_std = 
        #thorium_activity = 
        #other_source_mean = 
        #other_source_std = 
        #other_source_activity = 
        
        #data_range = 
        
        
        #access uncertainty by doing self.efficiency (cps = A * efficiecny)
        #use A formula
        #
        
        
        
        
        
    
    
    

