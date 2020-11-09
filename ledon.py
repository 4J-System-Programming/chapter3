import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14, GPIO.HIGH)
time.sleep(10)

GPIO.cleanup()
