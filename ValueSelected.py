
from Tkinter import *
import Main
#from RefreshCamList import *
import Image, ImageTk

CamNameSelected=''

class ComboBox():
	def __init__(self,x,y):
		self.Names=x
		self.Dict=y
	def ValueSelected(self):
		TempString=''
		TempString=self.Dict[self.z.get()]
		d=int(TempString[5:6])
		self.window1.destroy()
		Main.Main(d)		
	def CreateComboBox(self):
		self.window1=Tk()  #A window is created
		self.window1.geometry("270x60") 
		self.z= StringVar(self.window1) #object of StringVar() class that will store the value selected from combo box
		self.window1.title("Select Webcam")  #Title of the window is declared here
		self.z.set(self.Names[0])
		self.w =OptionMenu(self.window1,self.z,*self.Names)
		self.w.pack()
		self.b1 = Button(self.window1, text="OK", command=self.ValueSelected)
		self.b1.pack()
		self.window1.mainloop()  #the window which was created is started
		
		
