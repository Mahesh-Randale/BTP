from tkinter import *
import cv2
from PIL import Image, ImageTk
import tkinter.ttk

class Emergency:
	def __init__(self, parent):
		self.root1 = Toplevel(parent.root)
		self.root1.title("Emergency Mode")
		self.root1.geometry("500x570")
		self.label = Label(self.root1 , text = "Signs for Emergency" , fg = "red", font=("Courier",20))
		self.label.place(x = 100 , y = 10)
		self.gesturechart = cv2.imread("e1.jpg")
		self.panel3 = Label(self.root1)
		self.panel3.place(x =50 , y = 45 , width = 400 , height = 600)
		self.im1 = cv2.cvtColor(self.gesturechart, cv2.COLOR_BGR2RGBA)
		self.im1 = cv2.resize(self.im1, (400, 500))
		self.im1 = Image.fromarray(self.im1)
		self.g1 = ImageTk.PhotoImage(image = self.im1)
		self.panel3.img = self.g1
		self.panel3.configure(image = self.g1)
		self.root1.update()
		

	def destroy(self):
		self.root1.destroy()

class Shortcut:
	def __init__(self, parent):
		self.root1 = Toplevel(parent.root)
		self.root1.title("Shortcut Mode")
		self.root1.geometry("500x570")
		self.label = Label(self.root1 , text = "Signs for Shortcut" , fg = "red", font=("Courier",20))
		self.label.place(x = 100 , y = 10)
		self.gesturechart = cv2.imread("c1.jpg")
		self.panel3 = Label(self.root1)
		self.panel3.place(x =50 , y = 45 , width = 400 , height = 600)
		self.im1 = cv2.cvtColor(self.gesturechart, cv2.COLOR_BGR2RGBA)
		self.im1 = cv2.resize(self.im1, (400, 500))
		self.im1 = Image.fromarray(self.im1)
		self.g1 = ImageTk.PhotoImage(image = self.im1)
		self.panel3.img = self.g1
		self.panel3.configure(image = self.g1)
		self.root1.update()
		

	def destroy(self):
		self.root1.destroy()

