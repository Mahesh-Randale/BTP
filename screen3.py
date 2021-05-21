from tkinter import *
import cv2
from PIL import Image, ImageTk
import subprocess

class About:
	def __init__(self , obj):
		
		self.root1 = Toplevel(obj.root)
		self.root1.title("About")
		self.root1.protocol('WM_DELETE_WINDOW', self.destructor)
		self.root1.geometry("1600x900")
		self.root1.configure(bg = "gray17")

		self.label = Label(self.root1 , text = "Made By:"  ,bg = "gray11" ,fg = "yellow" ,font = ("Courier",30,"bold"))
		self.label.place(x = 700 , y = 0)

		self.x = 300
		self.y = 300
		self.img1 = cv2.imread("images\\mahesh.jpg")
		self.img2 = cv2.imread("images\\sabale.jpg")
		self.img3 = cv2.imread("images\\sahil.jpg")
		self.img4 = cv2.imread("images\\sir.jpg")

		self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGBA)
		self.img1 = cv2.resize(self.img1, (self.x , self.y))
		self.img1 = Image.fromarray(self.img1)
		self.imgtk1 = ImageTk.PhotoImage(image = self.img1)

		self.img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2RGBA)
		self.img2 = cv2.resize(self.img2, (self.x , self.y))
		self.img2 = Image.fromarray(self.img2)
		self.imgtk2 = ImageTk.PhotoImage(image = self.img2)

		self.img3 = cv2.cvtColor(self.img3, cv2.COLOR_BGR2RGBA)
		self.img3 = cv2.resize(self.img3, (self.x , self.y))
		self.img3 = Image.fromarray(self.img3)
		self.imgtk3 = ImageTk.PhotoImage(image = self.img3)

		self.img4 = cv2.cvtColor(self.img4, cv2.COLOR_BGR2RGBA)
		self.img4 = cv2.resize(self.img4, (self.x , self.y))
		self.img4 = Image.fromarray(self.img4)
		self.imgtk4 = ImageTk.PhotoImage(image = self.img4)

		self.panel1 = Label(self.root1)
		self.panel1.place(x = 70, y = 70, width = 300, height = 300 )
		self.panel1.configure(image = self.imgtk1)
		self.label1 = Label(self.root1 , text = "Mahesh Randale\n111708050", font = ("Courier",15,"bold"))
		self.label1.place(x = 150 , y = 400)

		self.panel2 = Label(self.root1)
		self.panel2.place(x = 570, y = 70, width = 300, height = 300 )
		self.panel2.configure(image = self.imgtk2)
		self.label1 = Label(self.root1 , text = "Rushikesh Sabale\n111708052", font = ("Courier",15,"bold"))
		self.label1.place(x = 650 , y = 400)

		self.panel3 = Label(self.root1)
		self.panel3.place(x = 1070, y = 70, width = 300, height = 300 )
		self.panel3.configure(image = self.imgtk3)
		self.label3 = Label(self.root1 , text = "Sahil Jadhav\n111708053", font = ("Courier",15,"bold"))
		self.label3.place(x = 1100 , y = 400)


		self.panel4 = Label(self.root1)
		self.panel4.place(x = 600, y = 500, width = 250, height = 250 )
		self.panel4.configure(image = self.imgtk4)
		self.label4 = Label(self.root1 , text = "Under Guidance of :\nProf. Shirish Gosavi", font = ("Courier",15,"bold"))
		self.label4.place(x = 600 , y = 700)

	def destructor(self):
		self.root1.destroy()





