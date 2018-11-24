from tkinter import *
#from EnvControl import *

''' GUI is the user interface for the environment control.
 @author: Bryce Hutton
 @Date: 11/23/2018
'''

class GUI(object):
  #  envCon = EnvHandler()

    def __init__(self, controller):
        self.observer = controller
        # Displayinfo is a textbox with relevant information, such as turned on exhaust.
        self.displayMessage = None
        # tempDisplay and humDisplay is the temperature and humidity
        self.tempDisplay = None
        self.humDisplay = None
        # fanStatus,heatStatus,and humStatus is whether or not the fan, humidifier, and heating pad are turned on.
        self.fanStatus = None
        self.heatStatus = None
        self.humStatus = None
        self.create()

    # adds a message to the textbox.
    def addMessage(self, message):
        self.displayMessage.configure(state=NORMAL)
        self.displayMessage.insert(END, '\n' + message)
        self.displayMessage.configure(state=DISABLED)

    def updateStatus(self, statusDict):
        self.tempDisplay.configure(text="temp:" + statusDict['temperatureState'])
        self.humDisplay.configure(text="humidity:" + statusDict['humidityState'])
        self.fanStatus.configure(text="FAN:" + statusDict['fanState'])
        self.heatStatus.configure(text="HEAT:" + statusDict['heatState'])
        self.humStatus.configure(text="HUMIDIFIER:" + statusDict['humidifierState'])
    def on_closing(self,window):
        self.observer.shutdown()
        window.destroy()

    def create(self):
        #creates main window
        window = Tk()
        window.title("Bonsai Environment Control")
        window.resizable(False,False)
        window.configure(background="white")
        window.geometry('600x400')

        # Creates the displays and status for temp/hum
        self.tempDisplay = Label(window, text="temp:    .   ", bg="white", fg="black")
        self.tempDisplay.grid(row=0,column=0,sticky=W)

        self.humDisplay = Label(window, text="humidity:   ", bg="white", fg="black")
        self.humDisplay.grid(row=1, column=0, sticky=W)

        self.fanStatus = Label(window, text="FAN:OFF", bg="white", fg="black")
        self.fanStatus.grid(row=0,column=1, sticky=W)

        self.heatStatus = Label(window, text="HEAT:OFF", bg="white", fg="black")
        self.heatStatus.grid(row=0, column=2, sticky=W)

        self.humStatus = Label(window, text="HUMIDIFIER:OFF", bg="white", fg="black")
        self.humStatus.grid(row=1, column=1, sticky=W, columnspan=2)


        Label(window, text="", bg="white", fg="black").grid(row=2,column=1)
        Label(window, text="Message Log", bg="white", fg="black").grid(row=3, column=1)
        #creates frame for the textbox
        textFrame = Frame(window, width=400, height=200,background="black")
        textFrame.grid(row=4,column=0,columnspan=4)
        textFrame.columnconfigure(0,weight=1)
        textFrame.rowconfigure(0, weight=1)
        textFrame.grid_propagate(False)

        self.displayMessage = Text(textFrame, bg="white")
        self.displayMessage.grid(row=0, column=0, padx=2, pady=2,sticky="we")

        self.displayMessage.configure(state=DISABLED)

        scrollb = Scrollbar(textFrame, command=self.displayMessage.yview)
        scrollb.grid(row=0,column=1, sticky='nsew')
        self.displayMessage['yscrollcommand'] = scrollb.set

        window.protocol("WM_DELETE_WINDOW", self.on_closing(window))
        window.mainloop()
GUI()