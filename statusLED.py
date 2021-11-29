import RPi.GPIO as GPIO
import time

# declare pins
STATUS_PIN = 23

# setup components
GPIO.setup(STATUS_PIN, GPIO.OUT) # led status led
greenLED = GPIO.PWM(STATUS_PIN,50)
greenLED.start(0)

def applicationStarted():
    #turn status led on
    greenLED.ChangeDutyCycle(10)

def applicationTerminated():
    #turn status led off
    GPIO.output(STATUS_PIN, 0)
    
def standby():
    greenLED.ChangeDutyCycle(10)
    time.sleep(1)
    greenLED.ChangeDutyCycle(0.0)
    time.sleep(1)