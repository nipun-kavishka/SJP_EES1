import RPi.GPIO as GPIO
import servo
import time
import controller
import statusLED
import muscle
import gyro

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# variables
mode = 1

# declare constatnts
CONST_ACTIVATION_LEVEL = 680
CONST_RELEASING_LEVEL = 120

# function declaration
def initilizeDevice():
  print("\n")
  print("**Application Started**")
  #turn status led on
  statusLED.applicationStarted()

def shoutdownDevice():
  print("\n")
  print("**Application Closed**")
  #turn status led onf
  statusLED.applicationTerminated()

def activeMovement():
  global mode
  mode = 1
  print("Movement -> activated")

def deactiveMovement():
  global mode
  mode = 0
  print("Movement -> deactivated")

def checkFunctionKey():
  if controller.readHomeButton():
    if mode == 0:
      activeMovement()
      time.sleep(0.8)
    else:
      deactiveMovement()
      time.sleep(0.8)

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

try:
  # initilize device
  initilizeDevice()

  while True:
    checkFunctionKey()
    
    if mode == 0:
     statusLED.standby()
    elif mode == 1:
     statusLED.applicationStarted()
     value = muscle.readSensor()
     print(str(value) + "\t")
#     time.sleep(0.8)

    #using linear interpolation formula to map
    maped2 = map(value,0,500,0,180)
    print(str(value) + "\t")
    print(maped2)
    servo.rotateServo1(maped2)
    servo.rotateServo2(180 - maped2)
    time.sleep(1.3)

    #**********use mode3 with gyro sensor conduct for exercises for patients
    #**********still developing  the mobile app

    #servo.grab()
    #time.sleep(5)
    #servo.release()
    #time.sleep(5)
    #servo.setToZero()
except KeyboardInterrupt:
  servo.stopServo()
  shoutdownDevice()
  GPIO.cleanup()