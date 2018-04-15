import numpy as np

def arrays(arr):
   return(np.array(arr[::-1], float))

def np_revers():    
    arr = input().strip().split(' ')
    ##simple input
    ##1 2 3 4 -8 -10

    result = arrays(arr)
    print(result)


'''
shape and reshape

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print(change_array)
#Output
[[1 2]
[3 4]
[5 6]]

my_array = numpy.array([1,2,3,4,5,6])
print(numpy.reshape(my_array,(3,2)))

#Output
[[1 2]
[3 4]
[5 6]]
'''
def reshape_arr():
    ##simple input 1 2 3 4 5 6 7 8 9
    arr = np.array(list(map(int,input().split())))
    arr.shape = (3,3)
    print(arr)


'''
transpose and flatten
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(numpy.transpose(my_array))

#Output
[[1 4]
 [2 5]
 [3 6]]

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(my_array.flatten())

#Output
[1 2 3 4 5 6]
'''
def transpose_and_flatten():
   '''
   simple input
   2 2
   1 2
   3 4
   '''
   n, m = map(int, input().split())
   arr = np.array([input().strip().split() for _ in range(n)], int)
   print(arr.transpose())
   print(arr.flatten())

'''
concatenate

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print(numpy.concatenate((array_1, array_2, array_3)))

#Output
[1 2 3 4 5 6 7 8 9]

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print(numpy.concatenate((array_1, array_2), axis = 1))

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]] 
'''

def concat():
   '''
   simple imput
   4 3 2
   1 2
   1 2 
   1 2
   1 2
   3 4
   3 4
   3 4 
   '''
   n, m, p = map(int, input().strip().split())
   arr = np.array(input().strip().split(), int)
   for i in range(1, n + m):
      arr = np.vstack((arr, np.array(input().strip().split(), int)))
   print(arr)

   

concat()
