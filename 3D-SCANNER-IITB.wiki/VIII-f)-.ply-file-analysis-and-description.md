1. The element faces describes how many faces (polygon) there are in all of the ply files.
Faces are polygons. After reading the vertices start reading the faces. Each face line starts with the number of vertices in the polygon(i.e. if 3 then triangle, if 4 then it can be square/rectangle). Then that number of 0-offset polygon vertex indices follow.
Remove the {..........} before using practically ,
***
    ply
    format ascii 1.0           { ascii/binary, format version number }
    comment made by Greg Turk  { comments keyword specified, like all lines }
    comment this file is a cube
    element vertex 8           { define "vertex" element, 8 of them in file }
    property float x           { vertex contains float "x" coordinate }
    property float y           { y coordinate is also a vertex property }
    property float z           { z coordinate, too }
    element face 6             { there are 6 "face" elements in the file }
    property list uchar int vertex_index { "vertex_indices" is a list of ints }
    end_header                 { delimits the end of the header }
    0 0 0                      { start of vertex list }
    0 0 1
    0 1 1
    0 1 0
    1 0 0
    1 0 1
    1 1 1
    1 1 0
    4 0 1 2 3                  { start of face list }
    4 7 6 5 4
    4 0 4 5 1
    4 1 5 6 2
    4 2 6 7 3
    4 3 7 4 0
If you take a look at where the face list starts and you count to the end, then you should count 6. And the element faces also says 6 to confirm it.So total 8 vertices, 6 faces and each face is a square,so a cube.
***
2. https://stackoverflow.com/questions/24635334/generated-corrupt-large-ply-file-how-to-find-the-error
***
3. https://stackoverflow.com/questions/28458673/ply-file-specifications-with-texture-coordinates