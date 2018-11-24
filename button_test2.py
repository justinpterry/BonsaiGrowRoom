"""button pressing test.  when pressed should turn on water pump outlet (GPIO23)
for 10 sec then turn off.  button connected to GPIO22
"""

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO22
GPIO.setup(23, GPIO.OUT) # duo outlet water pump

try:
    while True:
         button_state = GPIO.input(22)
         if button_state == False:
             GPIO.output(23, True)
         else:
             GPIO.output(23, False)
except:
    GPIO.cleanup()
