#You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

import numpy as np

num_list = list(map(int,input().split()))
convert_array = np.array(num_list)
print(convert_array.reshape(3,3))
