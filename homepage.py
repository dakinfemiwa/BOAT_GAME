import tkinter
from tkinter import ttk
from tkinter import *
import threading
import random
import json
import time

class GameIntro:
    def __init__(self, username):
        self.title = "Game Lobby"
        self.loadConfig()
        
        self.gameLobbyFile = Tk()
        self.gameLobbyFile.title(self.title)
        self.gameLobbyFile.config(bg="black")

        self.windowWidth = self.gameLobbyFile.winfo_screenwidth()
        self.screenHeight = self.gameLobbyFile.winfo_screenheight()
        self.windowHeight = self.windowWidth // 2
        self.geometry = str(self.windowWidth - 50) + "x" + str(self.windowHeight - 50) + "+-7+0"
        self.yPos = ((self.screenHeight - self.windowHeight - 80)) / self.screenHeight
        print(self.yPos)

        self.gameLobbyFile.geometry(self.geometry)
        self.gameLobbyFile.state("zoomed")
        self.gameLobbyCanvas = Canvas(self.gameLobbyFile, height=self.windowHeight)
        self.gameLobbyCanvas.config(width=self.windowWidth - 3)
        self.gameLobbyCanvas.place(relx=0, rely=self.yPos)

        """if self.introIndex == 0:
            self.gameLobbyCanvas.config(bg="white")
            self.leftDoor = self.gameLobbyCanvas.create_rectangle((0.35 * self.windowWidth), (0.28 * self.windowHeight), (0.495*self.windowWidth), (0.7*self.windowHeight), fill="#BBBBBB")
            self.rightDoor = self.gameLobbyCanvas.create_rectangle((0.505 * self.windowWidth), (0.28 * self.windowHeight), (0.64*self.windowWidth), (0.7*self.windowHeight), fill="#BBBBBB")
            """
        if self.introIndex == 1:
            self.gameLobbyCanvas.config(bg="#101010")
            self.xPos = 0.5
            self.imagePhoto = PhotoImage(file="background1.png")
            #self.imageLabel = self.gameLobbyCanvas.create_image((self.windowWidth // 2), (self.windowHeight // 2), image=self.imagePhoto)

            self.leftDoor = self.gameLobbyCanvas.create_rectangle((0.00 * self.windowWidth), (0.00 * self.windowHeight), (0.50*self.windowWidth), (1.0*self.windowHeight), fill="#0B0B0B")
            self.rightDoor = self.gameLobbyCanvas.create_rectangle((0.5 * self.windowWidth), (0.00 * self.windowHeight), (1.00*self.windowWidth), (1.0*self.windowHeight), fill="#0B0B0B")
            
            threading.Thread(target=self.animate, args=()).start()
            threading.Thread(target=self.gameLobbyFile.mainloop(), args=()).start()

    def animate(self):
        while self.xPos < 1:
            time.sleep(.00001)
            self.gameLobbyCanvas.move(self.leftDoor, (-0.00125* self.windowWidth), 0)
            self.gameLobbyCanvas.move(self.rightDoor, (0.00125* self.windowWidth), 0)
            self.xPos += 0.00125

        self.homepage()

    def homepage(self):
        self.OptionFrame = Frame(self.gameLobbyCanvas, background="#1F1F1F", height=self.windowHeight, width=self.windowWidth * 0.3)
        self.OptionFrame.place(relx=.0, rely=.0)

        self.ButtonTypes = ["My Apps", "Download Apps", "My Account"]
        self.Buttons = []
        self.Frames = []

        self.ShowAppsFrame = Frame(self.gameLobbyCanvas, background="#262626", width=self.windowWidth * 0.7, height=self.windowHeight)
        self.ShowAppsFrame.place(relx=.3, rely=.0)

        self.ShowAppsText = Label(self.ShowAppsFrame, text=self.ButtonTypes[0], font="Ebrima 30 bold underline", background="#262626", foreground="white")
        self.ShowAppsText.place(relx=.05, rely=.05)

        for button in self.ButtonTypes:
            i = self.ButtonTypes.index(button)
            self.OptionButtons = Canvas(self.OptionFrame, background="black", width=round(self.windowWidth * 0.3), height=round(self.windowHeight*0.15))
            self.OptionButtons.config(cursor="hand2")
            self.OptionButtons.place(relx=.0, rely=i * 0.15)

            self.Text = Label(self.OptionButtons, text=button, font="Ebrima 30", background="black", foreground="white")
            self.Text.place(relx=.05, rely=.2)

            self.Buttons.append(self.OptionButtons)

            #self.OptionButtons.bind('<Button1>', lambda event:self.viewFrame(event))

    def viewFrame(self, event):
        for btn in self.Buttons:
            if event.widget == btn:
                self.index = self.Buttons.index(btn)
                break;
        
        self.Fr
    def loadConfig(self):
        with open("configuration.json", "r") as configRead:
            self.configuration = json.load(configRead)

        self.backgrounds = self.configuration['backgroundImages']
        self.intros = self.configuration['introTheme']
        self.backgroundIndex = self.configuration['backgroundIndex']
        self.introIndex = self.configuration['introIndex']
        self.fgColours = self.configuration['colours']

        self.background = self.backgrounds[self.backgroundIndex]
        


if __name__  in '__main__':
    GameIntro("dakinfemiwa")
