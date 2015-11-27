import time
import RPi.GPIO as GPIO

RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)

pattern = ["R", "Y", "G", "RY", "YG", "RG", "RYG"]

for colours in pattern:
  if "R" in colours:
    GPIO.output(RED_PIN, GPIO.HIGH)
  else:
    GPIO.output(RED_PIN, GPIO.LOW)
  if "Y" in colours:
    GPIO.output(YELLOW_PIN, GPIO.HIGH)
  else:
    GPIO.output(YELLOW_PIN, GPIO.LOW)
  if "G" in colours:
    GPIO.output(GREEN_PIN, GPIO.HIGH)
  else:
    GPIO.output(GREEN_PIN, GPIO.LOW)
  time.sleep(1)

GPIO.cleanup()

