from cergen import *

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




def test():
    test_fundamental_functionalities()


if __name__ == "__main__":
    test()
