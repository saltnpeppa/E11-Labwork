import serial
import time
import gps

ser = serial.Serial("/dev/ttyUSB0", 9600)
data = ser.read(32)

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


while True:
	try:
		report = session.next()
		latitude = report.lat
		longitude = report.longitude 
		print("latitude: " + str(latitude) + "longitude: " + str(longitude))
		#if report['class'] == 'TPV':
			#if hasattr(report, 'time'):
				#print(report.time)
	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print("terminated")



#while True:
	#print(data)
	#time.sleep(0.5)
