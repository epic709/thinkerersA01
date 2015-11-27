import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_PIN = 24

GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.HIGH)

while True:
  value = raw_input("Turn LED on/off? ")
  if value == "on":
    GPIO.output(LED_PIN, GPIO.HIGH)
  elif value == "off":
    GPIO.output(LED_PIN, GPIO.LOW)
  else:
    break

GPIO.cleanup()

