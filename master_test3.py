"""humidity and temp control
-3 relay duo outlets
1) heating pad + circulating fan (GPIO27)
2) exhaust fan (GPIO18)
3) humidifier (GPIO17)
DHT22 (GPIO4)
"""

import Adafruit_DHT as dht    # imports Adafruit lib for DHT22
import time                   # imports time lib
import RPi.GPIO as GPIO       # imports GPIO lib
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)    # humidifier
GPIO.setup(18,GPIO.OUT)    # exhaust fan
GPIO.setup(27,GPIO.OUT)    # heating pad
try:
    while 1:                # Loop will run forever
        humi, temp = dht.read_retry(dht.DHT22, 4)  # Reading humidity and temperature
        print 'Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(float(temp),float(humi))
        if humi < 70:    # HUMIDITY LOW LIMIT
            print "humidifier  -on"
            GPIO.output(17,GPIO.HIGH)   # humidifier on
        else:
            print "humidifier -off"    
            GPIO.output(17,GPIO.LOW)    # humidifier off
        if temp < 24:   # TEMPERATURE LOW LIMIT HEATING PAD (75f)
            print "heating pad -on"
            GPIO.output(27,GPIO.HIGH)   # heating pad ON
        else:
            print "heating pad -off"
            GPIO.output(27,GPIO.LOW)# heating pad off
        if temp > 30:   # TEMPERATURE HIGH LIMIT EXHAUST FAN (85f)
            print "exhaust fan -on"
            GPIO.output(18,GPIO.HIGH)   # exhaust fan on
            time.sleep(5)
        else:
            print "exhaust fan -off"
            GPIO.output(18,GPIO.LOW)    # exhaust fan OFF
        time.sleep(5)
# If keyboard Interrupt is pressed
except KeyboardInterrupt:
    pass  			# Go to next line
