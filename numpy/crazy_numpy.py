import numpy as np

'''
mean

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(numpy.mean(my_array, axis = 1)))        #Output : [ 1.5  3.5]
print(numpy.mean(my_array, axis = None))     #Output : 2.5
print(numpy.mean(my_array))                  #Output : 2.5

varianse

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
print(numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
print(numpy.var(my_array, axis = None))      #Output : 1.25
print(numpy.var(my_array))                   #Output : 1.25

standard deviation

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.std(my_array, axis = 0))         #Output : [ 1.  1.]
print(numpy.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
print(numpy.std(my_array, axis = None))      #Output : 1.11803398875
print(numpy.std(my_array))                   #Output : 1.11803398875
'''
def print_mean_var_std():
    '''
    simple input
    2 2
    1 2
    3 4
    '''
    arr = np.array([input().split()
                  for _ in range(int(input().split()[0]))], int)
    print(np.mean(arr, axis=1), np.var(arr, axis=0), np.std(arr), sep="\n")

'''
dot

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.dot(A, B))       #Output : 11

cross

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.cross(A, B))     #Output : -2
'''
def print_dot_product():   
    '''
    simple input
    2
    1 2
    3 4
    1 2
    3 4
    '''
    n = int(input())
    a = np.array([input().split() for _ in range(n)], int)
    b = np.array([input().split() for _ in range(n)], int)
    print(np.dot(a, b))

'''
inner

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.inner(A, B))     #Output : 4

outer

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.outer(A, B))     #Output : [[0 0]
                             #          [3 4]]
'''
def print_inner_outer():
    '''
    simple input
    0 1
    2 3
    '''
    A = np.array(input().split(), int)
    B = np.array(input().split(), int)
    print(np.inner(A,B), np.outer(A,B), sep="\n")

'''
poly

print(numpy.poly([-1, 1, 1, 10]))        #Output : [  1 -11   9  11 -10]

root

print(numpy.roots([1, 0, -1]))           #Output : [-1.  1.]

polyint

print(numpy.polyint([1, 1, 1]))          #Output : [ 0.33333333  0.5         1.          0.        ]

polyder

print(numpy.polyder([1, 1, 1, 1]))       #Output : [3 2 1]

polyval

print(numpy.polyval([1, -2, 0, 2], 4))   #Output : 34

polyfit

print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2))
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
'''

def polynomials():
    '''
    simple input
    1.1 2 3
    0
    '''
    print(np.polyval(list(map(float, input().split())), int(input())))


'''
liner algebra

linalg.det

print(numpy.linalg.det([[1 , 2], [2, 1]]))       #Output : -3.0

linalg.eig

vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print(vals)                                      #Output : [ 3. -1.]
print(vecs)                                      #Output : [[ 0.70710678 -0.70710678]
                                                 #          [ 0.70710678  0.70710678]]
linalg.inv
print(numpy.linalg.inv([[1 , 2], [2, 1]]))       #Output : [[-0.33333333  0.66666667]
                                                 #          [ 0.66666667 -0.33333333]]
'''

def print_determinat():
    '''
    simple input
    2
    1.1 1.1
    1.1 1.1
    '''
    N = int(input())
    print(np.linalg.det(np.array([input().split() for _ in range(N)], float)))
