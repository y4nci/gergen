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
    print(gergo2)
    print(gergo2.D)
    print(gergo2[0, 0, 1], gergo2[0][0][1])

    print()

    print("toploo", gergo1 + gergo2)

    print("toploo", gergo1 + 5)




def test():
    test_fundamental_functionalities()


if __name__ == "__main__":
    test()
