import numpy as np

'''
a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]

print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
'''
def mathematics():
    '''
    simple input
    1 4
    1 2 3 4
    5 6 7 8
    '''
    n, m = map(int, input().split())
    a, b = (np.array([input().split()
                      for _ in range(n)], dtype = int)
            for _ in range(2))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(a**b)

'''
floor

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print9numpy.floor(my_array))         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

ceil

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.ceil(my_array))          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

rint

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.rint(my_array))          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''
def floor_ceil_rint():
    ##simple input 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
    arr = np.array(input().split(), float)
    print(np.floor(arr))
    print(np.ceil(arr))
    print(np.rint(arr))

'''
sum

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0))         #Output : [4 6]
print(numpy.sum(my_array, axis = 1))         #Output : [3 7]
print(numpy.sum(my_array, axis = None))      #Output : 10
print(numpy.sum(my_array))                   #Output : 10

prod

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24
'''
def sum_and_prod():
    '''
    simple input
    2 2
    1 2
    3 4
    '''
    n, m =map(int, input().split())
    arr = np.array([input().split()
                    for _ in range(n)], int)
    print(np.sum(arr, axis=0))
    print(np.prod(arr, axis=0))
    print(np.prod(np.sum(arr, axis=0),axis=0))

'''
min

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.min(my_array, axis = 0))         #Output : [1 0]
print(numpy.min(my_array, axis = 1))         #Output : [2 3 1 0]
print(numpy.min(my_array, axis = None))      #Output : 0
print(numpy.min(my_array))                   #Output : 0

max

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.max(my_array, axis = 0))         #Output : [4 7]
print(numpy.max(my_array, axis = 1))         #Output : [5 7 3 4]
print(numpy.max(my_array, axis = None))      #Output : 7
print(numpy.max(my_array))                   #Output : 7
'''

def min_and_max():
    '''
    simple input
    4 2
    2 5
    3 7
    1 3
    4 0
    '''
    n, m =map(int, input().split())
    arr = np.array([input().split()
                    for _ in range(n)], int)
    print(np.max(np.min(arr, axis=1)))

