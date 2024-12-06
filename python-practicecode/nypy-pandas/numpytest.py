import sys
# import numpy as np
# lst = [56, 45, 12, 6] 
# lst = [1, 2, 3, 'text', True, 3+2j]


# print(sys.getsizeof(lst))
# j=0
# for i in lst:
#     j=j+i
# print(j)    


# lst = [5, 10, 0, 200] 
# import numpy as np
# arr = np.array(lst)
# print(arr + 1)

# lst = [1, 2, 3,'test'] 

# arr = np.array(lst) #, 'text', True, 3+2j
# print(type(arr[0]),type(arr[3]))
# print(arr.nbytes)


# print(np.arange(0, 10, 1.33, dtype = np.float64))

# print(np.result_type( np.linspace(0, 160, 2, dtype = np.float64)))

 
''' Method I: Using array and reshape to convert array into matrix '''
# print(np.array([5,6,8,45,12,52]).reshape(2,3))
# # [[ 5  6  8]
# #  [45 12 52]]
# ''' Method II: Using matrix function '''
# print(np.matrix([[1,2],
#                 [3,4]]))
# # [[1 2]
# #  [3 4]]
# ''' Method III: Using misc. functions '''
# print(np.eye(3)) # Identity matrix
# # [[ 1.  0.  0.]
# #  [ 0.  1.  0.]
# #  [ 0.  0.  1.]]
# print( np.zeros( (4,3) ) )
# # [[ 0.  0.  0.]
# #  [ 0.  0.  0.]
# #  [ 0.  0.  0.]
# #  [ 0.  0.  0.]]
# print(np.ones( (3,3), dtype = np.float64 ))
# # [[ 1.  1.  1.]
# #  [ 1.  1.  1.]
# #  [ 1.  1.  1.]]
 

# arr1 = [25, 56, 12, 85, 34, 75] 
# arr2 = [42, 3, 86, 32, 856, 46]

# narr=np.random.rand(len(arr1))
# print(narr)

# arr1_dtype_changed=(np.array(arr1).astype(complex))
# print(arr1_dtype_changed)

# arr1_mat=np.array([arr1]).reshape(2,3).astype(complex)
# print(arr1_mat)
# arr2_mat=np.array([arr2]).reshape(2,3).astype(complex)
# print(arr2_mat)

# resutl=((arr1_mat)**2-(arr2_mat)**2)/((arr1_mat)-(arr2_mat))
# print(resutl)


# arr1 = np.ones(10)
# arr2 = np.arange(10, dtype = np.float64)
# arr3 = arr1 + arr2
# print(arr1)
# print(arr2)
# print(arr3)
# print(np.result_type(arr1))
# print(np.result_type(arr3))

# arr = np.arange(4)
# arr.reshape(2,2)
# print(arr)
# print(arr.shape)
# arr = np.arange(4).reshape(4,-1)
# print(arr)
# print(arr.shape)