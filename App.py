from tkinter import *
import cv2
from PIL import Image, ImageTk
import subprocess
import speech_recognition as s_r
import time
from screen1 import Sign_to_text
from screen3 import About
from screen2 import Speech_to_sign
import os
import tensorflow as tf
from keras.models import model_from_json
import tkinter.ttk

#shows "Loading" window
class Splash(Toplevel):
    def __init__(self, parent):
       	self.root = Toplevel(parent.root)
       	self.root.geometry("700x400")
        self.root.title("Intial Setup")

        self.panel1 = Label(self.root , text = "Sign Language Recognition System\n Preconfiguration",font = ("Courier",20), fg = "black")
        self.panel1.place(x = 100, y = 60)

        self.panel2 = Label(self.root ,font = ("Courier",15), fg = "red")
        self.panel2.place(x = 100, y = 200 )

        self.progress = tkinter.ttk.Progressbar(self.root, orient = HORIZONTAL, length = 400, mode = 'determinate')
        self.progress.place(x = 150 , y = 150)
        self.bar()
        ## required to make window show before the program gets to the mainloop
        self.root.update()
    def bar(self):

    	self.progress['value'] = 10
    	self.panel2.configure(text = "Intializing")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 20
    	self.panel2.configure(text = "Checking Permissions")
    	self.root.update()
    	time.sleep(1)
    	

    	self.progress['value'] = 40
    	self.panel2.configure(text = "Checking Network Connection")
    	self.root.update()
    	time.sleep(1)


    	self.progress['value'] = 60
    	self.panel2.configure(text = "Loading Models from disk")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 80
    	self.panel2.configure(text = "Securing Mic Access")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 100
    	self.panel2.configure(text = "Complete")
    	self.root.update()
    	time.sleep(1)

    def destroy(self):
    	self.root.destroy()

#Home screen
class Application:
	def __init__(self):


		#Home
		self.root = Tk()
		self.root.title("Dashboard")
		self.root.geometry("1200x500")
		self.root.configure(bg = "gray17")
		self.root.withdraw()
		splash = Splash(self)

		self.panel1 = Label(self.root , text = "Sign Language Recognition System",font = ("Courier",40),bg = "gray14" , fg = "spring green")
		self.panel1.place(x = 100, y = 60 )

		self.bt1 = Button(self.root ,text = "Sign to Speech Convertor" ,font = ("Courier",20), command = self.action1,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt1.place(x = 255,y=150)

		self.bt2 = Button(self.root ,text = "Speech to sign Convertor" , font = ("Courier",20), command = self.action2,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt2.place(x = 255,y=250)

		self.bt3 = Button(self.root ,text = "About" , command = self.action3, font = ("Courier",20),bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt3.place(x = 255,y=350)
		
		#speech to sign
		self.r = s_r.Recognizer()
		self.my_mic = s_r.Microphone()

		self.directory = 'model\\'
		self.json_file = open(self.directory+"model-bw.json", "r")
		self.model_json = self.json_file.read()
		self.json_file.close()
		self.bw_model = model_from_json(self.model_json)
		self.bw_model.load_weights(self.directory+"model-bw.h5")

		self.json_file = open(self.directory+"model-dru.json", "r")
		self.model_json = self.json_file.read()
		self.json_file.close()
		self.dru_model = model_from_json(self.model_json)
		self.dru_model.load_weights(self.directory+"model-dru.h5")

		self.json_file = open(self.directory+"model-tkdi2.json", "r")
		self.model_json = self.json_file.read()
		self.json_file.close()
		self.tkdi_model = model_from_json(self.model_json)
		self.tkdi_model.load_weights(self.directory+"model-tkdi2.h5")

		self.json_file = open(self.directory+"model-vw.json", "r")
		self.model_json = self.json_file.read()
		self.json_file.close()
		self.vw_model = model_from_json(self.model_json)
		self.vw_model.load_weights(self.directory+"model-vw.h5")

		self.json_file = open(self.directory+"model-aesmn.json", "r")
		self.model_json = self.json_file.read()
		self.json_file.close()
		self.aesmn_model = model_from_json(self.model_json)
		self.aesmn_model.load_weights(self.directory+"model-aesmn.h5")
		time.sleep(7)

		splash.destroy()
		self.root.deiconify()

	def destructor(self):
		self.root.destroy()

	def action1(self):
		pba = Sign_to_text(obj)

	def action2(self):
		pba = Speech_to_sign(obj)
		
	def action3(self):
		pba = About(obj)

obj = Application()
obj.root.mainloop()