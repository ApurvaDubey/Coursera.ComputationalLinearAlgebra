# version code 7f08c507c12c+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import *
from orthogonalization import *
import math

def project_onto_1(b, a):
    sigma = (b*a)/(a*a) if a*a > 1e-20 else 0
    #print (sigma * a)
    return (sigma * a)

def project_orthogonal_1(b, a):
    #print (b - project_onto_1(b, a))
    return (b - project_onto_1(b, a))

#a = Vec({0,1,2},{0:3,1:3,2:12})
#b = Vec({0,1,2},{0:1,1:1,2:4})
#print(project_onto_1(b, a))
#print(project_orthogonal_1(b, a))

## 1: (Problem 1) Generators for orthogonal complement
U_vecs_1 = [list2vec([0,0,3,2])]
W_vecs_1 = [list2vec(v) for v in [[1,2,-3,-1],[1,2,0,1],[3,1,0,-1],[-1,-2,3,1]]]

#print (orthogonalize(list(set(U_vecs_1) | set(W_vecs_1))))

# Give a list of Vecs
ortho_compl_generators_1 = [Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 3, 3: 2}), \
                            Vec({0, 1, 2, 3},{0: 3.0, 1: 1.0, 2: 0.46153846153846156, 3: -0.6923076923076923}), \
                            Vec({0, 1, 2, 3},{0: -0.2086330935251799, 1: 1.5971223021582734,\
                                              2: -0.6474820143884894, 3: 0.9712230215827338})]

U_vecs_2 = [list2vec([3,0,1])]
W_vecs_2 = [list2vec(v) for v in [[1,0,0],[1,0,1]]]

# Give a list of Vecs
ortho_compl_generators_2 = ...

U_vecs_3 = [list2vec(v) for v in [[-4,3,1,-2],[-2,2,3,-1]]]
W_vecs_3 = [list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]

# Give a list of Vecs
ortho_compl_generators_3 = ...



## 2: (Problem 2) Basis for null space
# Your solution should be a list of Vecs
null_space_basis = ...



## 3: (Problem 3) Orthonormalize(L)
def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ... 
    <BLANKLINE>
        a     b     c     d
    -----------------------
     0.73 0.548 0.183 0.365
    <BLANKLINE>
         a     b      c      d
    --------------------------
     0.187 0.403 -0.566 -0.695
    <BLANKLINE>
         a      b      c     d
    --------------------------
     0.528 -0.653 -0.512 0.181
    '''
    

    #D = {'a','b','c','d'}
    #L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}),Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    Lstar=orthogonalize(L)
    Lorthnorm=[]

    for i,v in enumerate(Lstar):
        Lorthnorm.append(v/math.sqrt(v*v))
        #print (v/math.sqrt(v*v))
    return Lorthnorm

D = {'a','b','c','d'}
L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}),Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
#print (orthonormalize(L))


## 4: (Problem 4) aug_orthonormalize(L)
def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
            
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat
    >>> print(coldict2mat(Qlist))
    <BLANKLINE>
               0      1      2
         ---------------------
     a  |   0.73  0.187  0.528
     b  |  0.548  0.403 -0.653
     c  |  0.183 -0.566 -0.512
     d  |  0.365 -0.695  0.181
    <BLANKLINE>
    >>> print(coldict2mat(Rlist))
    <BLANKLINE>
              0    1      2
         ------------------
     0  |  5.48 8.03   9.49
     1  |     0 11.4 -0.636
     2  |     0    0   6.04
    <BLANKLINE>
    >>> print(coldict2mat(Qlist)*coldict2mat(Rlist))
    <BLANKLINE>
           0  1  2
         ---------
     a  |  4  8 10
     b  |  3  9  1
     c  |  1 -5 -1
     d  |  2 -5  5
    <BLANKLINE>
    '''
    

    #D={'a','b','c','d'}
    #L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    LorthoGonal , sigma_vecs= (aug_orthogonalize(L))

    Qlist=[]
    Rlist=[]
    norms=[]

    for i,v in enumerate(LorthoGonal):
        Qlist.append(v/math.sqrt(v*v))
        norms.append(math.sqrt(v*v))

    sigma_vecs = (mat2coldict(rowdict2mat(sigma_vecs)))

    for i in range(len(sigma_vecs)):
        sigma_vecs[i] = (norms[i]*sigma_vecs[i])

    Rlist=[v for k,v in (mat2coldict(rowdict2mat(sigma_vecs))).items()]

    R = coldict2mat(Rlist)
    Q = coldict2mat(Qlist)

    #return (Q,R,Q*R)
    return (Qlist, Rlist)

D={'a','b','c'}
L = [Vec(D, {'a':6,'b':2,'c':3}), Vec(D, {'a':6,'b':0,'c':3})]

Qlist, Rlist = (aug_orthonormalize(L))
#print(coldict2mat(Qlist),coldict2mat(Rlist))

## 5: (Problem 5) QR factorization of small matrices
#Compute the QR factorization

#Please represent your solution as a list of rows, such as [[1,0,0],[0,1,0],[0,0,1]]

part_1_Q = [[0.857,0.256],[0.286,-0.958],[0.429,0.128]] 
part_1_R =  [[7,6.43],[0,1.92]]

part_2_Q = [[0.667,0.707],[0.667,-0.707],[0.333,0]]
part_2_R = [[3,3],[0,1.41]]




## 6: (Problem 6) QR Solve
from matutil import mat2coldict, coldict2mat
from python_lab import dict2list, list2dict
from triangular import *

def QR_factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R


def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor, which in turn uses dict2list and list2dict.
           You wrote these procedures long back in python_lab.  Make sure the completed python_lab.py
           is in your matrix directory.
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''

    #domain = ({'a','b','c'},{'A','B'})
    #A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
    Q, R = QR_factor(A)
    #print(Q,R)
    #b = Vec(domain[0], {'a': 1, 'b': -1})

    c = (Q.transpose()*b)
    R_rowlist=[v for k,v in (mat2rowdict(R)).items()]
    #print((R_rowlist))
    label_list=sorted(R.D[1], key=repr)

    return (triangular_solve(R_rowlist,label_list, c))


## 7: (Problem 7) Least Squares Problem
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]])
least_squares_b1 = list2vec([10, 8, 6])

#print(QR_solve(least_squares_A1, least_squares_b1))
#tmp1 = (least_squares_A1*QR_solve(least_squares_A1, least_squares_b1)-least_squares_b1)
#print (math.sqrt(tmp1*tmp1))
x_hat_1 = QR_solve(least_squares_A1, least_squares_b1)


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

#tmp2 = (least_squares_A2*QR_solve(least_squares_A2, least_squares_b2)-least_squares_b2)
#print(math.sqrt(tmp2*tmp2))
x_hat_2 = QR_solve(least_squares_A2, least_squares_b2)



## 8: (Problem 8) Small examples of least squares
#Find the vector minimizing (Ax-b)^2

#Please represent your solution as a list
v1=QR_solve(listlist2mat([[8, 1], [6, 2], [0, 6]]), list2vec([10,8,6]))
v2=QR_solve(listlist2mat([[3, 1], [4, 1]]), list2vec([10,13]))



your_answer_1 = [(v1.f)[d] for d in sorted(list(v1.D))]
your_answer_2 = [(v2.f)[d] for d in sorted(list(v2.D))]


## 9: (Problem 9) Linear regression example
#Find a and b for the y=ax+b line of best fit

a = ...
b = ...

