import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
controlPin = 7
GPIO.setup(controlPin, GPIO.OUT) #Garage Switch (Pin 1 - power, Pin 9 - Gnd)

def toggleDoor():
    GPIO.output(controlPin, True)
    sleep(1)
    GPIO.output(controlPin, False)
    return "Success"