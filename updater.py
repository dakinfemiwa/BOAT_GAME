import urllib.request
import tkinter
from tkinter import ttk
from tkinter import *
import time
import os

class Updater:
    def __init__(self):
        self.WindowTitle = "Update File"
        self.updateTitleText = "RACING GAME"
        self.updateButtonText = "  Update  ".upper()

        self.font1 = "Verdana 40 bold"
        self.font2 = "Ebrima 12"
        self.font3 = "Ebrima 20"

        self.background2 = "#000000"
        self.background1 = "#FFFFFF"
        self.foreground2 = "#FFFFFF"
        self.foreground1 = "#000000"

        self.updateWindow = Tk()
        self.updateWindow.title()
        self.updateWindow.geometry("500x300+500+100")
        self.updateWindow.overrideredirect(1)
        self.updateWindow.config(bg=self.background1)
        self.design = Canvas(self.updateWindow, width=500, height=300, background=self.background1, bd=0)
        self.design.place(relx=.0, rely=.0)

        self.updateLabel = Label(self.design, text=self.updateTitleText, font=self.font1)
        self.updateLabel.place(relx=.075, rely=.1)

        self.photo = PhotoImage(file="pattern.png")
        self.design.create_image(400, 250, image=self.photo)

        self.needUpdate = self.checkUpdates()

        if self.needUpdate == True:
            self.updateMessage = "Updated to latest version"
            self.displayStatus(self.updateMessage)
            #time.sleep(7)
            self.updateWindow.destroy()
        else:
            self.updateMessage = "Updating your device"
            self.displayStatus(self.updateMessage)
            #time.sleep(7)
            self.updateWindow.destroy()
            self.updateProgram()

        try:
            for widget in self.design.winfo_children():
                widget.config(fg=self.foreground1, bg=self.background1)


            self.update.config(bg=self.background2, fg=self.foreground2, bd=0, cursor="hand2")
        except:
            pass

        self.updateWindow.mainloop()

    def displayStatus(self, message):
        self.updateStatusLabel = Label(self.design, text=message, font=self.font2)
        self.updateStatusLabel.place(relx=.075, rely=.4)

    def updateProgram(self):
        file1 = "https://raw.githubusercontent.com/dakinfemiwa/BoatGame/master/BoatPlay.py"
        file2 = "https://raw.githubusercontent.com/dakinfemiwa/BoatGame/master/versionNo.pdf"

        name1 = "BoatPlayNew.py"
        name2 = "versionNoNew.py"

        oldFile1 = "BoatPlay.py"
        oldFile2 = "versionNo.pdf"

        files = [file1, file2]
        names = [name1, name2]
        oldFiles = [oldFile1, oldFile2]

        for x in range(0, len(files)):
            urllib.request.urlretrieve(files [x], names[x])
            try:
                os.remove(oldFiles[x])
            except:
                pass
            os.rename(names[x], oldFiles[x])

    def checkUpdates(self):
        with open("versionNo.txt", "r+") as updateFile:
            self.versionNoLine = updateFile.readlines()
            self.versionNo = self.versionNoLine[0]

        os.rename("versionNo.pdf", "versionNoC.pdf")

        source = "https://raw.githubusercontent.com/dakinfemiwa/BoatGame/master/versionNo.pdf"
        file = "versionNo.pdf"

        urllib.request.urlretrieve(source, file)

        with open("versionNo.txt", "r+") as self.updateFile:
            self.versionNoLine = self.updateFile.readlines()
            self.latestVersion = self.versionNoLine[0]

        os.remove("versionNo.pdf")
        os.rename("versionNoC.pdf", "versionNo.txt")

        if self.latestVersion == self.versionNo:
            return True
        else:
            return False
