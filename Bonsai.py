'''
 Bonsai is the presentor for the project.
 @author: Bryce Hutton
 @Date: 11/23/2018
'''

import GUI
import EnvControl
import datetime
import threading
from apscheduler.schedulers.blocking import BlockingScheduler

class Bonsai():
    def __init__(self):
        self.lastDict = None
        self.envCon = EnvControl.EnvHandler(self)
        self.gui = GUI.GUI(self)

      #  self.envCon.exhaustThread = threading.Thread(target=self.envCon.exhaustSchedule()).start()

        self.gui.UIThread = threading.Thread(target=self.gui.create()).start()
        self.envCon.statusCheckerThread = threading.Thread(target=self.envCon.adjustEnvironment()).start()

     #   self.scheduledUpdates()
        
    def scheduledUpdates(self):
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(self.scheduledMessage(), 'interval', minutes=15)

    def scheduledMessage(self):
        if self.lastDict == None:
            return
        message = ("temperature is ", + self.lastDict["temperatureState"] +
                   ", humidity is " + self.lastDict["humidityState"] +
                   ", fan is " + self.lastDict["fanState"] +
                   ", heating pad is " + self.lastDict["heatState"] +
                   ", humidifier is " + self.lastDict["humidifierState"])
    def addMessages(self, message):
        now = datetime.datetime.now()
        updatedMessage = str(now.hour) + ":" + str(now.minute) + " - " + message
        self.gui.displayMessage(updatedMessage)

    def shutdown(self):
        self.envCon.shutdown()
        exit()
    def update(self, statusDict):  
       # if it's the first time running, update headers and send startup messages.
        if self.lastDict == None:
            self.gui.updateStatus(statusDict)
            self.addMessages("Bonsai Environmental Control turned ON")
            self.addMessages("fan turned " + statusDict["fanState"])
            self.addMessages("heating pad turned " + statusDict["heatState"])
            self.addMessages("humidifier turned " + statusDict["humidifierState"])
        else:
            # if the result is the same as last time, don't bother updating.
            if not statusDict == self.lastDict:
                #Always update the headers.
                self.gui.updateStatus(statusDict)
            # Only do a message log if something has been turned on or off.
            if not statusDict["fanState"] == self.lastDict["fanState"]:
                self.addMessages("fan turned " + statusDict["fanState"])
            if not statusDict["heatState"] == self.lastDict["heatState"]:
                self.addMessages("heating pad turned " + statusDict["heatState"])
            if not statusDict["humidifierState"] == self.lastDict["humidifierState"]:
                self.addMessages("humidifier turned " + statusDict["humidifierState"])
        self.lastDict = statusDict
        
        


Bonsai()