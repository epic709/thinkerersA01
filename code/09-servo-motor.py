import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 100)
pwm.start(5)

try:

	while True:

		angle = int(raw_input("Enter angle between 0 and 180 degrees e.g. 45, 90, 135: "))

		print("Press CTRL-C if it sounds very weird...")
		
		if angle >= 0 and angle <= 180:
			duty = float(angle) / 10.0 + 2.5
			pwm.ChangeDutyCycle(duty)
			time.sleep(2)
		else:
			print("Angle error!")

except KeyboardInterrupt:
	pwm.stop()

	GPIO.cleanup