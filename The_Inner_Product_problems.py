# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from vec import *



## 1: (Problem 1) Norm
norm1 = 3
norm2 = 4
norm3 = 3



## 2: (Problem 2) Closest Vector
# Write each vector as a list
closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## 3: (Problem 3) Projection Orthogonal to and onto Vectors
# Write each vector as a list
# round up to 6 decimal points if necessary
project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-0.166667,-0.333333,0.166667]
projection_orthogonal_2 = [1.166667,1.333333,3.833333]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



def project_onto_1(b, a):
    sigma = (b*a)/(a*a) if a*a > 1e-20 else 0
    #print (sigma * a)
    return (sigma * a)

def project_orthogonal_1(b, a):
    #print (b - project_onto_1(b, a))
    return (b - project_onto_1(b, a))

a = Vec({0,1,2},{0:3,1:3,2:12})
b = Vec({0,1,2},{0:1,1:1,2:4})
#print(project_onto_1(b, a))
#print(project_orthogonal_1(b, a))
