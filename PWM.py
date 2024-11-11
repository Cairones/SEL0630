from gpiozero import PWMLED
from time import sleep
 
led = PWMLED(5)

while(True):
	b=0
	for b in range(101):
		led.value = b/100
		sleep(0.1)
