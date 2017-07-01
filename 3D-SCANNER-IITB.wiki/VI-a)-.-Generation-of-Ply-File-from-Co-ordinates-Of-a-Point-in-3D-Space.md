PLY is a computer file format known as the Polygon File Format or the Stanford Triangle Format. It was principally designed to store three-dimensional data from 3D scanners. The data storage format supports a relatively simple description of a single object as a list of nominally flat polygons. A variety of properties can be stored, including: color and transparency, surface normals, texture coordinates and data confidence values. The format permits one to have different properties for the front and back of a polygon. There are two versions of the file format, one in ASCII, the other in binary.
The file format
Files are organized as a header, that specifies the elements of a mesh and their types, followed by the list of elements itself. The elements are usually vertices and faces, but may include other entities such as edges, samples of range maps, and triangle strips.

The header of both ASCII and binary files is ASCII text. Only the numerical data that follows the header is different between the two versions.
In computer programming, the term magic number has multiple meanings. It could refer to one or more of the following:
 The header always starts with a **"magic number"**, a line containing

**ply**


***

1.A constant numerical or text value used to identify a file format or protocol; for files, see List of file signatures.
***

2.Distinctive unique values that are unlikely to be mistaken for other meanings (e.g., Globally Unique Identifiers).
***

3.Unique values with unexplained meaning or multiple occurrences which could (preferably) be replaced with named constants.

***


After the ply header, the description of the File Type is made by anyone of the following-

     format ascii 1.0
     format binary_little_endian 1.0
     format binary_big_endian 1.0

Important Note- 
The ***'element'*** keyword introduces a description of how some particular data element is stored and how many of them there are. Hence, in a file where there are 12 vertices, each represented as a floating point (X,Y,Z) triple, one would expect to see:
     element vertex 12
The no. of vertex can be easily found out by the length of X co-ordinate or Y co-ordinate or Z co-ordinate.
     property float x
     property float y
     property float z

Other 'property' lines might indicate that colours or other data items are stored at each vertex and indicate the data type of that information. Regarding the data type there are two variants, depending on the source of the ply file. The type can be specified with one of char uchar short ushort int uint float double, or one of int8 uint8 int16 uint16 int32 uint32 float32 float64.
For an object with ten polygonal faces, one might see:

     element face 10 
#We are not using faces, faces are used to define texture and other properties , so we in our final .ply file that is generated, we are keeping face value 0
***
    property list uchar int vertex_indices
    #This line is also not used because face no. is 0

The word 'list' indicates that the data is a list of values, the first of which is the number of entries in the list (represented as a 'uchar' in this case). In this example each list entry is represented as an 'int'. At the end of the header, there must always be the line:

     end_header

***
Explanation of Code Build to Generate a .ply file from X ,Y and Z coordinate of a Point
***
     import numpy as np
     f=open("coord.ply","w+")
the w+ flag is used :+1:  Open for reading and writing.  The file is created if it does not exist, otherwise it is truncated.  The stream is positioned at the beginning of the file.
     s=[]
Initialize an empty list, and we are going to create 8 lines in a .ply general file , so make it's 8 elements as 0
***
     for i in range(9):
     s.append("0")
     #We have assumed X,Y,Z data from ourselves to show a creation
     X=[1,2,3,4]
     Y=[5,3,9,6]
     Z=[8,6,9,4]
     s[0]="ply"
     s[1]="format ascii 1.0"
     s[2]="element vertex "+ str(len(X))
     s[3]="property float32 x"
     s[4]="property float32 y"
     s[5]="property float32 z"
     s[6]="element face 0"
     s[7]="property list uint8 int32 vertex_indices"
     s[8]="end_header"
***
    #Writing the format of a .ply file into "coord.ply" file 
    for i in range(len(s)):
    f.write(s[i]+"\n")
***
    #Adding to .ply file from the coordinates in the list X,Y,Z respectively	
    for i in range(len(X)):
    f.write(str(X[i])+" ")
    f.write(str(Y[i])+" ")
    f.write(str(Z[i])+"\n")

Src :+1: https://en.wikipedia.org/wiki/PLY_(file_format) 
A Save.ply file is made in main directory with the link [SavePLY.py](https://github.com/animeshsrivastava24/3D-SCANNER-IITB/blob/master/SavePLY.py)
in which a function is created to write X,Y,Z coordinate to the final .ply file