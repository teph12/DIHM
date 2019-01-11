import os
import errno
import picamera
import time
import RPi.GPIO as GPIO

#initialize GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


#initialize parameters

d1 = 30     	#distance between pinhole and camera in mm
d2 = 5.91     	#distance between object and camera in mm
ph = 15       	#pinhole size in microns
wl = 430      	#wavelength in nm
object = 'objectname' #which object

#create the directory and save the parameters

path = "/home/pi/Desktop/" + time.strftime("%y.%m.%d_%H.%M") #the absolute path
filename = path + "/Parameters.txt" #the folder is named after the current date and time. If you take several pictures in one minute, they get overwritten!
if not os.path.exists(os.path.dirname(filename)):
    try: os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:  #write down experimental parameters
    f.write("Object: " + object +"\r")
    f.write("Distance between camera and pinhole: " + str(d1) + " mm\r")
    f.write("Distance between camera and object: " + str(d2) + " mm\r")
    f.write("Pinhole size: " + str(ph) + " microns\r")
    f.write("Wavelength: " + str(wl) + " nm\r")

#turn on LED and capture images
    
GPIO.output(17, GPIO.HIGH)  #turns on LED 

with picamera.PiCamera() as camera:
    camera.resolution = (3280, 2464)    
    camera.iso = 100    #fixed iso
    camera.awb_mode = 'off'     
    camera.awb_gains = (1,3)    #fixed white balance
    camera.start_preview(resolution=(1440, 1080))
    input("Take Picture")
    camera.capture_sequence([path + '/object%s.jpg'%i for i in range(1)])   #one image is captured on pressing enter
    input("Take Background")
    camera.capture_sequence([path + '/background%s.jpg'%i for i in range(1)]) #remove object. On pressing enter again, the background image is captured.
    camera.close()
    

GPIO.output(17, GPIO.LOW)   #turns off LED
