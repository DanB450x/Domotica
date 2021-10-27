import RPi.GPIO as GPIO

import time


GPIO.setwarnings(False)


ledpin = 13

GPIO.setmode(GPIO.BOARD)


GPIO.setup(ledpin, GPIO.OUT)

GPIO.output(ledpin, GPIO.HIGH)


GPIO.cleanup()
