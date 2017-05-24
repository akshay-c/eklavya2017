import Tkinter as tk
import Main

def About():
	PopupWindow=tk.Tk()
	PopupWindow.title("About")
	label1 =tk.Label(PopupWindow, text=Main.AboutText)
	label1.pack()
