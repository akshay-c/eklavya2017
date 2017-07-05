Go to [Integration.py](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/blob/master/Integration.py) file to read the code.
In the previous section-
"Generation of Ply File from Co ordinates Of a Point in 3D Space"
We learned how to generate a .ply file , if we have X,Y and Z coordinate lists of an object edge.From the frames captured from the camera, we generate total 256 files in .txt format having combined x and y co-ordinate of all contour points in a frame.
***
In the integration.py file in main directory [Integration.py](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/blob/master/Integration.py) we have code for how to plot it and visualize it using matplotlib.
Understand the conversion of co-ordinate to Spherical System
[Spherical Co-ordinate](http://tutorial.math.lamar.edu/Classes/CalcIII/SphericalCoords.aspx)
***
### Description about the spherical coordinate system . 
***
In mathematics, a spherical coordinate system is a coordinate system for three-dimensional space where the position of a point is specified by three numbers: the radial distance of that point from a fixed origin, its polar angle measured from a fixed zenith direction, and the azimuth angle of its orthogonal projection on a reference plane that passes through the origin and is orthogonal to the zenith, measured from a fixed reference direction on that plane. It can be seen as the three-dimensional version of the polar coordinate system.

The radial distance is also called the radius or radial coordinate. The polar angle may be called colatitude, zenith angle, normal angle, or inclination angle.

The use of symbols and the order of the coordinates differs between sources. In one system frequently encountered in physics (r, θ, φ) gives the radial distance, polar angle, and azimuthal angle, whereas in another system used in many mathematics books (r, θ, φ) gives the radial distance, azimuthal angle, and polar angle. In both systems ρ is often used instead of r. Other conventions are also used, so great care needs to be taken to check which one is being used.
Src : https://en.wikipedia.org/wiki/Spherical_coordinate_system
***
The explanation of code is given below
***
#The necessary packages are imported 

    import math
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib
    from matplotlib import cm
    from matplotlib import pyplot as plt
    import os
    
#The SavePLY file made to generate the .ply file using X,Y and Z list is also imported
***
    import SavePLY

#An integration class is made
***
    class Integration():
*** 
"""With the help of X , Y co-ordinate and angle of rotation of our object , we generate Radius,theta and phi.The camera we are using in our project can't analyze depth of the object ,so we don't have Z value of a point, so we take help of the rotation of the object mounted on stand.Now matplotlib can plot X,Y and Z co-ordinate , so we now convert R,theta and phi to X1,Y1,Z1 co-ordinate for plotting"
***
    def __init__(self):
#Empty list is initialized to store the X and Y co-ordinates of all the frames
***
    self.X=[] #this will contain the x coordinates of all the frames
    self.Y=[] #this will contain the y coordinates of all the frames
    self.Radius=[] #This will contain value of all the Radius
    self.theta=[] #This will contain all the values of theta
    self.phi=[] #This will contain the phi values of all the points,Phi is determined by the rotation of our object
***
Now after initializing the instance of the class, we define other functions as-
***
The camera generates contour points and then for our total 256 captured frame , a single text file is generated
(so total 256 files are generated) in a folder whose path can be input using the variable- folderpath                
***		
    def ReadFile(self,folderpath):
***
The method chdir() changes the current working directory to the given path.It returns None in all the cases.path -- This is complete path of the directory to be changed to a new location.
***
    os.chdir(folderpath)
***
Now we enter the folder containing all the files.
***
    for i in range(0,256):
Run the for loop to visit each .txt file.
Now the .txt files are from 0.txt to 255.txt.So i is converted to string concatenated with .txt extension,now use of flag r, it Opens text file for reading.  The stream is positioned at the beginning of the file.
***
*** Description of Files (0.txt to 255.txt) that are generated-***
It has two sections one part showing the x-values of all the points captured in a particular frame, and the other showing the y-values respectively.
*** 
    f=open(str(i)+'.txt','r')
***
Now from each file we have to separate the x and y data for all points in a particular frame.
To understand the basics how to do it.Please visit this [link](https://stackoverflow.com/questions/9857731/python-read-in-string-from-file-and-split-it-into-values)
***
    data=f.read().split('\n\n')
Read the file using read() function and split the content in the text file having two newline distance between them,our main aim is to split each file x and y section separate add them all in a list and make a final x and y,convert it to radius,theta and phi.
For example if we want to split a based on ",".
***
    a = "123,456" 
    b = a.split(",")
    print b
    >>['123', '456']
    c = [int(e) for e in b]
    print c
    [123, 456]
    x, y = c
    print x
    >>123
    print y
    >>456
***
Now data will have two values x and y denoted by data[0] and data[1],the x and y values will be enclosed in  "[]" and each x values and y values in their respective section will be separated by "," we need to remove [] and separate each values and store them. 
The below mentioned code removes the 1st and last element of data[0] and data[1] i.e. [ and ]
***
    data[0]=data[0][1:(len(data[0])-1)]
    data[1]=data[1][1:(len(data[1])-1)]
***
Now we split each data section around "," and store the values in Xcoordinate and Ycoordinates.
### The x and y coordinates captured in the .txt files by camera, are swapped for matplotlib because for matplotlib the co-ordinates are just opposite.
A question arises here-
*** 
Q.Can we swap the final x and y co-ordinate that is generated from R,theta and phi and plot it? 
***
A.No, we cannot ,because formula for phi is arctan(y/x), so if we try to convert it afterwards , it will be error and we will not get desired result.Thus now we swap the section and store the data[1] in Xcoordinate and data[0] in Ycoordinate.
***
    Xcoordinate=data[1].split(',')
    Ycoordinate=data[0].split(',')
***
    R=[] #this will contain the value of Radius for a single frame
    th=[] #this will contains the values of all the theta for a single frame
***
We are in a for loop and considering each file,now each Xcoordinate and Ycoordinate is a list containing all points.Now  conversion is shown here-
[Conversion](https://wikimedia.org/api/rest_v1/media/math/render/svg/d93ebb804a548a5bbebd33f3bb330c65ae461cff).Take Xcoordinate each element, use the corresponding Ycoordinate element and find R ,so we use for loop for traversing and then store it as element in R list
*** 
    for i in range(len(Xcoordinate)):
    R.append(math.sqrt(float(Xcoordinate[i])**2+float(Ycoordinate[i])**2))
***
Now for calculation of phi values,(we are considering the anticlockwise direction movement) we use general formula arctan(y/x),also a condition may arise, when Xcoordinate value is 0 (i.e. on the Y-Axis ) at that time possible values of theta can be either 90 degree or 270 degree calculated from the positive x-axis respectively.)
***
    if float(Xcoordinate[i])==0:
    if float(Ycoordinate[i])>=0:
    th.append(3.14159/2)
    else:
    th.append(3*3.14159/2)
    else:
    th.append(np.arctan(float(Ycoordinate[i])/float(Xcoordinate[i])))	
***			
			
    self.Radius.append(R) #append the values of the Radius in self.Radius
    self.theta.append(th) #append the values oh theta in self.theta
***
Also value is appended in the phi list per frame.
360 degree is convered in 256 step, each step traverses angle 360/256 degree, now convert it into radian.
((360/256)*pi)/180.
***
    for k in range(256):
    self.phi.append((0.02454)*k)
			
    print self.phi
***
Now we append each frame's R and theta value in the Radius and theta empty list initialized at beginning of the code, also phi list is initialized storing values.
***
### Explanation of the Plot3D code.
Now we visualize Radius and theta as a 2D array , i denote each line and j denote coloumn,So [i][j] will give us location of each element in the list.Also with each element,we need to add phi value of frame.So we run nested loop, and generate finalR, finaltheta and finalphi.Also from these we generate X1,Y1 and Z1 respectively and plot them using matplotlib respectively.Here we take use of the SavePLY file and send these co-ordinates of X1,Y1 and Z1 to it, to finally generate .ply file using ***SavePLY.SavePLY(X1,Y1,Z1)***

***		
	def Plot3D(self):
		finalR=[]
		finaltheta=[]
		finalphi=[]
		for i in range(len(self.Radius)):
			for j in range(len(self.Radius[i])):
				finalR.append(float(self.Radius[i][j]))
				finaltheta.append(float(self.theta[i][j]))
				finalphi.append(float(self.phi[i]))
		#print finalphi
		#print self.phi
		X1=[]
		Y1=[]
		Z1=[]
		for i in range(len(finalR)):
			X1.append(finalR[i] * np.sin(finaltheta[i]) * np.cos(finalphi[i])) #final x coordinate of the point is calculated for plotting
			Y1.append(finalR[i] * np.sin(finaltheta[i]) * np.sin(finalphi[i])) #final y coordinate of the point for plotting
			Z1.append(finalR[i] * np.cos(finaltheta[i])) #final z coordinate of the point for plotting
		
		
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		SavePLY.SavePLY(X1,Y1,Z1)
		ax.scatter(X1, Y1, Z1)
		plt.show()
		

'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''

		
