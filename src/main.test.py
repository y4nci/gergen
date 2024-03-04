from cergen import *
import numpy as np
import math

def test_fundamental_functionalities():
    boyut = ()
    aralik = (31.0, 91.0)
    dagilim = 'uniform'
    print(rastgele_gercek(boyut, aralik, dagilim))

    print()

    boyut = (2, 3)
    aralik = (1.0, 8.0)
    dagilim = 'uniform'
    print(rastgele_gercek(boyut, aralik, dagilim))

    print()

    boyut = (4, 3, 4)
    aralik = (1.0, 8.0)
    dagilim = 'uniform'
    print(rastgele_gercek(boyut, aralik, dagilim))

    print()

    boyut = ()
    aralik = (31, 91)
    dagilim = 'uniform'
    gergo = rastgele_dogal(boyut, aralik, dagilim)
    print(gergo)
    print(gergo.D)

    print()

    boyut = (2, 3)
    aralik = (1, 8)
    dagilim = 'uniform'
    gergo = rastgele_dogal(boyut, aralik, dagilim)
    print(gergo)
    print(gergo.D)
    print(gergo[0])

    print()

    boyut = (4, 3, 4)
    aralik = (1, 8)
    dagilim = 'uniform'
    gergo = rastgele_dogal(boyut, aralik, dagilim)
    print(gergo)
    print(gergo.devrik())
    print(gergo[0])

    print()

    boyut = (2, 2, 2)
    aralik = (1, 8)
    dagilim = 'uniform'
    gergo1 = rastgele_dogal(boyut, aralik, dagilim)
    print("gergo 1: ", gergo1)
    print(gergo1.D)
    print(gergo1[0])

    print()

    boyut = (2, 2, 2)
    aralik = (1, 8)
    dagilim = 'uniform'
    gergo2 = rastgele_dogal(boyut, aralik, dagilim)
    print("gergo 2:", gergo2)
    print(gergo2.D)
    print(gergo2[0, 0, 1], gergo2[0][0][1])

    print()

    gergo3 = gergo1 + gergo2

    print('GERGOOOOOOOOOOO3: ', gergo3)

    print("toploo", gergo3 + gergo2)

    print("toploo", gergo3 + 5)

    print("cikartoo", gergo3 - 5)

    print("carp", gergo3 * 5)

    print("bol", gergo3 / gergo2)

    print("zor carpoo", gergo3 * gergo2)

    print(unnest_list([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]))

    print(gergen([[[[[[[[[100000000]]]]], [[1000]]]]]]).log())

    print(nest_list([1, 2, 3, 4, 5, 6], (1, 2, 3)))

    print(get_dimensions_of_nested_list(nest_list([1, 2, 3, 4, 5, 6], (1, 2, 3))))

    print(nest_list([1, 2, 3, 4, 5, 6, 7, 8], (2, 2, 2)))

    print(get_dimensions_of_nested_list(nest_list([1, 2, 3, 4, 5, 6, 7, 8], (2, 2, 2))))

    print()
    print()
    print()
    print()

    raw_arr = nest_list(list(range(1, 121)), (4, 3, 2, 5))
    arr = np.array(raw_arr)
    print(arr, np.sum(arr, axis=0), np.sum(arr, axis=1), np.sum(arr, axis=2), np.sum(arr, axis=3))

    print("NOW GERGO")

    gergo_from_arr = gergen(raw_arr)
    print(gergo_from_arr, gergo_from_arr.topla(eksen=0), gergo_from_arr.topla(eksen=1), gergo_from_arr.topla(eksen=2), gergo_from_arr.topla(eksen=3))

    print()

    print()
    print()
    print()
    print()

    raw_arr = nest_list(list(range(1, 121)), (4, 3, 2, 5))
    arr = np.array(raw_arr)
    print(arr, np.average(arr, axis=0), np.average(arr, axis=1), np.average(arr, axis=2), np.average(arr, axis=3))

    print("NOW GERGO")

    gergo_from_arr = gergen(raw_arr)
    print(gergo_from_arr, gergo_from_arr.ortalama(eksen=0), gergo_from_arr.ortalama(eksen=1), gergo_from_arr.ortalama(eksen=2), gergo_from_arr.ortalama(eksen=3))

    print()
    print()
    print()
    print()

    left_carpim = gergen([[1, 2], [3, 4]])
    right_carpim = gergen([[5, 6], [7, 8]])

    print(left_carpim.ic_carpim(right_carpim))

    left_carpim = gergen([[1, 2, 3, 4]])
    right_carpim = gergen([[5], [6], [7], [8]])

    print(left_carpim.ic_carpim(right_carpim))

    left_carpim = gergen([1, 2, 3, 4])
    right_carpim = gergen([5, 6, 7, 8])

    print(left_carpim.dis_carpim(right_carpim))


def test():
    test_fundamental_functionalities()


if __name__ == "__main__":
    test()
