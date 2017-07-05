The link location is : [PLYwithfaces](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/blob/e470510a2bc3eedaebbbbbdd4840e05c840e7b1e/Miscellanous%20Applications/PLYwithFaces.py).
We have used **Delaunay triangulation**-The Delaunay triangulation is a subdivision of a set of points into a non-overlapping set of triangles, such that no point is inside the circumcircle of any triangle. In practice, such triangulations tend to avoid triangles with small angles.Delaunay triangulation can be computed using scipy.spatial.
***
[Difference between Matlab delaunayn and Scipy Delaunay](https://stackoverflow.com/questions/36604172/difference-between-matlab-delaunayn-and-scipy-delaunay)
***
Import the necessary packages

    import matplotlib.pyplot as plt

matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. In matplotlib.pyplot various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes (please note that “axes” here and in most places in the documentation refers to the axes part of a figure and not the strict mathematical term for more than one axis).

    from mpl_toolkits.mplot3d import Axes3D
An Axes3D object is created just like any other axes using the projection=‘3d’ keyword. Create a new matplotlib.figure.Figure and add a new axes to it of type Axes3D:

    from matplotlib.ticker import LinearLocator
This module contains classes to support completely configurable tick locating and formatting. Although the locators know nothing about major or minor ticks, they are used by the Axis class to support major and minor tick locating and formatting. Generic tick locators and formatters are provided, as well as domain specific custom ones.
    import numpy as np
    import matplotlib.tri as mtri
link 👍 https://matplotlib.org/api/tri_api.html Unstructured triangular grid functions.`class matplotlib.tri.Triangulation(x, y, triangles=None, mask=None)`An unstructured triangular grid consisting of npoints points and ntri triangles. The triangles can either be specified by the user or automatically generated using a `Delaunay triangulation`.


    from scipy.spatial import Delaunay
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.Delaunay.html, the general syntax is  
`class scipy.spatial.Delaunay(points, furthest_site=False, incremental=False, qhull_options=None)` so we imported Delaunay from scipy.spatial. The `points : ndarray of floats, shape (npoints, ndim)` , 

    Coordinates of points to triangulate


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
Figure is drawn and axis are defined
    path=raw_input("Enter the path of the file\n") #path for opening the file is asked to the user
Open the ply file that has vertices and element face 0
***
    X=[]
    Y=[]
    Z=[]
    StartIndex=0
***
3 empty list and StartIndex is initialized with value 0

    f=open(path,'r')
    lines=f.readlines()
    f.close()
Open the files ,read them and then close,coordinates of the point cloud vertices are extracted from the file
   ***
    for i in lines:
	temp=i.split(' ')
	if (temp[0]=='element'):
		if (temp[1]=='vertex'):
			vertices=long(int(temp[2]))
		if (temp[1]=='face'):
			face=long(int(temp[2]))
***
Now go through each line if it starts with element then it can be element vertices some_value or element face some_value,so split the value with white spaces and then store them as a list in temp,now if temp list elements has a string name 'element' then we check whether next element in temp list is vertices or face, if vertices then store the no. of vertices in vertices using vertices=long(int(temp[2])) else if it is face then store the no. of faces in face using face=long(int(temp[2]))
***
    print "The given file has %d number of vertices and %d number of faces" %(vertices,face)
    coordinates=[]
***
Make a empty list named as coordinates
***
    for i in range(len(lines)):
	temp=lines[i]
***
Store each line again in temp buffer and search for the line end header that denotes end of the ply file header and after it the value of vertex and face begins.
***
    if (temp=='end_header\n'):
***
As soon as we find it , store that line no. index in StartIndex and break
***   
    StartIndex=i+1
    break
***
Now the total no. of vertices will be from line having index - StartIndex to StartIndex+vertices ( the total value of vertices is stored in the variable vertices)
***
    for i in range(StartIndex,(StartIndex+vertices)):
    coordinates.append(lines[i])
***
Now coordinate was initialized now we append each line in the range in the coordinate list.The coordinates are appended in the list X, Y, Z .Now coordinate will contain X Y Z value split it and store it in X[] Y[] and Z[].
***
    for i in coordinates:
	point=i.split(' ')
	X.append(float(point[0]))
	Y.append(float(point[1]))
	Z.append(float(point[2]))

#a scatter plot is created
    surf = ax.scatter(X, Y, Z, zdir='y') 

#a window is created showing the scatter plot
    plt.show()

***
Now create a file named coord.ply using flag w+ and append all data now
***
    f=open("coord.ply","w+")
    s=[]
    for i in range(9):
	s.append("0")
'''X=[1,2,3,4]
Y=[5,3,9,6]
Z=[8,6,9,4]
'''
***
Make numpy arrat for X Y and Z co-ordinates
***
    u=np.array(X)
    v=np.array(Y)
    z=np.array(Z)
***
A useful link - https://stackoverflow.com/questions/39741163/delaunay-triangulation-of-point-cloud
***
`use of np.array.T` Same as self.transpose(), except that self is returned if self.ndim < 2.
https://docs.scipy.org/doc/scipy/reference/tutorial/spatial.html
***
    tri = Delaunay(np.array([u,v]).T)
the type of tri is <class 'scipy.spatial.qhull.Delaunay'>
***
    num=len(tri.simplices)
the type of tri.simplices is <type 'numpy.ndarray'>  
***
    s[0]="ply"
    s[1]="format ascii 1.0"
    s[2]="element vertex "+ str(len(X))
    s[3]="property float32 x"
    s[4]="property float32 y"
    s[5]="property float32 z"
    s[6]="element face "+str(num)
    s[7]="property list uint8 int32 vertex_indices"
    s[8]="end_header"
    for i in range(len(s)):
	f.write(s[i]+"\n")
    for i in range(len(X)):
	f.write(str(X[i])+" ")
	f.write(str(Y[i])+" ")
	f.write(str(Z[i])+"\n")
***
Till here we have append all data including the vertices in the ply file .Now we add the face data in the file
***
tri.simplices is a numpy array and returns numpy array containing coordinate of faces,so now we traverse each face coordinate using vert and then add 3 in front of it and then write the coordinate forming a triangular face
***
    for vert in tri.simplices:
        f.write("3 "+str(vert[0])+" ")
        f.write(str(vert[1])+" ")
        f.write(str(vert[2])+"\n")
     fig = plt.figure()
     ax = fig.gca(projection='3d')

     ax.plot_trisurf(X, Y, Z, linewidth=0.2, antialiased=True)

     plt.show()
***
Then we use [trisurf](https://plot.ly/python/trisurf/) to plot it.

