import cv2
from tkinter import *
import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import hunspell
import pyttsx3
from keras.models import model_from_json
from string import ascii_uppercase
import numpy as np
import operator
import os
import tkinter.ttk
import time

class Splash(Toplevel):
    def __init__(self, parent):
       	self.root = Toplevel(parent.root)
       	self.root.geometry("700x400")
        self.root.title("Sign Recognition Resource Acquirement")

        self.panel1 = Label(self.root , text = "Loading and Configuring Dependencies",font = ("Courier",20), fg = "black")
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
    	self.panel2.configure(text = "Intializing Sign Recognition")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 20
    	self.panel2.configure(text = "Configuring CNN Models")
    	self.root.update()
    	time.sleep(1)
    	

    	self.progress['value'] = 30
    	self.panel2.configure(text = "Loading Weights and Images")
    	self.root.update()
    	time.sleep(1)


    	self.progress['value'] = 50
    	self.panel2.configure(text = "Securing Dictionaries")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 60
    	self.panel2.configure(text = "Word Suggestions Activated")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 70
    	self.panel2.configure(text = "pyttsx3 Engine ready")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 80
    	self.panel2.configure(text = "Accessing Webcam")
    	self.root.update()
    	time.sleep(1)

    	self.progress['value'] = 100
    	self.panel2.configure(text = "Complete")
    	self.root.update()
    	time.sleep(1)

    def destroy(self):
    	self.root.destroy()

