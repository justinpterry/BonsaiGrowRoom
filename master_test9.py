import Adafruit_DHT as dht    # imports Adafruit lib for DHT22
import time                   # imports time lib
import schedule               # imports schedule lib
import RPi.GPIO as GPIO       # imports GPIO lib
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)    # humidifier
GPIO.setup(18,GPIO.OUT)    # exhaust fan
GPIO.setup(27,GPIO.OUT)    # heating pad
GPIO.setup(23,GPIO.OUT)    # dehumidifier (IN4)
GPIO.output(18,GPIO.LOW)   # turns off exhaust fan

def exhaust():
    t_end = time.time() + 121    # time just after 2min
    t_on = time.time() + 120     # time in which fan will be on, 2min
    while time.time() < t_end:
        if time.time() < t_on:
            GPIO.output(18,GPIO.HIGH)   # exhaust fan on
        else:
            GPIO.output(18,GPIO.LOW)   # exhaust fan off

def humtemp():
    humi, temp = dht.read_retry(dht.DHT22, 4)  # Reading humidity and temperature
    print 'Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(float(temp),float(humi))

# Humidity target dependent on air temperature.  Sectioned into temp ranges >28, 27-28, 25-27, 23-25, 22-23, <20.
# All low ends in ranges are designated as "greater than OR equal to" so all numbers are covered by if/then statements.

    if temp >= 28:   # hi range for temp settings, want hum 75-80%
        print "HUM GOAL               (75-80%)"
        if humi < 75:
            print "HUM                    -ON"
            GPIO.output(17,GPIO.HIGH)    # humidifier on
        else:
            print "HUM                    -OFF"    
            GPIO.output(17,GPIO.LOW)     # humidifier off
        if humi > 80:
            print "DEHUM                  -ON"
            GPIO.output(23,GPIO.HIGH)    # dehumidifier on
        else:
            print "DEHUM                  -OFF"    
            GPIO.output(23,GPIO.LOW)     # dehumidifier off

    if 27 <= temp < 28:   # want hum 75% (range 72.5-77.5%)
        print "HUM GOAL               (75%)"
        if humi < 72.5:
            print "HUM                    -ON"
            GPIO.output(17,GPIO.HIGH)    # humidifier on
        else:
            print "HUM                    -OFF"    
            GPIO.output(17,GPIO.LOW)     # humidifier off
        if humi > 77.5:
            print "DEHUM                  -ON"
            GPIO.output(23,GPIO.HIGH)    # dehumidifier on
        else:
            print "DEHUM                  -OFF"    
            GPIO.output(23,GPIO.LOW)     # dehumidifier off

    if 25 <= temp < 27:   # want hum 70-75%
        print "HUM GOAL               (70-75%)"
        if humi < 70:
            print "HUM                    -ON"
            GPIO.output(17,GPIO.HIGH)    # humidifier on
        else:
            print "HUM                    -OFF"    
            GPIO.output(17,GPIO.LOW)     # humidifier off
        if humi > 75:
            print "DEHUM                  -ON"
            GPIO.output(23,GPIO.HIGH)    # dehumidifier on
        else:
            print "DEHUM                  -OFF"    
            GPIO.output(23,GPIO.LOW)     # dehumidifier off

    if 23 <= temp < 25:   # want hum 65-70%
        print "HUM GOAL               (65-70%)"
        if humi < 65:
            print "HUM                    -ON"
            GPIO.output(17,GPIO.HIGH)    # humidifier on
        else:
            print "HUM                    -OFF"    
            GPIO.output(17,GPIO.LOW)     # humidifier off
        if humi > 70:
            print "DEHUM                  -ON"
            GPIO.output(23,GPIO.HIGH)    # dehumidifier on
        else:
            print "DEHUM                  -OFF"    
            GPIO.output(23,GPIO.LOW)     # dehumidifier off

    if 22 <= temp < 23:   # want hum 60-70%
        print "HUM GOAL               (60-70%)"
        if humi < 60:
            print "HUM                    -ON"
            GPIO.output(17,GPIO.HIGH)    # humidifier on
        else:
            print "HUM                    -OFF"    
            GPIO.output(17,GPIO.LOW)     # humidifier off
        if humi > 70:
            print "DEHUM                  -ON"
            GPIO.output(23,GPIO.HIGH)    # dehumidifier on
        else:
            print "DEHUM                  -OFF"    
            GPIO.output(23,GPIO.LOW)     # dehumidifier off

    if 14 < temp < 22:   # want hum 60-65%
        print "HUM GOAL               (60-65%)"
        if humi < 60:
            print "HUM                    -ON"
            GPIO.output(17,GPIO.HIGH)    # humidifier on
        else:
            print "HUM                   -OFF"    
            GPIO.output(17,GPIO.LOW)     # humidifier off
        if humi > 65:
            print "DEHUM                  -ON"
            GPIO.output(23,GPIO.HIGH)    # dehumidifier on
        else:
            print "DEHUM                 -OFF"    
            GPIO.output(23,GPIO.LOW)     # dehumidifier off

    if temp < 24:   # TEMPERATURE LOW LIMIT HEATING PAD (75f)
        print "heating pad            -ON"
        GPIO.output(27,GPIO.HIGH)   # heating pad ON
    else:
        print "heating pad            -OFF"
        GPIO.output(27,GPIO.LOW)# heating pad off
        
schedule.every(1).hour.do(exhaust) # run exhaust every hour 
schedule.every(5).seconds.do(humtemp)  # run humidity and temp check every 5 sec

while 1:
    schedule.run_pending()
    time.sleep(1)
