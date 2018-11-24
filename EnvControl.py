"""humidity and temp control
-3 relay duo outlets
1) heating pad + circulating fan (GPIO27)
2) exhaust fan (GPIO18)
3) humidifier (GPIO17)
DHT22 (GPIO4)
"""

import Adafruit_DHT as dht    # imports Adafruit lib for DHT22
import sched, time                   # imports time lib
import threading
import RPi.GPIO as GPIO       # imports GPIO lib
from PyQt5.QtCore import (QThread, pyqtSignal)


class EnvHandler(QThread):
    finished = pyqtSignal()
    schedDelay = 900
    def __init__(self, observer):
        super().__init__()
        self.observer = observer
        self.humPin = 17 # humidifiers gpio pin is 17
        self.exhPin = 18 # exhaust fans gpio pin is 18
        self.heatPin = 27 # heating pads gpio pin is 27
        self.hourlyFanOn = False


    def run(self):
        #self.exhaustThread = threading.Thread(self.exhaustSchedule()).start()
        self.adjustEnvironment()

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.exhPin,GPIO.OUT)    # exhaust fan
        GPIO.setup(self.heatPin,GPIO.OUT)    # heating pad




    def adjustEnvironment(self):
        statusDict = {
            "temperatureState": "0",
            "humidityState" : "0",
            "fanState": "OFF",
            "heatState":"OFF",
            "humidifierState":"OFF"
        }
        try:
            while 1:                # Loop will run forever
                # humi = 20.00
                #temp = 40.00
                humi, temp = dht.read_retry(dht.DHT22, 4)  # Reading humidity and temperature
                statusDict['temperatureState']= '{0:0.1f}*C'.format(float(temp))
                statusDict['humidityState']= '{0:0.1f}%'.format(float(humi))
                #print 'Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(float(temp),float(humi))
                if humi < 70:    # HUMIDITY LOW LIMIT
                    statusDict["humidifierState"]="ON"
                    #print "humidifier  -on"
                    GPIO.output(self.humPin,GPIO.HIGH)   # humidifier on
                else:
                    statusDict["humidifierState"] = "OFF"
                    #print "humidifier -off"
                    GPIO.output(self.humPin,GPIO.LOW)    # humidifier off
                if temp < 24:   # TEMPERATURE LOW LIMIT HEATING PAD (75f)
                    statusDict["heatState"] = "ON"
                    #print "heating pad -on"
                    GPIO.output(self.heatPin,GPIO.HIGH)   # heating pad ON
                else:
                    statusDict["heatState"] = "OFF"
                    #print "heating pad -off"
                    GPIO.output(self.heatPin,GPIO.LOW)# heating pad off
                if not self.hourlyFanOn:
                    if temp > 30:   # TEMPERATURE HIGH LIMIT EXHAUST FAN (85f)
                        statusDict["fanState"]="ON"
                        #print "exhaust fan -on"
                        GPIO.output(self.exhPin,GPIO.HIGH)   # exhaust fan on
                    else:
                        statusDict["fanState"] = "OFF"
                        #print "exhaust fan -off"
                        GPIO.output(self.exhPin,GPIO.LOW)    # exhaust fan OFF
                else:
                    statusDict["fanState"] = "ON"
                self.updateObserver(statusDict)
                time.sleep(5)
        # If keyboard Interrupt is pressed
        except KeyboardInterrupt:
            # Shuts down the scheduler and the thread for it so that nothing is left unclosed.
            self.shutdown()
            pass  			# Go to next line

    def updateObserver(self, statusDict):
        self.observer.updateStat(statusDict)

    def shutdown(self):
        #self.scheduler.shutdown(wait=False)
        #self.exhaustThread.exit()
        return
    # ExhaustSchedule creates a scheduler for the exhaust fan, then adds the job for it to vent the fan every hour
    def exhaustSchedule(self):
        #self.scheduler = BlockingScheduler()
        #self.scheduler.add_job(self.hourlyExhaust, 'interval', hours=1)
       # self.scheduler.start()
        return
    # hourlyExhaust is the job that happens every hour. It sets hourlyFanOn to true, so that the main while-loop
    # can't turn the fan off, then turns the fan on for ten seconds, then relinquishes control of the fan back
    # to the main while-loop.
    def hourlyExhaust(self):
        self.hourlyFanOn = True
       # GPIO.output(self.exhPin, GPIO.HIGH)
        time.sleep(10)
       # GPIO.output(self.exhPin, GPIO.LOW)
        self.hourlyFanOn = False

