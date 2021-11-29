import RPi.GPIO as GPIO
import time

# declare pins
SERVO_PIN1 = 27
SERVO_PIN2 = 22

# store current angle
cur_angle1 = 0
cur_angle2 = 0

# constants declaration
GRABING_ANGLE = 180
RELEASING_ANGLE = 90

#  setup servo1
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN1, GPIO.OUT)
GPIO.setup(SERVO_PIN2, GPIO.OUT)
servo1 = GPIO.PWM(SERVO_PIN1, 50) # GPIO 27 for PWM with 50Hz
servo2 = GPIO.PWM(SERVO_PIN2, 50) # GPIO 22 for PWM with 50Hz
# Initialization servo
servo1.start(0)
servo2.start(0) 

def rotateM(angle, angle2):
     servo1.ChangeDutyCycle(2+(float(angle)/18))
     servo2.ChangeDutyCycle(2+(float(angle2)/18))

     time.sleep(0.3)
     servo1.ChangeDutyCycle(0)
     servo2.ChangeDutyCycle(0)
#    if angle != cur_angle1:
#     servo1.ChangeDutyCycle(2+(float(angle)/18))
#     setAngle1(angle)
#     time.sleep(0.3)
#     servo1.ChangeDutyCycle(0)
#    else:
#     servo1.ChangeDutyCycle(0)
#    if angle2 != cur_angle2: 
#     servo2.ChangeDutyCycle(2+(float(angle2)/18))
#     setAngle2(angle2)
#     time.sleep(0.3)
#     servo2.ChangeDutyCycle(0)
#    else:
#     servo2.ChangeDutyCycle(0)

def rotateServo1(angle):
    if angle != cur_angle1: 
     servo1.ChangeDutyCycle(2+(float(angle)/18))
     setAngle1(angle)
     time.sleep(0.3)
     servo1.ChangeDutyCycle(0)
    else:
     servo1.ChangeDutyCycle(0)
     
def rotateServo2(angle):
    if angle != cur_angle2: 
     servo2.ChangeDutyCycle(2+(float(angle)/18))
     setAngle2(angle)
     time.sleep(0.3)
     servo2.ChangeDutyCycle(0)
    else:
     servo2.ChangeDutyCycle(0)
    
def release():
    rotateM(90,1)

def grab():
    rotateM(1,90)

def setToZero():
    rotateM(0)

def setAngle1(angle):
    cur_angle1 = angle

def setAngle2(angle):
    cur_angle2 = angle

def stopServo():
    release()
    time.sleep(1)
    servo1.stop()
    servo2.stop()
    
def dumdum():
    for x in range(90, 180):
      print(x)
      servo2.ChangeDutyCycle(2+(float(x)/18))
      time.sleep(0.009)
      #servo2.ChangeDutyCycle(0)
      #time.sleep(0.05)
    servo2.ChangeDutyCycle(0)
  
#def dumdum1():
#    current_duty_cycle = 2+(float(90)/18) 
#    desired_duty_cycle = 2+(float(180)/18)
#    steps = 20.0
#    duty_cycle_delta = (desired_duty_cycle - current_duty_cycle) / steps
#    while (current_duty_cycle != desired_duty_cycle):
#        if (current_duty_cycle > desired_duty_cycle):
#            duty_cycle_delta = -duty_cycle_delta
#        current_duty_cycle = current_duty_cycle + duty_cycle_delta
#        servo2.ChangeDutyCycle (current_duty_cycle)