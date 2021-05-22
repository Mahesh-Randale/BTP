import speech_recognition as s_r
from tkinter import *
import subprocess
import cv2
from PIL import Image, ImageTk
import pyttsx3

class Speech_to_sign:
	def __init__(self , obj):
		
		self.path = r"images\\gestures\\"
		
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('voice', self.voices[1].id)
		self.engine.setProperty('rate' , 130)
		
		self.curr_index = 0
		self.r = obj.r
		self.my_mic = obj.my_mic

		self.root2 = Toplevel(obj.root)
		self.root2.title("Speech to Sign")
		self.root2.protocol('WM_DELETE_WINDOW', self.destructor)
		self.root2.geometry("1200x900")
		self.root2.configure(bg = "gray17")

		self.e1 = Entry(self.root2 , width = 50)
		self.e1.place(x = 100 , y = 400)
		self.e1.insert(0 , "")

		self.string = self.e1.get()
		self.length = len(self.string)
		

		self.p1 = Label(self.root2 , text = "Speech to\n Sign",font = ("Courier",40),bg = "gray14" , fg = "spring green")
		self.p1.place(x = 100, y = 60 )
		
		self.l1 = Label(self.root2,text = "",font = ("Courier",5))
		self.l1.place(x=600 , y=650)

		self.letter = Label(self.root2 , text = "" , font = ("Courier",50,"bold"),bg = "gray16" , fg = "pink")
		self.letter.place(x = 730,y = 550)
		
		self.bt_mic = Button(self.root2 ,text = "Speak Here" ,command = self.convert_speech,font = ("Courier",15,"bold"))
		self.bt_mic.place(x=300, y=600)

		self.bt_enter = Button(self.root2 ,text = "Enter text" ,command = self.convert_text,font = ("Courier",15,"bold"))
		self.bt_enter.place(x=150, y=450)

		self.forward = Button(self.root2 ,text = "--->>" ,font = ("Courier",15,"bold"),command = lambda :self.next(self.curr_index+1))
		self.forward.place(x=800, y=650)

		self.back = Button(self.root2 ,text = "<<---" ,font = ("Courier",15,"bold"),command = lambda :self.prev(self.curr_index-1))
		self.back.place(x=600, y=650)

		self.bt_reset1 = Button(self.root2 ,text = "Reset" ,font = ("Courier",15,"bold"),command = self.reset1)
		self.bt_reset1.place(x=100, y=700)

		self.img_panel = Label(self.root2 , bg = "gray11" )
		self.img_panel.place(x = 500, y = -60, width = 600, height = 600)


	def load_image(self , curr):
		string = self.e1.get()
		if(string[curr] == " "):
			final = self.path + "0.jpg"
		else:
			final = self.path + string[curr] + ".jpg"
		img = cv2.imread(final)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
		img = cv2.resize(img , (500 , 500))
		img = Image.fromarray(img)
		imgtk1 = ImageTk.PhotoImage(image = img)
		self.letter['text'] = string[curr].upper()
		return imgtk1

	def next(self , curr):
		self.img_panel.configure(image = None)
		self.imgtk1 = self.load_image(curr)
		self.img_panel.imgtk1 = self.imgtk1
		self.img_panel.configure(image = self.imgtk1 )
		
		self.curr_index = self.curr_index+1

	def prev(self,curr):
		self.img_panel.configure(image = None)
		self.imgtk1 = self.load_image(curr)
		self.img_panel.imgtk1 = self.imgtk1
		self.img_panel.configure(image = self.imgtk1 )
		
		self.curr_index = self.curr_index-1

	def gesture_to_voice(self):
		self.engine.say("Speak now")
		self.engine.runAndWait()

	def convert_speech(self):
		#self.gesture_to_voice()
		with self.my_mic as source:
			self.r.adjust_for_ambient_noise(source)
			print("Say now!!!!")

			audio = self.r.listen(source)
		string = self.r.recognize_google(audio)
		word = self.e1.get()
		self.e1.delete(0, 'end')
		self.l1['text'] = word +" " + string
		self.e1.insert(0 , word +" " + string)
		self.imgtk1 = self.load_image(0)
		self.img_panel.imgtk1 = self.imgtk1
		self.img_panel.configure(image = self.imgtk1 )
		#self.letter['text'] = self.l1['text'][0]

	def convert_text(self):
		string = self.e1.get()
		self.l1['text'] = string
		self.imgtk1 = self.load_image(0)
		self.img_panel.imgtk1 = self.imgtk1
		self.img_panel.configure(image = self.imgtk1 )
		#self.letter['text'] = self.l1['text'][0]

	def reset1(self):
		self.l1['text'] = ""
		self.e1.delete(0, 'end')
		final = self.path + "0.jpg"
		img = cv2.imread(final)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(img)
		self.imgtk1 = ImageTk.PhotoImage(image = img)
		self.img_panel.imgtk1 = self.imgtk1
		self.img_panel.configure(image = self.imgtk1 )
		self.letter['text'] = ""
		self.curr_index = 0
		self.string = ""
		self.length = 0
		self.forward['state'] = "normal"

	def destructor(self):
		self.root2.destroy()
