import Adafruit_DHT as dht    # imports Adafruit lib for DHT22
import time                   # imports time lib
import schedule               # imports schedule lib
import RPi.GPIO as GPIO       # imports GPIO lib
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)    # humidifier
GPIO.setup(18,GPIO.OUT)    # exhaust fan
GPIO.setup(27,GPIO.OUT)    # heating pad
GPIO.output(18,GPIO.LOW)   # turns off exhaust fan

def exhaust():
    t_end = time.time() + 11
    t_on = time.time() + 10
    while time.time() < t_end:
        if time.time() < t_on:
            GPIO.output(18,GPIO.HIGH)   # exhaust fan on
        else:
            GPIO.output(18,GPIO.LOW)   # exhaust fan off

def humtemp():
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
        
schedule.every(1).hour.do(exhaust) # run exhaust every hour 
schedule.every(5).seconds.do(humtemp)  # run humidity and temp check every 5 sec

while 1:
    schedule.run_pending()
    time.sleep(1)
