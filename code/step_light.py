import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin_coilA1 = 10
pin_coilA2 = 27
pin_coilB1 = 17
pin_coilB2 = 22
LDR_PIN = 23

def motorSetup():
  GPIO.setup(pin_coilA1, GPIO.OUT)
  GPIO.setup(pin_coilA2, GPIO.OUT)
  GPIO.setup(pin_coilB1, GPIO.OUT)
  GPIO.setup(pin_coilB2, GPIO.OUT)

def motorFree():
  motorStep(0, 0, 0, 0)

def motorMove(steps, delay):
  if steps >= 0:
    for i in range(0, steps):
      motorStep(1, 0, 1, 0)
      time.sleep(delay)
      motorStep(0, 1, 1, 0)
      time.sleep(delay)
      motorStep(0, 1, 0, 1)
      time.sleep(delay)
      motorStep(1, 0, 0, 1)
      time.sleep(delay)
  else:
    for i in range(0, -steps):
      motorStep(1, 0, 1, 0)
      time.sleep(delay)
      motorStep(1, 0, 0, 1)
      time.sleep(delay)
      motorStep(0, 1, 0, 1)
      time.sleep(delay)
      motorStep(0, 1, 1, 0)
      time.sleep(delay)

def motorStep(a1, a2, b1, b2):
  GPIO.output(pin_coilA1, a1)
  GPIO.output(pin_coilA2, a2)
  GPIO.output(pin_coilB1, b1)
  GPIO.output(pin_coilB2, b2)

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

lightLevel = float(raw_input("Desired light level: "))

motorSetup()
motorFree()

motorPosition = 64

try:
  while True:
    motorAdjust = 0
    ldr_val = ldr_value()
    print("LDR: %s" % ldr_val)
    if ldr_val < lightLevel - 1:
      if motorPosition < 128:
        motorAdjust = 8
      motorPosition += motorAdjust
      print("Too bright, adjusting motor to %s" % motorPosition)
    elif ldr_val > lightLevel + 1:
      if motorPosition > 0:
        motorAdjust = -8
      motorPosition += motorAdjust
      print("Too dim, adjusting motor to %s" % motorPosition)
    else:
      print("Just right")
    if motorAdjust == 0:
      time.sleep(0.25)
except KeyboardInterrupt:
  pass

GPIO.cleanup()

