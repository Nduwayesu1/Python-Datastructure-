import numpy as np

# creating numpy array
# 1-D array
my_array=np.array([10,20,60,90])
my_array2=np.array([10,40,89,96])

# adding the arrays
result=np.add(my_array,my_array2)
print("My 1-D Array:")
print(result)
# 2-D Array
my_2D=np.array([[10,6,3,38],[12,7,39,7]])
print("My 2-D Array:")
print(my_2D)

# 3-D Array 
# Formula (number_of_layers,number_of_rows_each_layers,number_of_column_of_each_layer)
my_3D=np.array(  [ [ [1,2,6],[10,6,8] ],
               
                    [[20,7,12],[12,7,18]],
                    [[1,10,15],[16,33,28]] ]
) # (3,3,3)

print("Printing The number of 3-D Array:")
print(my_3D)


# Accessing Array properties
print("3-D Array:")
print(np.ndim(my_3D))
print(np.size(my_3D))
print(np.shape(my_3D))

print("2-D Array:")
print(np.ndim(my_2D))
print(np.size(my_2D))
print(np.shape(my_2D))

print("1-D Array:")
print(np.ndim(my_array))
print(np.size(my_array))
print(np.shape(my_array))