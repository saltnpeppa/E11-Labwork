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
        e = Eu_152_activity / np.mean(pd.read_csv("Europium_152_Data_2021-11-19_D3S.csv"))
        
        unknown_activities = []
        
        U1_mean = np.mean(pd.read_csv("Unknown_1_Data_2021-11-19_D3S.csv"))
        # U1_data = open(Unknown_1_Data_2021-11-19_D3S.csv)
        # U1_data = np.loadtxt(file_unknown, delimiter=",")
        # reduced_U1_data = np.add.reduce(U1_data, axis=1)
        U1_activity = U1_mean / e
        U1_activity_uncertainty = np.sqrt(U1_activity)
        
        U2_mean = np.mean(pd.read_csv("Unknown_2_Data_2021-11-19_D3S.csv"))
        # U2_data = open(Unknown_2_Data_2021-11-19_D3S.csv)
        # U2_data = np.loadtxt(U2_data, delimiter=",")
        # reduced_U2_data = np.add.reduce(U2_data, axis=1)
        U2_activity = U2_mean / e
        U2_activity_uncertainty = np.sqrt(U2_activity)
        
        U3_mean = np.mean(pd.read_csv("Unknown_3_Data_2021-11-19_D3S.csv"))
        # U3_data = open(Unknown_3_Data_2021-11-19_D3S.csv)
        # U3_data = np.loadtxt(U3_data, delimiter=",")
        # reduced_U3_data = np.add.reduce(U3_data, axis=1)
        U3_activity = U2_mean / e
        U3_activity_uncertainty = np.sqrt(U3_activity)
        
        background_mean = np.mean(pd.read_csv("Background_Data_2021-11-19_D3S.csv"))
        # background_data = open(Background_Data_2021-11-19_D3S.csv)
        # background_data = np.loadtxt(background_data, delimiter=",")
        # reduced_background_data = np.add.reduce(background_data, axis=1)
        Background_activity = background_mean / e
        Background_activity_uncertainty = np.sqrt(Background_activity)
        
        
        
        #data_std = np.std(self.data["Counts"])
        
        
        #data_uncertainty = np.sqrt(data_mean)
        # equation for uncertainty effeciency std_f = f * sqrt((std_a/A)^2 + (std_b/B)^2) Where f = uncertainty, a = CPS, b = Determined Activity
        #print(uncertainty_efficiency, "= uncertainty of the efficiency of the detector")
      
        #Activity = CPS/e use this formula
        # get uncertainties for A
        #creat range for values and the compare to our unknown values and choose closest to the mean
        #print("The activity of the unknown source is:", A)
        
     
        #data_range = 
        
        
        #access uncertainty by doing self.efficiency (cps = A * efficiecny)
        #use A formula
        #
        
        
        
        
        
    
    
    

