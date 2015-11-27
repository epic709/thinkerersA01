import time
import RPi.GPIO as GPIO 

LED_PIN = 17
LED_PIN2 = 27
LED_PIN3 = 22

GPIO.setmode(GPIO.BCM) 

GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(LED_PIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_PIN3, GPIO.OUT, initial=GPIO.LOW)


for i in range(1,20):
  GPIO.output(LED_PIN, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(LED_PIN, GPIO.LOW)
  GPIO.output(LED_PIN2, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(LED_PIN2, GPIO.LOW)
  GPIO.output(LED_PIN3, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(LED_PIN3, GPIO.LOW)


# while True:
#   value = raw_input("Turn blue LED on/off? ")
#   if value == "on":
#     GPIO.output(LED_PIN, GPIO.HIGH)
#   elif value == "off":
#     GPIO.output(LED_PIN, GPIO.LOW)
#   else:
#     break

# while True:  
#   value = raw_input("Turn red LED on/off? ")
#   if value == "on":
#     GPIO.output(LED_PIN2, GPIO.HIGH)
#   elif value == "off":
#     GPIO.output(LED_PIN2, GPIO.LOW)
#   else:
#     break

# while True:
#   value = raw_input("Turn green LED on/off? ")
#   if value == "on":
#     GPIO.output(LED_PIN3, GPIO.HIGH)
#   elif value == "off":
#     GPIO.output(LED_PIN3, GPIO.LOW)
#   else:
#     break


GPIO.cleanup()
