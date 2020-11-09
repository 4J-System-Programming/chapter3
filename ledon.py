import time
import RPi.GPIO as GPIO

# GPIO.BCMを指定するとGPIO番号モードで指定
# GPIO.BOARDを指定するとpin番号モードで指定
GPIO.setmode(GPIO.BCM)

# GPIO14を出力に設定
GPIO.setup(14, GPIO.OUT)

# GPIO14にHighを出力
GPIO.output(14, GPIO.HIGH)

# 10msスリープ
time.sleep(10)

GPIO.cleanup()
