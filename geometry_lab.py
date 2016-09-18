# version code 77ed2409f40d+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# version code 05f5a0d767f0+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
from matutil import *
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    it defines the default value of labels to be {'x','y','u'}.
    You should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  If you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  

    >>> identity()==Mat(({'x','y','u'},{'x','y','u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1})
    True
    >>> identity({'r','g','b'})==Mat(({'r','g','b'},{'r','g','b'}), {('r','r'):1, ('g','g'):1, ('b','b'):1})
    True
    '''
    return Mat((labels,labels), {(d,d):1 for d in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.

    >>> translation(9,10)==Mat(({'x','y','u'},{'x','y','u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1, ('y','u'):10, ('x','u'):9})
    True
    '''
    labels = {'x','y','u'}
    Mat_Trans = Mat((labels,labels), {(d,d):1 for d in labels})
    Mat_Trans[('x','u')]=x
    Mat_Trans[('y','u')]=y

    return Mat_Trans

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.

    >>> scale(3,4)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'x':3, 'y':4, 'u':1})
    True
    >>> scale(0,0)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'u':1})
    True
    '''
    labels = {'x','y','u'}
    Mat_Scale = Mat((labels,labels), {(d,d):1 for d in labels})
    Mat_Scale[('x','x')]=a
    Mat_Scale[('y','y')]=b

    return Mat_Scale
    
## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.

    >>> def normsq(v): return v*v
    >>> normsq(rotation(math.pi) * Vec({'u', 'x', 'y'},{'x':1,'y':2,'u':1}) - Vec({'u', 'x', 'y'},{'u': 1, 'x': -1, 'y': -2})) < 1e-15
    True
    >>> normsq(rotation(math.pi/2) * Vec({'u', 'x', 'y'},{'x':3,'y':1,'u':1}) - Vec({'u', 'x', 'y'},{'u': 1, 'x': -1, 'y': 3.0})) < 1e-15
    True
    '''
    labels = {'x','y','u'}
    Mat_Rotate = Mat((labels,labels), {(d,d):1 for d in labels})
    Mat_Rotate[('x','x')]=math.cos(angle)
    Mat_Rotate[('y','y')]=math.cos(angle)
    Mat_Rotate[('x','y')]=-1*math.sin(angle)
    Mat_Rotate[('y','x')]=math.sin(angle)

    return Mat_Rotate

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''

    return (translation(x,y) * rotation(angle) * translation(-x,-y))

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.

    >>> v = Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1})
    >>> reflect_y()*v == Vec({'x','y','u'}, {'x':-1, 'y':1, 'u':1})
    True
    >>> w = Vec({'x','y','u'}, {'u':1})
    >>> reflect_y()*w == Vec({'x','y','u'},{'u':1})
    True
    '''
    labels = {'x','y','u'}
    Mat_RefY = Mat((labels,labels), {(d,d):1 for d in labels})
    Mat_RefY[('x','x')]=-1
    
    return Mat_RefY

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.

    >>> v = Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1})
    >>> reflect_x()*v == Vec({'x','y','u'}, {'x':1, 'y':-1, 'u':1})
    True
    >>> w = Vec({'x','y','u'}, {'u':1})
    >>> reflect_x()*w == Vec({'x','y','u'},{'u':1})
    True
    '''
    labels = {'x','y','u'}
    Mat_RefY = Mat((labels,labels), {(d,d):1 for d in labels})
    Mat_RefY[('y','y')]=-1
    
    return Mat_RefY

## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.

    >>> scale_color(1,2,3)*Vec({'r','g','b'},{'r':1,'g':2,'b':3}) == Vec({'r','g','b'},{'r':1,'g':4,'b':9})
    True
    '''
    labels = {'r','g','b'}
    Mat_Scale = Mat((labels,labels), {(d,d):1 for d in labels})
    Mat_Scale[('r','r')]=scale_r
    Mat_Scale[('g','g')]=scale_g
    Mat_Scale[('b','b')]=scale_b
    
    return Mat_Scale

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    labels = {'r','g','b'}
    Mat_GS = Mat((labels,labels), {(d,d):1 for d in labels})
    #Mat_GS=listlist2mat([[77/256,151/256,28/256],[77/256,151/256,28/256],[77/256,151/256,28/256]])
    Mat_GS[('r','r')]=77/256
    Mat_GS[('r','g')]=151/256
    Mat_GS[('r','b')]=28/256

    Mat_GS[('g','r')]=77/256
    Mat_GS[('g','g')]=151/256
    Mat_GS[('g','b')]=28/256
    
    Mat_GS[('b','r')]=77/256
    Mat_GS[('b','g')]=151/256
    Mat_GS[('b','b')]=28/256
    
    return Mat_GS

## Task 10
def reflect_about(x1, y1, x2, y2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.

    >>> def normsq(v): return v*v
    >>> normsq(reflect_about(0,1,1,1) * Vec({'x','y','u'}, {'u':1}) - Vec({'x', 'u', 'y'},{'x': 0.0, 'u': 1, 'y': 2.0})) < 10e-15
    True
    >>> normsq(reflect_about(0,0,1,1) * Vec({'x','y','u'}, {'x':1, 'u':1}) - Vec({'x', 'u', 'y'},{'u': 1, 'y': 1})) < 1e-15
    True
    '''
    pass


###

t = Vec({'x','y','u'}, {'x':1,'y':1,'u':1})
S=Mat(({'x','y','u'},{'x','y','u'}), {('x','y'):3, ('y','x'):4, ('u','u'):1})
#print (S*t)


