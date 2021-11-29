import RPi.GPIO as GPIO
import time

# declare pins
HOME_BUTTON = 24
GPIO.setup(HOME_BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def readHomeButton():
    button_state = GPIO.input(HOME_BUTTON)
    if button_state == 0:
        return True
    else:
        return False