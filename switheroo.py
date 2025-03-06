import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RELAY_PIN = 21

GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    
    while True:
        
        GPIO.output(RELAY_PIN, True)
        time.sleep(2)
        
        GPIO.output(RELAY_PIN, False)
        time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()