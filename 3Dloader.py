'''Open binary/ASCII STL, Wavefront OBJ, ASCII OFF, binary/ASCII PLY, XAML format files'''
'''Please donot use 'uint', 'uint8' and 'uint16' formats in the point cloud files'''
'''Team SAAS, Ekalavya 2017'''

import numpy as np
import trimesh
import cv2
print "Please give the file path"
path=raw_input()
mesh = trimesh.load_mesh(path)# load a file from its path
np.divide(mesh.volume, mesh.convex_hull.volume)
mesh.vertices -= mesh.center_mass # to set the volumetric center of mass as the origin of the object
mesh.show()
