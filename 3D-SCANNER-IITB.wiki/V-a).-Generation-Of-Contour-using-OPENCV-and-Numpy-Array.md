Migrate to the file Root.py
We are writing a detailed description of working of the code.To access an image pixel is similar to access numpy ndarray elements.

***
 For a general BGR image.
if we follow below codes

    import cv2
    import numpy as np
    img=cv2.imread('path',-1)
    px=img[100,100]
    print px
***
It will  return an array of Blue,Green and Red value at that pixel location, so to access a pixel value we need it's row and coloumn coordinates and then it returns whatever it finds.Also to only access Blue value we can give location as [100,100,0] setting 3rd value in the [] to 0 for B, 1 for G, 2 for R
Also whenever an image is loaded using gray scale the pixel will only be accessed by two argument one of row and other of coloumn and it will return the intensity of the pixel value in the terms of shades of black and white.
Thresholding Operations using inRange function :  
    1) Perform basic thresholding operations using OpenCV function cv2.inRange
    2) Detect an object based on the range of pixel values it has
    3) Checks if array elements lie between the elements of two other arrays. 
So in the inRange function we need to pass ndarray when we need to compare it with frame that is captured so these values are used (which can be dynamically changed as per our requirement) , In the def __init__(self,x,y,z,a,n): #constructor of the class
We have created instance as such of 
    `self.redlow=240`
    `self.redup=255`
    `self.greenlow=150`
    `self.greenup=255`
    `self.bluelow=235`
    `self.blueup=255`

See example here : http://docs.opencv.org/trunk/da/d97/tutorial_threshold_inRange.html 
Now we have to do the thresholding of the frame that is captured ,so made 
    `self.upper= np.array([self.blueup,self.greenup,self.redup]) `#upper limit of BGR values of the laser line
    `self.mask = cv2.inRange(self.frame, self.lower, self.upper) `#create a mask within the specified values of RED
    `self.mask = cv2.inRange(self.frame, self.lower, self.upper)`
A copy is created of the original frame-
    `self.output_img = self.frame.copy()` 
***
Use of numpy.where(condition[, x, y])
condition : array_like, bool
            When True, yield x, otherwise yield y.
            x, y : array_like, optional
            Values from which to choose. x and y need to have the same shape as condition.
Return   :+1: out : ndarray or tuple of ndarrays
                    If both x and y are specified, the output array contains elements of x where condition is True,            
                    and elements from y elsewhere.
                    If only condition is given, return the tuple condition.nonzero(), the indices where condition is  
                    True.
Its Use
***
    `self.output_img[np.where(self.mask==0)] = 0` #where the mask value is 0, make those coordinates black
    `self.output_img[np.where(self.mask>100)] =255` #The target points, or the points which belong to the laser line                     
                                                     #are displayed in white
***
As we know mask is thresholded and only contains black and white color as intensity, so the above lines simply , takes the points where the value of mask is 0 and at that corresponding points make the value of output_img to black and at points where mask value is above 100 makes it White,these points are the target points which belong to the laser line .
***
Morphological Operations-
The most basic morphological operations are two: Erosion and Dilation. They have a wide array of uses, i.e. :
1.Removing noise
2.Isolation of individual elements and joining disparate elements in an image.
3.Finding of intensity bumps or holes in an image
Link to learn about Erode and Dilation : http://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html
So we perform the following operations: 
    self.gray = cv2.cvtColor(self.output_img, cv2.COLOR_BGR2GRAY)
    self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
    self.thresh = cv2.threshold(self.gray, 45, 255, cv2.THRESH_BINARY)[1]
    self.thresh = cv2.erode(self.thresh, None, iterations=2)
    self.thresh = cv2.dilate(self.thresh, None, iterations=2)
