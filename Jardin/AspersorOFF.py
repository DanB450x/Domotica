import RPi.GPIO as GPIO
import time

servoPIN = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5)#2.5
try:
  while True:
    p.ChangeDutyCycle(14)
    time.sleep(0)
    p.ChangeDutyCycle(7.5)
    time.sleep(0)
    #break;
except KeyboardInterrupt:
  p.stop()
  #break;
  GPIO.cleanup()

#break;
