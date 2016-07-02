import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
while True:
	
	if GPIO.input(21):
		GPIO.output(3,True)
		GPIO.output(5,True)
	if GPIO.input(23):	
		GPIO.output(3,True)
		GPIO.output(5,True)
		GPIO.output(7,True)
		GPIO.output(11,True)
	if GPIO.input(29):
		GPIO.output(3,True)
		GPIO.output(5,True)
		GPIO.output(7,True)
		GPIO.output(11,True)
		GPIO.output(13,True)
		GPIO.output(15,True)
	if GPIO.input(31):
		GPIO.output(3,True)
		GPIO.output(5,True)
		GPIO.output(7,True)
		GPIO.output(11,True)
		GPIO.output(13,True)
		GPIO.output(15,True)
		GPIO.output(19,True)
	time.sleep (0.5)	
	GPIO.output(3,False)
	GPIO.output(5,False)
	GPIO.output(7,False)
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(15,False)
	GPIO.output(19,False)
	time.sleep(0.5)