class Sign_to_text:
	def __init__(self):

		self.root = Tk()
		self.root.title("Gesture to Text and Voice")
		#self.root.protocol('WM_DELETE_WINDOW', self.destructor)
		self.root.geometry('1600x1000')
		self.root.configure(bg = "gray7")
		self.mode = "Character"
		self.modelabel = Label(self.root ,bg = "gray1" ,text = self.mode, fg = "spring green" , font=("Courier",30))
		self.modelabel.place(x = 600 , y = 570)
		self.Emergency_flag = False
		self.shortcut_flag = False
		#RGB feed
		self.panel1 = Label(self.root)
		self.panel1.place(x = 500 , y = -60 , width = 600 , height = 600)

		#binary feed
		self.panel2 = Label(self.root)
		self.panel2.place(x = 800 , y = 95 , width = 250 , height = 250 )

		#Gesture Chart
		self.gesturechart = cv2.imread("canny.png")
		self.panel3 = Label(self.root)
		self.panel3.place(x = 50 , y = 0 , width = 400 , height = 500)
		self.im1 = cv2.cvtColor(self.gesturechart, cv2.COLOR_BGR2RGBA)
		self.im1 = cv2.resize(self.im1, (400, 500))
		self.im1 = Image.fromarray(self.im1)
		self.g1 = ImageTk.PhotoImage(image = self.im1)
		self.panel3.img = self.g1
		self.panel3.configure(image = self.g1)

		#sentence
		self.label1 = Label(self.root , text = "Sentence:" , bg = "gray1" , fg = "red", font=("Courier",20))
		self.label1.place(x = 50 , y = 700)

		self.label2 = Label(self.root , bg = "gray1" , fg = "yellow")
		self.label2.place(x = 250 ,y = 700)

		#Predicted letter
		self.label3 = Label(self.root , text = "Predicted letter:" , bg = "gray1" , fg = "red" , font=("Courier",20))
		self.label3.place(x = 50 , y = 580)

		self.label4 = Label(self.root ,bg = "gray1" , fg = "cyan" , font=("Courier",20))
		self.label4.place(x = 350 , y = 580)

		#word formation
		self.label5 = Label(self.root , text = "Current Word:" , bg = "gray1" , fg = "red", font=("Courier",20))
		self.label5.place(x = 50 , y = 640)

		self.label6 =  Label(self.root ,bg = "gray1" , fg = "cyan" , font=("Courier",20))
		self.label6.place(x = 350 , y = 640)
		#suggestion header
		self.label7 = Label(self.root ,bg = "gray1" ,text ="Suggestions", fg = "spring green" , font=("Courier",30))
		self.label7.place(x = 1200 , y = 10)


		#Buttons

		#enter buuton

		self.bt0 = Button(self.root ,text = "Emergency" ,font = ("Courier",15,"bold"),command = self.Emergency , bg = "snow", fg = "deepskyblue2")
		self.bt0.place(x=530, y=500)

		self.bt01 = Button(self.root ,text = "Shortcuts" ,font = ("Courier",15,"bold"),command = self.Shortcut , bg = "snow", fg = "deepskyblue2")
		self.bt01.place(x=700, y=500)

		
		#sign to speech buuton
		self.bt_speak = Button(self.root , text = "Speak" , font =("Courier",15,"bold"),command = self.action , bg = "snow", fg = "deepskyblue2")
		self.bt_speak.place(x=870, y=500)

		#reset buttons
		self.bt_reset = Button(self.root , text = "Reset" ,font = ("Courier",15,"bold"),command = self.action,bg = "snow", fg = "deepskyblue2")
		self.bt_reset.place(x=1000, y=500)

		#Suggestion buttons
		self.bt1 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt1.place(x = 1125,y=60)

		self.bt2 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt2.place(x = 1265,y=110)

		self.bt3 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt3.place(x = 1405,y=60)

		self.bt4 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt4.place(x = 1125,y=160)

		self.bt5 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt5.place(x = 1265,y=210)

		self.bt6 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt6.place(x = 1405,y=160)

		self.bt7 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt7.place(x = 1125,y=270)

		self.bt8 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt8.place(x = 1265,y=330)

		self.bt9 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt9.place(x = 1405,y=270)

		self.bt10 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt10.place(x = 1125,y=390)

		self.bt11 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt11.place(x = 1265,y=450)

		self.bt12 = Button(self.root , command = self.action ,bg = "snow", fg = "gray1" , height = 0,width = 0,font = ("Courier",20))
		self.bt12.place(x = 1405,y=390)
	def Shortcut(self):
		if self.shortcut_flag == False:
			self.root.configure(bg = "gray43")
			self.modelabel.configure(text = "Shortcut Mode")
			self.sh = Shortcut(self)

		if self.shortcut_flag == True:
			self.destroy2(self.sh)
			self.root.configure(bg = "gray7")
			self.modelabel.configure(text = "Character Mode")
		self.shortcut_flag = not self.shortcut_flag

	def destroy2(self , sh):
		self.sh.root1.destroy()

	def destroy1(self , em):
		self.em.root1.destroy()



	def Emergency(self):
		if self.Emergency_flag == False:
			self.root.configure(bg = "IndianRed1")
			self.modelabel.configure(text = "Emergency Mode")
			self.em = Emergency(self)
			
			#self.reset()
		if self.Emergency_flag == True:
			self.destroy1(self.em)
			self.root.configure(bg = "gray10")
			self.modelabel.configure(text = "Character Mode")
			#self.reset()
		self.Emergency_flag = not self.Emergency_flag
	def action(self):
		self.label2['text'] = "Text here"
		self.label4['text']="Text here"
		self.label6['text']="Text here"
		self.word="Text here"
		self.sentence="Text here"
		self.bt1.config(text = "Text here")
		self.bt2.config(text = "Text here")
		self.bt3.config(text = "Text here")
		self.bt4.config(text = "Text here")
		self.bt5.config(text = "Text here")
		self.bt6.config(text = "Text here")
		self.bt7.config(text = "Text here")
		self.bt8.config(text = "Text here")
		self.bt9.config(text = "Text here")
		self.bt10.config(text = "Text here")
		self.bt11.config(text = "Text here")
		self.bt12.config(text = "Text here")

		
pb = Sign_to_text()
pb.root.mainloop()