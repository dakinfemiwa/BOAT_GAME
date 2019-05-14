import tkinter
from tkinter import ttk
from tkinter import *
import threading
import time
import random

class BoatPlay:
    def __init__(self):
        self.title = "BOAT RACING"
        self.background = "#282828"
        self.background2= "black"
        self.foreground = "white"
        self.background2 = "#7A7A7A"
        self.background3 = "lightblue"
        self.pos = 0.6
        self.bgPos = 1
        self.kayakPos = 400
        self.gameOver = False
        self.points = 0
        self.multiplyer = 1
        self.lane = 2
        self.obstacleImages = [['kayakO1.png'], ['kayakO3.png'],
                               ['kayakO5.png'],['kayakO2.png']]
        self.ObstaclePhImgs = []
        self.obstacles = []
                               

        self.file = Tk()
        self.file.attributes("-topmost", True)
        self.file.title(self.title)
        self.file.geometry("1250x575+10+50")
        self.file.overrideredirect(1)
        self.file.config(bg=self.background)

        self.exitButton = Button(self.file, text=" × ", command=lambda :self.close(), font="Arial 35", bd=0, background=self.background,foreground="white", cursor="hand2", justify="left")
        self.exitButton.config(activebackground="black", activeforeground="gray")
        self.exitButton.place(relx=.93, rely=-.02)

        self.fileTitle = Label(self.file, text=self.title, background=self.background, font="Segoe 29 bold")
        self.fileTitle.config(fg="white")
        self.fileTitle.place(relx=.0, rely=.025)

        self.gameCanvas = Canvas(self.file, width=1250, height=500, background=self.background2, bd=0)
        self.gameCanvas.place(relx=.0, rely=.1)

        self.imagePhoto = PhotoImage(file="sea.png")
        self.KayakImage = PhotoImage(file="kayak.png")

        self.image = self.gameCanvas.create_image(625, self.bgPos, image=self.imagePhoto)
        self.kayak = self.gameCanvas.create_image(625, self.kayakPos, image=self.KayakImage)

        self.Players = [self.kayak, 625, self.kayakPos]

        self.pointsLabel = Label(self.file, text="|  POINTS: " + str(self.points), background=self.background, foreground="white", font="Segoe 14")
        self.pointsLabel.place(relx=.225, rely=.05)

        self.levelLabel =  Label(self.file, text="  LEVEL: " + str(self.multiplyer), background=self.background, foreground="white", font="Segoe 14")
        self.levelLabel.place(relx=.75, rely=.05)

        self.file.bind("<Key>", lambda event:self.moveKayak(event))

        threading.Thread(target=self.moveBackground, args=()).start()
        threading.Thread(target=self.showPoints, args=()).start()
        threading.Thread(target=self.startObstacles, args=()).start()
        threading.Thread(target=self.file.mainloop(), args=()).start()

    def showPoints(self):
        while self.gameOver == False:
            time.sleep(.025 / (2 ** (self.multiplyer - 2)))
            self.points += random.randint(1,3)
            self.pointsLabel['text'] = "|  POINTS: " + str(self.points)
            if self.points >= (500 * (self.multiplyer ** 2)):
                self.multiplyer += 1
                self.levelLabel['text'] = "  LEVEL: " + str(self.multiplyer)
        if self.gameOver == True:
            return False

    

    def moveKayak(self, event):
        if self.gameOver == False:
            if event.keysym == "Left":
                if self.lane - 1 >= 1:
                    self.lane -= 1
                    self.gameCanvas.move(self.kayak, -300, 0)
                    self.Players[1] -= 300
            if event.keysym == "Right":
                if self.lane + 1 <= 3:
                    self.lane += 1
                    self.gameCanvas.move(self.kayak, 300, 0)
                    self.Players[1] += 300


    def close(self):
        self.file.destroy()

    def moveBackground(self):
        while True and self.gameOver == False:
            time.sleep(.02)
            self.oribgPos = self.bgPos
            self.bgPos -= -20
            self.bgPos = (self.bgPos % 100)

            self.yChange = self.bgPos - self.oribgPos
            self.gameCanvas.move(self.image, 0, self.yChange)
        if self.gameOver == True:
            return False
            
            """self.bgPos = (self.bgPos % 10)
            print(self.bgPos)
            self.imageLabel.place(relx=0, rely=self.bgPos)"""

    def startObstacles(self):
        while True and self.gameOver == False:
            if self.multiplyer < 5:
                time.sleep(.02)
            elif self.multiplyer < 10:
                time.sleep(.0175)
            else:
                time.sleep(.0155)

            for o in range(0, len(self.obstacleImages)):
                self.pic = PhotoImage(file=self.obstacleImages[o])
                self.ObstaclePhImgs.append(self.pic)

            random.shuffle(self.ObstaclePhImgs)

            self.yOValue = -100

            self.ranLane = random.randint(1, 3)
            self.xDistan = 25 + (300 * self.ranLane)
            self.obstacle = self.gameCanvas.create_image(self.xDistan, -100, image=self.ObstaclePhImgs[0])
            self.obstacles.append([])
            self.obstacles[len(self.obstacles) - 1].append(self.obstacle)
            self.obstacles[len(self.obstacles) - 1].append(self.xDistan)
            self.obstacles[len(self.obstacles) - 1].append(self.yOValue)


            for obstacle in self.obstacles:
                while obstacle[2] <=1250:
                    i = self.obstacles.index(obstacle)
                    if self.multiplyer < 5:
                        time.sleep(.023)
                    elif self.multiplyer < 10:
                        time.sleep(.0185)
                    else:
                        time.sleep(.0125)

                    self.gameCanvas.move(obstacle[0], 0, 10)
                    self.obstacles[i][2] += 10
                        
                    obstX = obstacle[1]
                    obstY = obstacle[2]
                    obstYR = obstY + 185

                    if (obstYR - self.Players[2] >= - 2 and obstYR - self.Players[2] < 395) and obstX == self.Players[1]:
                        self.gameOver = True
                        break

                if self.gameOver == True:
                    break

                if obstacle[2] >= 1300:
                    i = self.obstacles.index(obstacle)
                    self.obstacles.pop(i)
   
        if self.gameOver == True:
            self.end()
            return False

    def end(self):
        self.gameCanvas.delete(self.Players[0])
        try:
            for obstacle in self.obstacles:
                self.gameCanvas.delete(obstacle[0])
        except:
            pass

        self.gameOverLabel = self.gameCanvas.create_text(.5*1250, .4*650, text="GAME OVER\n"+"Score: "+ str(self.points), font="Verdana 40", fill="white", justify="center")

     

if __name__ == '__main__':
    BoatPlay = BoatPlay()
