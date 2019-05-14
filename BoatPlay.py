import tkinter
from tkinter import ttk
from tkinter import *
import threading
import time
import random

class BoatPlay:
    def __init__(self):
        self.title = "BOAT RACING"
        self.background = "black"
        self.background2= "black"
        self.foreground = "white"
        self.background2 = "#7A7A7A"
        self.pos = 0.6
        self.bgPos = 10
        self.kayakPos = 400
        self.gameOver = False
        self.points = 0
        self.multiplyer = 1
        self.lane = 2
        self.obstacleImages = [['kayak.png'], ['kayak.png'],
                               ['kayak.png'], ['kayak.png'], ['kayak.png']]
        self.ObstaclePhImgs = []
        self.obstacles = []
                               

        self.file = Tk()
        self.file.attributes("-topmost", True)
        self.file.title(self.title)
        self.file.geometry("1250x650+10+50")
        self.file.overrideredirect(1)
        self.file.config(bg=self.background)

        self.exitButton = Button(self.file, text=" × ", command=lambda :self.close(), font="Arial 35", bd=0, background="black",foreground="white", cursor="hand2", justify="left")
        self.exitButton.config(activebackground="black", activeforeground="gray")
        self.exitButton.place(relx=.93, rely=-.02)

        self.fileTitle = Label(self.file, text=self.title, background=self.background, font="Segoe 29")
        self.fileTitle.config(fg="white")
        self.fileTitle.place(relx=.0, rely=.025)

        self.gameCanvas = Canvas(self.file, width=1250, height=500, background=self.background2, bd=0)
        self.gameCanvas.place(relx=.0, rely=.1)

        self.imagePhoto = PhotoImage(file="sea.png")
        self.KayakImage = PhotoImage(file="kayak.png")

        self.image = self.gameCanvas.create_image(625, self.bgPos, image=self.imagePhoto)
        self.kayak = self.gameCanvas.create_image(625, self.kayakPos, image=self.KayakImage)

        self.Players = [self.kayak, 625, self.kayakPos]

        self.pointsLabel = Label(self.file, text=self.points, background=self.background, foreground="white", font="MSSansSerif 29 bold", width=50, anchor=E, justify="right")
        self.pointsLabel.place(relx=.0, rely=.9)

        self.file.bind("<Key>", lambda event:self.moveKayak(event))

        threading.Thread(target=self.moveBackground, args=()).start()
        threading.Thread(target=self.showPoints, args=()).start()
        threading.Thread(target=self.startObstacles, args=()).start()
        threading.Thread(target=self.moveObstacle, args=()).start()
        threading.Thread(target=self.file.mainloop(), args=()).start()

    def showPoints(self):
        while self.gameOver == False:
            time.sleep(.025 / (2 ^ (self.multiplyer - 1)))
            self.points += random.randint(1,3)
            self.pointsLabel['text'] = self.points
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
            time.sleep(0.02)

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

        if self.gameOver == True:
            pass

    def moveObstacle(self):
        while True and self.gameOver == False:
            for obstacle in self.obstacles:
                while obstacle[2] <=1250:
                    i = self.obstacles.index(obstacle)
                    time.sleep(.02)
                    self.gameCanvas.move(obstacle[0], 0, 10)
                    self.obstacles[i][2] += 10
                        
                    obstX = obstacle[1]
                    obstY = obstacle[2]
                    obstYR = obstY + 185

                    if (obstYR - self.Players[2] >= - 15 and obstYR - self.Players[2] <= 400) and obstX == self.Players[1]:
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
        self.gameOverFrame = Frame(self.gameCanvas, background=self.background).place(relx=.35, rely=.35)
        self.gameOverLabel = Label(self.gameOverFrame, text="GAME OVER", background=self.background, font="Verdana 40", foreground="white").place(relx=.4, rely=.4)
        self.gameOverPoint = Label(self.gameOverFrame, text="Score: "+ str(self.points), background=self.background, font="Verdana 20", foreground="white")
        self.gameOverPoint.place(relx=.475, rely=.5)
        
                    

    
            
            
        

if __name__ == '__main__':
    BoatPlay = BoatPlay()
