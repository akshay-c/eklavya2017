### This Wiki Section is designed to explain the code in the file -[ValueSelected.py](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/blob/master/ValueSelected.py)
## Tkinter: Python GUI used to create windows
Tkinter is used as the Python GUI toolkit in our code. Tk is an open source multiplatform widget toolkit that is used by many different languages for building GUI Program.Tkinter interface is implemented as a Python module which is just a wrapper around a C extension that uses Tcl/Tk libraries.
**How to install Tkinter in Python?**
Press open your terminal using Ctrl+Alt+t
***
`$ sudo apt-get install python-tk`
Thread: [How to install Tkinter](https://stackoverflow.com/questions/26702119/installing-tkinter-on-ubuntu-14-04)
***
The packages imported in the file are-
Tkinter,[ImageTk](http://pillow.readthedocs.io/en/3.1.x/reference/ImageTk.html)
***
* The ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images.
*  class PIL.ImageTk.PhotoImage(image=None, size=None, **kw) -> A Tkinter-compatible photo image. This can be used everywhere Tkinter expects an image object. If the image is an RGBA image, pixels having alpha 0 are treated as transparent. The constructor takes either a PIL image, or a mode and a size. Alternatively, you can use the file or data options to initialize the photo image object.
***
A [ComboBox](#) combines an entry with a list of choices available to the user. This lets them either choose from a set of values you've provided (e.g. typical settings), but also put in their own value (e.g. for less common cases you don't want to include in the list).
![Combobox](http://www.tkdocs.com/images/w_combobox_all.png).
'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''
#Bug 2.0 remove the 10 and 11 line

#The necessary packages are imported
from Tkinter import *
import Image, ImageTk
from Root import * #local package
from Main import * #local package


class ComboBox():
	
	def __init__(self,x,y,Boards): #constructor of the class ComboBox		
		#Values to the instance variables are assigned
		self.Names=x
		self.Dict=y
		self.Boards=Boards
		self.d=0
		
	def ValueSelected(self): #callback function which is called when the button in the combobox is clicked
		
		TempString=self.Dict[self.z1.get()] #value of the selection is stored in a temporary string variable
		self.d=int(TempString[5:6]) #slicing operation is done to extract the VideoDeviceNumber
		self.b=self.z2.get() #value of the arduino selected is stored in self.b
		self.window1.quit()	 #the combobox window is made inactive 
		self.window1.destroy() #the combobox window is destroyed
		
				
	def CreateComboBox(self):
		
		self.window1=Tk()  #A window is created
		self.window1.geometry("270x100") #specify the width and height of the window
		self.window1.title("Select Webcam")  #title of the window is declared here
		
		self.z1= StringVar(self.window1) #object of StringVar() class that will store the value selected from combo box
		self.z1.set(self.Names[0]) #the first variable is set as default variable
		self.w1 =OptionMenu(self.window1,self.z1,*self.Names) #an OptionMenu tk widget is created that will display elements of self.names
		self.w1.pack()#OptionMenu is packed inside the window created
		
		self.z2= StringVar(self.window1) #object of StringVar() class that will store the value selected from combo box
		self.z2.set(self.Boards[0]) #default value is the first element in self.Boards
		self.w2 =OptionMenu(self.window1,self.z2,*self.Boards) #OptionMenu for displaying the arduino devices is created
		self.w2.pack() #OptionMenu is packed
		self.b1 = Button(self.window1, text="OK", command=self.ValueSelected) #A Button widget is created which will call the function self.valueselected() on clicking
		self.b1.pack() #Button is packed
		self.window1.mainloop()  #the window which was created is started

		
***
Explanation of the above given code is as under-