import RPi.GPIO as GPIO     
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(7,GPIO.OUT)      

GPIO.output(7,1)            
time.sleep(.5)               
                             
GPIO.output(7,1)           
time.sleep(.5)

 