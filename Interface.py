
import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)
from BonsaiGUI import Ui_MainWindow
from EnvControl import EnvHandler
from apscheduler.schedulers.blocking import BlockingScheduler


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lastDict = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.envCon = None
        self.scheduled = 0

    # Add the environment that the GUI is getting the information from.
    def addEnv(self, env):
        self.envCon = env


    def scheduledMessage(self):
        if self.lastDict == None:
            return
        message = ("temperature is ", + self.lastDict["temperatureState"] +
                   ", humidity is " + self.lastDict["humidityState"] +
                   ", fan is " + self.lastDict["fanState"] +
                   ", heating pad is " + self.lastDict["heatState"] +
                   ", humidifier is " + self.lastDict["humidifierState"])
        self.addMessages(message)

    def addMessages(self, message):
        now = datetime.datetime.now()
        updatedMessage = "{:d}:{:02d}".format(now.hour, now.minute) + " - " + message
        self.ui.displayMessage.append("\n" + updatedMessage)
        self.show()

    def updateStatus(self, statusDict):
        self.ui.tempDisplay.setText("Temperature:" + statusDict['temperatureState'])
        self.ui.humDisplay.setText("Humidity:" + statusDict['humidityState'])
        self.ui.fanStatus.setText("FAN:" + statusDict['fanState'])
        self.ui.heatStatus.setText("HEAT:" + statusDict['heatState'])
        self.ui.humStatus.setText("HUMIDIFIER:" + statusDict['humidifierState'])
        self.show()

    def updateStat(self, statusDict):
       # if it's the first time running, update headers and send startup messages.
        if self.lastDict == None:
            self.updateStatus(statusDict)
            self.addMessages("Bonsai Environmental Control turned ON")
            self.addMessages("fan turned " + statusDict["fanState"])
            self.addMessages("heating pad turned " + statusDict["heatState"])
            self.addMessages("humidifier turned " + statusDict["humidifierState"])
        else:
            # if the result is the same as last time, don't bother updating.
            if not statusDict == self.lastDict:
                #Always update the headers.
                self.updateStatus(statusDict)
            # Only do a message log if something has been turned on or off.
            if not statusDict["fanState"] == self.lastDict["fanState"]:
                self.addMessages("fan turned " + statusDict["fanState"])
            if not statusDict["heatState"] == self.lastDict["heatState"]:
                self.addMessages("heating pad turned " + statusDict["heatState"])
            if not statusDict["humidifierState"] == self.lastDict["humidifierState"]:
                self.addMessages("humidifier turned " + statusDict["humidifierState"])
        self.lastDict = statusDict

app = QApplication(sys.argv)
w = AppWindow()
w.show()
thread = EnvHandler(w)
thread.finished.connect(app.exit)
thread.start()
sys.exit(app.exec_())