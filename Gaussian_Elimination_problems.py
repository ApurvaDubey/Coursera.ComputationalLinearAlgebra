# version code f4bde2e5d0a5+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from vec import Vec
from vecutil import zero_vec

## 1: (Problem 1) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
                  [0,1,0,3,4],
                  [0,0,2,3,4],
                  [0,0,0,2,0],
                  [0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
                  [0,0,4,2,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
                  [0,0,0,1],
                  [0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]



## 2: (Problem 2) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
    is_echelon([[9,-1,2],[0,4,5],[0,0,2]])
        True
    is_echelon([[0,4,5],[0,3,0],[0,0,2]])
        False
    is_echelon([[9,10]])
        True
    is_echelon([[5]])
        True
    is_echelon([[1],[1]])
        False
    is_echelon([[0]])
        True
    is_echelon([[0],[1]])
        False
    '''
    # L=[[0]]

    dic={i:-1 for i,v in enumerate(A)}

    flag=True

    for i,v in enumerate(A):

        for j,e in enumerate(v):
            #print (i,v,j,v[j],v[j-1])
            if (j==0 and v[j] !=0):
                dic[i]=-1
                break
            elif (v[j]!=0 and v[j-1]==0):
                dic[i]=j
                break
            elif (v[j]==0 and j==len(v)-1):
                dic[i]=len(v)-1+i
                break
            
    # print (dic)

    for k in sorted(dic.keys()):
        if (k > 0 and dic[k] <= dic[k-1]):
            flag=False

    return flag

    #print(flag)

## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list
        

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## 5: (Problem 5) Echelon Solver
def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    D = {'A','B','C','D','E'}
    U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    b_list = [one,0,one]
    cols = ['A', 'B', 'C', 'D', 'E']
    echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    '''

    x = zero_vec(row_list[0].D)
    #print (x,len(row_list[0].D))
    for j in reversed(range(len(row_list))):
        #c = label_list[j]
        #print(j,row_list[j])
        d=row_list[j].f
        #print (d)
        for z in label_list:
            if d.get(z,0) !=0:
                #print (z,d,d.get(z,0))
                x[z] = (b[j] - x*row_list[j])/d.get(z,0)
                break
    #print (x)        
    return x

#D = {'A','B','C','D','E'}
#U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
#b_list = [one,0,one]
#cols = ['A', 'B', 'C', 'D', 'E']
#print(echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one}))
    
#v1 = Vec({'a','b','c'}, {'b':1, 'c':3})
#v2 = Vec({'a','b','c'}, {'c':2})
#v3 = Vec({'a','b','c'}, {})
#b = [12,6,0]
#rowlist = [v1,v2,v3]
#label_list=['a','b','c']
#print(echelon_solve(rowlist,label_list, b))



## 6: (Problem 6) Solving General Matrices via Echelon
D={'A','B','C','D'}
row_list = [Vec(D, {'A':one, 'B':one, 'D':one}), Vec(D, {'B':one}), Vec(D,{'C':one}), Vec(D,{'D':one})]    # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one,one,0,0]          # Provide as a list of GF(2) values
#print(echelon_solve(row_list,label_list, b))


def solve(A, b):
    M = echelon.transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    row_list = [U_rows_dict[i] for i in sorted(U_rows_dict)]
    return echelon_solve(row_list,col_label_list, M*b)




## 7: (Problem 7) Nullspace A
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## 8: (Problem 8) Nullspace B
null_space_rows_b = {4} # Put the row numbers of M from the PDF

