import pygame as pg
import numpy
import cv2
from pygame.locals import *
import Tkinter as tk
import Image, ImageTk
from About import *
from showbmp import *
import OpenGL
import os
#from Main import *
from showbmp import *
import ValueSelected

class Root():
	w,h=800,600
	def __init__(self,x,y,z):
		self.VideoDeviceNumber=x
		self.Names=y
		self.Dict=z

	def setDeviceNumber(self,x):
		self.VideoDeviceNumber=x
		
	def func(self):
			del self.cap
			#self.root.destroy()
			#pg.display.init()
			#pg.display.quit()
			obj=ValueSelected.ComboBox(self.Names,self.Dict)
			obj.CreateComboBox()
			self.VideoDeviceNumber = obj.d
			#self.CreateMainWindow()
			
	def ShowFrame(self):
		try:
				del self.embed
		except:
				pass
		self.embed = tk.Frame(self.root, width=Root.w, height=Root.h)#a frame called 'embed' is created that hosts the pygame graphics
		self.embed.pack()
		self.embed.tkraise()
		os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())# Tell pygame's SDL window which window ID to use
		self.root.update()
		pg.display.init()# Usual pygame initialization
		pg.display.set_mode((800,600), DOUBLEBUF|OPENGL|HWSURFACE|RESIZABLE)
		while 1:
			try:
				self.cap = cv2.VideoCapture(self.VideoDeviceNumber)
				_, self.frame = self.cap.read()
				self.frame = cv2.flip(self.frame, 1)
				self.im=ShowBmp(self.frame)
				wall(self.im)
				pg.display.flip()# Update the pygame display
				self.root.update()# Update the Tk display
				del self.cap
			except:
				pass
	def CreateMainWindow(self):
		self.root = tk.Tk()
		self.root.wm_title("Webcam Interface")
		menubar = tk.Menu(self.root)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command=self.root.destroy)
		menubar.add_cascade(label="File", menu=filemenu)
		editmenu = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Edit", menu=editmenu)
		self.VideoDeviceName=tk.StringVar()		
		editmenu.add_radiobutton(label="Settings", command=self.func)
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About", command=About)
		menubar.add_cascade(label="Help", menu=helpmenu)
		self.root.config(menu=menubar)
		self.ShowFrame()

			
