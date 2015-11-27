import time
import RPi.GPIO as GPIO

LDR_PIN = 23

GPIO.setmode(GPIO.BCM)

def ldr_value():
  value = 0
  GPIO.setup(LDR_PIN, GPIO.OUT)
  GPIO.setup(LDR_PIN, GPIO.LOW)
  time.sleep(0.1)
  start = time.time()
  GPIO.setup(LDR_PIN, GPIO.IN)
  while (GPIO.input(LDR_PIN) == GPIO.LOW):
    value += 1
  finish = time.time()
  duration = 1000 * (finish - start)
  return duration

try:
  while True:
    ldr_val = ldr_value()
    print("LDR: %s" % ldr_val)
    time.sleep(1)
except KeyboardInterrupt:
  pass

GPIO.cleanup()

