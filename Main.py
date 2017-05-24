import os
import v4l2
import fcntl
from ValueSelected import *
from showbmp import *
from About import *
from Root import *

AboutText = """
This is a software where you can select the Video Device and get the output
Developed by Team SAAS, Ekalavya 2017, IITB"""


def RefreshCamList():
	CamList=[]
	AddressList=[]
	CamDict={}
	DeviceList=os.listdir("/dev") #it will return a list of the contents inside /dev
	for i in DeviceList:
		temp=i
		if (temp[:5]=='video'):
			AddressList.append(i) #the video devices are added to CamList
	for i in AddressList:
		vd = open("/dev/"+i, 'rw') 
		cp = v4l2.v4l2_capability()
		fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp) 
		CamList.append(cp.card)
		CamDict[cp.card]=i
	return CamList,CamDict

def Main():
	VideoDeviceNumber=0
	CamList,CamDict=RefreshCamList() #this will update the list of new devices ,if any new is connected
	MainWindow=Root(VideoDeviceNumber,CamList,CamDict)
	MainWindow.CreateMainWindow()

Main()
