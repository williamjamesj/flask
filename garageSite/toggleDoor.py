from settings import DEBUG
from time import sleep

if not DEBUG:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    controlPin = 7
    lowerSensorPin = 12 # The lower sensor on the door, if active, indicates the door is closed.
    higherSensorPin = 16 # The higher sensor on the door, if active, indicates the door is open.
    GPIO.setup(controlPin, GPIO.OUT) #Garage Switch
    GPIO.setup(lowerSensorPin, GPIO.IN) # Lower sensor
    GPIO.setup(higherSensorPin, GPIO.IN) # Upper sensor
else:
    print(" * Garage door DEBUG on. ")
def toggle():
    if DEBUG:
        print("Toggled!")
    else:
        GPIO.output(controlPin, True)
        sleep(1)
        GPIO.output(controlPin, False)
    return "Success"

def getStatus():
    lower = GPIO.input(lowerSensorPin)
    higher = GPIO.input(higherSensorPin)
    if lower == 1:
        return "The Door is Closed"
    elif higher == 1:
        return "The Door is Open"
    else: # If neither of the sensors sense the door, it is neither closed or open.
        return "The Door is in Motion"

def open():
    if getStatus() == "The Door is Closed":
        toggle()
        incrementer = 0
        while getStatus() != "The Door is Open":
            sleep(1) # Wait until the door is opened to send the response.
            incrementer += 1
            if incrementer >= 30:
                return "The Door Failed to Open"
        return "The Door is Open"
    elif getStatus() == "The Door is Open":
        return "The Door is already Open"
    else:
        return "The Door is in Motion"

def close():
    if getStatus() == "The Door is Open":
        toggle()
        incrementer = 0
        while getStatus() != "The Door is Closed":
            sleep(1) # Wait until the door is opened to send the response.
            incrementer += 1
            if incrementer >= 30:
                return "The Door Failed to Close"
        return "The Door is Closed"
    elif getStatus() == "The Door is Closed":
        return "The Door is already Closed"
    else:
        return "The Door is in Motion"