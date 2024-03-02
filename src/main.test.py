from cergen import *

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
    print(gergo.D)
    print(gergo[0])

    print()

    boyut = (1, 1, 2, 1, 1, 1, 1, 1, 1, 1)
    aralik = (1, 8)
    dagilim = 'uniform'
    gergo = rastgele_dogal(boyut, aralik, dagilim)
    print(gergo)
    print(gergo.D)
    print(gergo[0, 0, 1], gergo[0][0][1])

    print()


def test():
    test_fundamental_functionalities()


if __name__ == "__main__":
    test()