class Sign_to_text:
	

	def __init__(self, obj):

		self.root = Toplevel(obj.root)
		self.root.title("Gesture to Text and Voice")
		self.root.protocol('WM_DELETE_WINDOW', self.destructor)
		self.root.geometry('1600x1000')
		self.root.configure(bg = "gray11")
		self.root.withdraw()
		splash = Splash(self)

		#RGB feed
		self.panel1 = Label(self.root)
		self.panel1.place(x = 500 , y = -60 , width = 600 , height = 600)

		#binary feed
		self.panel2 = Label(self.root)
		self.panel2.place(x = 800 , y = 95 , width = 250 , height = 250 )

		#Gesture Chart
		self.gesturechart = cv2.imread("images\\canny.png")
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
		self.bt0 = Button(self.root ,text = "Enter" ,font = ("Courier",15,"bold"),command = self.suggest , bg = "gray9", fg = "deepskyblue2")
		self.bt0.place(x=600, y=500)
		#sign to speech buuton
		self.bt_speak = Button(self.root , text = "Speak" , font =("Courier",15,"bold"),command = self.gesture_to_voice , bg = "gray9", fg = "deepskyblue2")
		self.bt_speak.place(x=800, y=500)

		#reset buttons
		self.bt_reset = Button(self.root , text = "Reset" ,font = ("Courier",15,"bold"),command = self.reset,bg = "gray9", fg = "deepskyblue2")
		self.bt_reset.place(x=1000, y=500)

		#Suggestion buttons
		self.bt1 = Button(self.root , command = self.action1 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt1.place(x = 1125,y=60)

		self.bt2 = Button(self.root , command = self.action2 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt2.place(x = 1265,y=110)

		self.bt3 = Button(self.root , command = self.action3 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt3.place(x = 1405,y=60)

		self.bt4 = Button(self.root , command = self.action4 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt4.place(x = 1125,y=160)

		self.bt5 = Button(self.root , command = self.action5 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt5.place(x = 1265,y=210)

		self.bt6 = Button(self.root , command = self.action6 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt6.place(x = 1405,y=160)

		self.bt7 = Button(self.root , command = self.action7 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt7.place(x = 1125,y=270)

		self.bt8 = Button(self.root , command = self.action8 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt8.place(x = 1265,y=330)

		self.bt9 = Button(self.root , command = self.action9 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt9.place(x = 1405,y=270)

		self.bt10 = Button(self.root , command = self.action10 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt10.place(x = 1125,y=390)

		self.bt11 = Button(self.root , command = self.action11 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt11.place(x = 1265,y=450)

		self.bt12 = Button(self.root , command = self.action12 ,bg = "gray9", fg = "pink" , height = 0,width = 0)
		self.bt12.place(x = 1405,y=390)

		self.bw_model = obj.bw_model
		self.dru_model = obj.dru_model
		self.tkdi_model = obj.tkdi_model
		self.vw_model = obj.vw_model
		self.aesmn_model = obj.aesmn_model

		self.directory = 'model\\'
		self.cam = cv2.VideoCapture(0)
		self.current_image = None
		self.canny_img = None
		self.image_x = 128
		self.image_y = 128

		

		self.ct = {}
		self.ct['blank'] = 0
		self.blank_flag = 0
		for i in ascii_uppercase:
			self.ct[i] = 0

		self.sentence = ""
		self.word = ""
		self.current_symbol = "Empty"
		

		curr_dir = os.getcwd()
		
		dir1 = curr_dir + '/dictionary'
		
		self.h = hunspell.Hunspell('en_US' , hunspell_data_dir=dir1)
		

		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('voice', self.voices[1].id)
		self.engine.setProperty('rate' , 130)
		
		splash.destroy()
		self.root.deiconify()
		self.videoloop()

	def keras_process_image(self,img):
		img = cv2.resize(img, (self.image_x, self.image_y))
		img = np.array(img, dtype=np.float32)
		img = np.reshape(img, (1, self.image_x, self.image_y, 1))
		return img

	def predict(self,test_image):
		test_image = self.keras_process_image(test_image)
		result = self.bw_model.predict(test_image)
		prediction={}
		prediction['blank'] = result[0][0]
		inde = 1
		for i in ascii_uppercase:
			prediction[i] = result[0][inde]
			inde += 1
		prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
		self.current_symbol = prediction[0][0]
		if(self.current_symbol == 'D' or self.current_symbol == 'R' or self.current_symbol == 'U'):
			result_dru = self.dru_model.predict(test_image)
			prediction = {}
			prediction['D'] = result_dru[0][0]
			prediction['R'] = result_dru[0][1]
			prediction['U'] = result_dru[0][2]
			prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
			self.current_symbol = prediction[0][0]
		if(self.current_symbol == 'D' or self.current_symbol == 'I' or self.current_symbol == 'K' or self.current_symbol == 'T'):
			result_tkdi = self.tkdi_model.predict(test_image)
			prediction = {}
			prediction['D'] = result_tkdi[0][0]
			prediction['I'] = result_tkdi[0][1]
			prediction['K'] = result_tkdi[0][2]
			prediction['T'] = result_tkdi[0][3]
			prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
			self.current_symbol = prediction[0][0]

		if(self.current_symbol == 'M' or self.current_symbol == 'N' or self.current_symbol == 'S'):
			result_smn = self.aesmn_model.predict(test_image)
			prediction1 = {}
			prediction1['M'] = result_smn[0][0]
			prediction1['N'] = result_smn[0][1]
			prediction1['S'] = result_smn[0][2]
			prediction1 = sorted(prediction1.items(), key=operator.itemgetter(1), reverse=True)
			if(prediction1[0][0] == 'S'):
				self.current_symbol = prediction1[0][0]
			else:
				self.current_symbol = prediction[0][0]
		if(self.current_symbol == 'V' or self.current_symbol == 'W'):
			result_vw = self.vw_model.predict(test_image)
			prediction1 = {}
			prediction1['V'] = result_vw[0][0]
			prediction1['W'] = result_vw[0][1]
			prediction1 = sorted(prediction1.items(), key=operator.itemgetter(1), reverse=True)
			self.current_symbol = prediction1[0][0]
		
		if(self.current_symbol == 'blank'):
			for i in ascii_uppercase:
				self.ct[i] = 0
		self.ct[self.current_symbol] += 1
		if(self.ct[self.current_symbol] > 45):
			for i in ascii_uppercase:
				if i == self.current_symbol:
					continue
				tmp = self.ct[self.current_symbol] - self.ct[i]
				if tmp < 0:
					tmp *= -1
				if tmp <= 5:
					self.ct['blank'] = 0
					for i in ascii_uppercase:
						self.ct[i] = 0
					return
			self.ct['blank'] = 0
			for i in ascii_uppercase:
				self.ct[i] = 0
			if self.current_symbol == 'blank':
				if self.blank_flag == 0:
					self.blank_flag = 1
					if len(self.sentence) > 0:
						self.sentence += " "
					self.sentence += self.word
					self.word = ""
			else:
				self.blank_flag = 0
				self.word += self.current_symbol

	def videoloop(self):
		ok , img = self.cam.read()
		if ok:
			img = cv2.flip(img , 1)
			img = cv2.cvtColor(img ,cv2.COLOR_BGR2RGBA)
			self.current_image = Image.fromarray(img)
			imgtk = ImageTk.PhotoImage(image = self.current_image)
			self.panel1.imgtk = imgtk
			self.panel1.configure(image = imgtk)
			
			gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray,(5,5),2)
			th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
			ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			res = res[50:300 ,275:625]
			self.canny_img = Image.fromarray(res)
			imgtk = ImageTk.PhotoImage(image = self.canny_img)
			self.panel2.imgtk = imgtk
			self.panel2.configure(image = imgtk)
			self.predict(res)
			self.label4.config(text = self.current_symbol)
			self.label2.config(text=self.sentence,font=("Courier",20))
			self.label6.config(text = self.word ,font=("Courier",20))
			predicts=self.h.suggest(self.word)
			self.list2 = []
			for s in predicts:
				if s.startswith(self.word):
					self.list2.append(s)
			self.suggest()


		self.root.after(10 , self.videoloop)

	def gesture_to_voice(self):
		string = self.label2['text']
		self.engine.say(string)
		self.engine.runAndWait()

	def reset(self):
		self.label2['text'] = ""
		self.label4['text']=""
		self.label6['text']=""
		self.word=""
		self.sentence=""
		self.bt1.config(text = "")
		self.bt2.config(text = "")
		self.bt3.config(text = "")
		self.bt4.config(text = "")
		self.bt5.config(text = "")
		self.bt6.config(text = "")
		self.bt7.config(text = "")
		self.bt8.config(text = "")
		self.bt9.config(text = "")
		self.bt10.config(text = "")
		self.bt11.config(text = "")
		self.bt12.config(text = "")

	def suggest(self):
		dic = self.list2
		if (len(dic)) >0:
			self.bt1.config(text=dic[0],font = ("Courier",20))
		else:
			self.bt1.config(text = "")

		if (len(dic)) >1:
			self.bt2.config(text=dic[1],font = ("Courier",20))
		else:
			self.bt2.config(text = "")

		if (len(dic)) >2:
			self.bt3.config(text=dic[2],font = ("Courier",20))
		else:
			self.bt3.config(text = "")

		if (len(dic)) >3:
			self.bt4.config(text=dic[3],font = ("Courier",20))
		else:
			self.bt4.config(text = "")

		if (len(dic)) >4:
			self.bt5.config(text=dic[4],font = ("Courier",20))
		else:
			self.bt5.config(text = "")

		if (len(dic)) >5:
			self.bt6.config(text=dic[5],font = ("Courier",20))
		else:
			self.bt6.config(text = "")

		if (len(dic)) >6:
			self.bt7.config(text=dic[6],font = ("Courier",20))
		else:
			self.bt7.config(text = "")

		if (len(dic)) >7:
			self.bt8.config(text=dic[7],font = ("Courier",20))
		else:
			self.bt8.config(text = "")

		if (len(dic)) >8:
			self.bt9.config(text=dic[8],font = ("Courier",20))
		else:
			self.bt9.config(text = "")
		
		if (len(dic)) >9:
			self.bt10.config(text=dic[9],font = ("Courier",20))
		else:
			self.bt10.config(text = "")

		if (len(dic)) >10:
			self.bt11.config(text=dic[10],font = ("Courier",20))
		else:
			self.bt11.config(text = "")

		if (len(dic)) >11:
			self.bt12.config(text=dic[11],font = ("Courier",20))
		else:
			self.bt12.config(text = "")


	def action1(self):
		dic = self.list2
		if (len(dic)) > 0:
			self.word = ""
			self.sentence = self.label2['text'] + " " + dic[0]
			

	def action2(self):
		dic = self.list2
		if (len(dic)) > 1:
			self.sentence = self.label2['text'] + " " + dic[1]
			

	def action3(self):
		dic = self.list2
		if (len(dic)) > 2:
			self.sentence = self.label2['text'] + " " + dic[2]
			self.word = ""

	def action4(self):
		dic = self.list2
		if (len(dic)) > 3:
			self.sentence = self.label2['text'] + " " + dic[3]
			self.word = ""

	def action5(self):
		dic = self.list2
		if (len(dic)) > 4:
			self.sentence = self.label2['text'] + " " + dic[4]
			self.word = ""

	def action6(self):
		dic = self.list2
		if (len(dic)) > 5:
			self.sentence = self.label2['text'] + " " + dic[5]
			self.word = ""
	
	def action7(self):
		dic = self.list2
		if (len(dic)) > 6:
			self.sentence = self.label2['text'] + " " + dic[6]
			self.word = ""

	def action8(self):
		dic = self.list2
		if (len(dic)) > 7:
			self.sentence = self.label2['text'] + " " + dic[7]
			self.word = ""

	def action9(self):
		dic = self.list2
		if (len(dic)) > 8:
			self.sentence = self.label2['text'] + " " + dic[8]
			self.word = ""

	def action10(self):
		dic = self.list2
		if (len(dic)) > 9 :
			self.sentence = self.label2['text'] + " " + dic[9]
			self.word = ""

	def action11(self):
		dic = self.list2
		if (len(dic)) > 10:
			self.sentence = self.label2['text'] + " " + dic[10]
			self.word = ""
	
	def action12(self):
		dic = self.list2
		if (len(dic)) > 11:
			self.sentence = self.label2['text'] + " " + dic[11]
			self.word = ""

	def about_window(self):
		self.destructor()
		subprocess.call(['python' , 'about.py'])

	def speech_to(self):
		self.destructor()
		subprocess.call((['python' , 'speech_to_sign.py']))

	def destructor(self):
		print("Closing Application")
		self.root.destroy()
		self.cam.release()
"""
print("Starting Application...")
pba = Application()
pba.root.mainloop()
"""