from cergen import *
import numpy as np
import math

def test_fundamental_functionalities():
    

    raw_arr_4D = nest_list(list(range(1, 121)), (4, 3, 2, 5))
    print("TRANSPOZE")
    arr_4D = np.array(raw_arr_4D)
    print(np.transpose(arr_4D))
    print(get_transpose_of_nested_list(raw_arr_4D))

    raw_arr_3D = nest_list(list(range(1, 25)), (2, 3, 4))
    print("TRANSPOZE")
    arr_3D = np.array(raw_arr_3D)
    print(np.transpose(arr_3D))
    print(get_transpose_of_nested_list(raw_arr_3D))

    raw_arr_2D = nest_list(list(range(1, 7)), (2, 3))
    print("TRANSPOZE")
    arr_2D = np.array(raw_arr_2D)
    print(np.transpose(arr_2D))
    print(get_transpose_of_nested_list(raw_arr_2D))

    raw_arr_1D = nest_list(list(range(1, 4)), (3,))
    print("TRANSPOZE")
    arr_1D = np.array(raw_arr_1D)
    print(np.transpose(arr_1D))
    print(get_transpose_of_nested_list(raw_arr_1D))


def test():
    test_fundamental_functionalities()


if __name__ == "__main__":
    test()
