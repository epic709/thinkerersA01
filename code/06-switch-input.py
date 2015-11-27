import time
import RPi.GPIO as GPIO

SWITCH_PIN = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH_PIN, GPIO.IN)

def wait_switch_pressed():
  while (GPIO.input(SWITCH_PIN) == GPIO.LOW):
    time.sleep(0.05)

def wait_switch_released():
  while (GPIO.input(SWITCH_PIN) == GPIO.HIGH):
    time.sleep(0.05)

try:
  while True:
    wait_switch_pressed()
    print("Switch pressed")
    wait_switch_released()
    print("Switch released")
except KeyboardInterrupt:
  pass

GPIO.cleanup()

