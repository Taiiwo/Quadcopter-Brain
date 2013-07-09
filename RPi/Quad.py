import RPi.GPIO as GPIO
import time
print "Initialising Pins..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT) #NE
GPIO.setup(5, GPIO.OUT) #NW
GPIO.setup(7, GPIO.OUT) #SW
GPIO.setup(8, GPIO.OUT) #SE
NE = GPIO.PWM(3,100)
NW = GPIO.PWM(5,100)
SE = GPIO.PWM(7,100)
SW = GPIO.PWM(8,100)
motors = (NE, NW, SW, SE)
for i in motors:
	i.start(0.0)
print "Defining command modules..."
def motor(num,motor): #set the thrust of individual motor
	motor.ChangeDutyCycle(num)
def lift(num): # set the thrust of all of the motors
	for i in motors:
		i.changeDutyCycle(num)
def steady():
	#where x and y are readings from the acceleromiter / gyro between -10 and 10
	if y > 0 and x < 0:
		gy =  ((x * -1) + y) / 2
		motor(gy*10,NE)

        if y > 0 and x > 0:
                gy =  (y + x) / 2
                motor(gy*10,NW)

	if y < 0 and x > 0:
                gy =  ((y * -1) + x) / 2
                motor(gy*10,SW)

        if y < 0 and x < 0:
                gy =  ((x * -1) + (y * -1)) / 2
                motor(gy*10,SE)


while l :
	command = str(raw_input("TaiiwoCopter_v1.0 $")
	
	if command[:6] == "motor ":
		motor = command[7:8]
		num = int(command[9:])
		motor(num,motor)
		
	if command[:5] == "lift ":
		num = command[6:]
		lift(num)
