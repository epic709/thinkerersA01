import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 18
LDR_PIN = ?? #hint: check the wiring diagram!

def motorSetup():
  # what is the code needed to set up the motor?

def motorMoveForward:
  # how do we move the motor forward?
  time.sleep(2)

def motorMoveBackward:
  # how do we move the motor backward?
  time.sleep(2)

def ldr_value():
  # reuse the code from earlier exercise!

lightLevel = # what LDR value do you want to use to represent neutral light?

try:
  while True:
    ldr_val = ldr_value()
    print("LDR: %s" % ldr_val)
    if ldr_val < lightLevel - 1:
      motorMoveBackward()
      print("It\'s getting dark, retreat....")
    elif ldr_val > lightLevel + 1:
      motorMoveForward()
      print("It\'s bright outside, let\'s roll!")
    else:
      print("Just right, I\'m not going anywhere....")
    
except KeyboardInterrupt:
  pass

GPIO.cleanup()

