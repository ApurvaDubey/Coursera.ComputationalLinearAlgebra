# version code 3e169d60c2de+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 0.8.3) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    return [(x[0]+y[0], x[1]+y[1]) for (i,x) in enumerate(A)  for (j,y) in enumerate(B) if i==j]



## 2: (Problem 0.8.4) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    return { value:key for (key,value) in d.items() }



## 3: (Problem 0.8.5) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [ p+i for i in range(n) ]

comprehension_with_row = [row(i,20) for i in range(15)]

comprehension_without_row = [ list(range(x,x+20)) for x in range(20) if x+20 < 35]



## 4: (Problem 0.8.10) Probability Exercise 1
Pr_f_is_even = 0.7
Pr_f_is_odd  = 0.3



## 5: (Problem 0.8.11) Probability Exercise 2
Pr_g_is_1    = 0.4
Pr_g_is_0or2 = 0.6

