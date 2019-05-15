import tkinter
from tkinter import ttk
from tkinter import *
import threading
import time
import random

class BoatPlay:
    def __init__(self):
        """Use the left and right keys to move.
        Avoid the other boats."""
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
        self.ranLane = 0
        self.ranLanPr = 0        


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
        self.gameOver = True
        self.close2()

    def close2(self):
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
                time.sleep(.0002)
            elif self.multiplyer < 10:
                time.sleep(.00075)
            else:
                time.sleep(.0125)

            for o in range(0, len(self.obstacleImages)):
                self.pic = PhotoImage(file=self.obstacleImages[o])
                self.ObstaclePhImgs.append(self.pic)


            for o in range(2):
            
                random.shuffle(self.ObstaclePhImgs)

                self.yOValue = -100

                while self.ranLane == self.ranLanPr:
                    self.ranLane = random.randint(1, 3)
                
                
                self.ranLanPr = self.ranLane
                self.xDistan = 25 + (300 * self.ranLane)
                self.obstacle = self.gameCanvas.create_image(self.xDistan, -100, image=self.ObstaclePhImgs[0])
                self.obstacles.append([])
                self.obstacles[len(self.obstacles) - 1].append(self.obstacle)
                self.obstacles[len(self.obstacles) - 1].append(self.xDistan)
                self.obstacles[len(self.obstacles) - 1].append(self.yOValue)


            for obstacle in self.obstacles:
                while obstacle[2] <=1250:
                    i = self.obstacles.index(obstacle)
                    if True:                            
                        if self.multiplyer < 5:
                            time.sleep(.023)
                        elif self.multiplyer < 10:
                            time.sleep(.0195)
                        elif self.multiplyer < 12:
                            time.sleep(.005)

                    self.gameCanvas.move(obstacle[0], 0, 10)
                    self.obstacles[i][2] += 10
                    choice = random.randint(0,1)

                    if choice == 1:
                        try:
                            pass
                            #ranT = random.randint(-20, 20)
                            #time.sleep(.0001 * ranT)
                            #self.gameCanvas.move(self.obstacles[i+1][0], 0, 10)
                            #self.obstacles[i+1][2] += 10
                        except:
                            pass
                        
                    obstX = obstacle[1]
                    obstY = obstacle[2]
                    #obsTX = self.obstacles[i+1][1]
                    #obsTY = self.obstacles[i+1][2]
                    obstYR = obstY + 185
                    #obsTYR = obsTY + 185

                    if (obstYR - self.Players[2] >= - 2 and obstYR - self.Players[2] < 350) and obstX == self.Players[1]:
                        self.gameOver = True
                        break

                    """if (obsTYR - self.Players[2] >= - 2 and obsTYR - self.Players[2] < 350) and obsTX == self.Players[1]:
                        self.gameOver = True
                        break  """                  

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
        with open("highScore.pdf", "r")as highScoreRead:
            highScoreRd = highScoreRead.readline()
            if int(highScoreRd) < self.points:
                self.newHighScore = True
            else:
                self.newHighScore = False

        self.gameOverLabel = self.gameCanvas.create_text(.5*1250, .4*650, text="GAME OVER\n", font="Verdana 40", fill="white", justify="center")
        self.gameOverLabel = self.gameCanvas.create_text(.5*1250, .45*650, text="Score: "+ str(self.points), font="Verdana 20", fill="white", justify="center")
        if self.newHighScore == True:
             with open("highScore.pdf", "w")as highScoreRead:
                highScoreRead.write(str(self.points))
             self.highScoreLabel = self.gameCanvas.create_text(.5*1250, .65*650, text="NEW HIGH SCORE ", font="Verdana 20", fill="white", justify="center")

                
if __name__ == '__main__':
    BoatPlay = BoatPlay()
